# configuralble class is evil
#
# example:
#
# 1) basic class (works fine) 
#
#   class Page {
#
#       private final String uri;
#
#       Page(final String address) {
#           this.uri = address;
#       }
#
#       public String html() throws IOException { // read the content of a webpage, decoded by "UTF-8" 
#           return IOUtils.toString(new URL(this.uri).openStream(), "UTF-8");
#       }
#   }
#
#  // the client code: read the content of Google front page
#  String html = new Page("http://www.google.com").html();
#  
# (bad design)
#
# 2) extend the functionality of the class: can decode by "UTF-8" or others
# 
#   class Page {
#
#       private final String uri;
#       private final String encoding;      // a configurable field
#
#       Page(final String address, final String enc) {
#           this.uri = address;
#           this.encoding = enc;
#       }
#
#       public String html() throws IOException {
#           return IOUtils.toString(new URL(this.uri).openStream(), this.encoding);
#       }
#   }
#   // the class becomes a configurable class
#  
# 3) extend the functionality of the class: can handle an empty page
#
#   class Page {
#
#       private final String uri;
#       private final String encoding;      // a configurable field
#       private final boolean alwaysHtml;   // a configurable field
#
#       Page(final String address, final String enc, final boolean always) {
#           this.uri = address;
#           this.encoding = enc;
#           this.alwaysHtml = always;
#       }
#
#       public String html() throws IOException {
#           String html = IOUtils.toString(new URL(this.uri).openStream(), this.encoding);
#           if (html.isEmpty() && this.alwaysHtml) { // different behavior based on the configuration field
#               html = "<html/>";                    // return "<html/>" if an empty page is loaded
#           }
#           return html;
#       }
#   }
#  
# 4) extend the functionality of the class: can handle unknown encoding 
#
#   class Page {
#
#       private final String uri;
#       private final String encoding;      // a configurable field
#       private final boolean alwaysHtml;   // a configurable field
#       private final boolean encodeAnyway; // a configurable field
#
#       Page(final String address, final String enc, final boolean always, final boolean encode) {
#           this.uri = address;
#           this.encoding = enc;
#           this.alwaysHtml = always;
#           this.encodeAnyway = encode;
#       }
#
#       public String html() throws IOException, UnsupportedEncodingException {
#           final byte[] bytes = IOUtils.toByteArray(new URL(this.uri).openStream());
#           String html;
#
#           try {
#               html = new String(bytes, this.encoding); // can use different encoding
#           } catch (UnsupportedEncodingException ex) {
#               if (!this.encodeAnyway) {                // can handle unknown encoding or not
#                   throw ex;
#               }
#               html = new String(bytes, "UTF-8")
#           }
#
#           if (html.isEmpty() && this.alwaysHtml) {     // can handle empty page
#               html = "<html/>";
#           }
#           return html;
#       }
#   }
#  
#   (refinement)
#
#   class Page {
#
#       private final String uri;
#       private final PageSettings settings;             // encapsulate the setting in one object
#
#       Page(final String address, final PageSettings stts) {
#           this.uri = address;
#           this.settings = stts;
#       }
#
#       // one big method with many logics and case handling, hard to extend and maintain
#       public String html() throws IOException {
#           final byte[] bytes = IOUtils.toByteArray(new URL(this.uri).openStream());
#           String html;
#           try {
#               html = new String(bytes, this.settings.getEncoding());
#           } catch (UnsupportedEncodingException ex) {
#               if (!this.settings.isEncodeAnyway()) {
#                   throw ex;
#               }
#               html = new String(bytes, "UTF-8")
#           }
#           if (html.isEmpty() && this.settings.isAlwaysHtml()) {
#               html = "<html/>";
#           }
#           return html;
#       }
#   }
#  
#   // the client code
#   String html = new Page(
#       "http://www.google.com",
#       new PageSettings()
#           .withEncoding("ISO_8859_1")
#           .withAlwaysHtml(true)
#           .withEncodeAnyway(false)
#   ).html();
#  
#
###
#
#  (good design: use composable decorators)
#
#  // the client code
#  Page page = new NeverEmptyPage(new DefaultPage("http://www.google.com"))
#
#  String html = new AlwaysTextPage(new TextPage(page, "ISO_8859_1"), page).html();
#  
#
#  // implementation of classes
#
#  class DefaultPage implements Page {
#
#      private final String uri;
#
#      DefaultPage(final String address) {
#          this.uri = address;
#      }
#
#      @Override
#      public byte[] html() throws IOException {
#          return IOUtils.toByteArray(new URL(this.uri).openStream());
#      }
#  }
#
#  // a decorator class: 
#  //   new NeverEmptyPage(new DefaultPage("http://www.google.com"))
#
#  class NeverEmptyPage implements Page {
#
#      private final Page origin;
#
#      NeverEmptyPage(final Page page) {
#          this.origin = page;
#      }
#
#      @Override
#      public byte[] html() throws IOException { // enhance the html() method to handle empty page
#          byte[] bytes = this.origin.html();
#          if (bytes.length == 0) {
#              bytes = "<html/>".getBytes();
#          }
#          return bytes;
#      }
#  }
#  
#
#  // a decorator class: new TextPage(Page, "ISO_8859_1")
#
#  class TextPage {
#
#      private final Page origin;
#      private final String encoding; // an additional parameter for encoding
#
#      TextPage(final Page page, final String enc) {
#          this.origin = page;
#          this.encoding = enc;
#      }
#
#      public String html() throws IOException { // enhance the html() method to handle different encoding
#          return new String(this.origin.html(), this.encoding);
#      }
#  }
#
#  // a decorator class: new AlwaysTextPage(new TextPage(page, "ISO_8859_1"), Page)
#
#  class AlwaysTextPage {
#
#      private final TextPage origin;
#      private final Page source;
#
#      AlwaysTextPage(final TextPage ori, final Page src) {
#          this.origin = ori;
#          this.source = src;
#      }
#
#      public String html() throws IOException { // enchance the html() method to handle unknown encoding
#          String html;
#          try {
#              html = this.origin.html();
#          } catch (UnsupportedEncodingException ex) { // this creates another HTTP request
#              html = new TextPage(this.source, "UTF-8").html();
#          }
#          return html;
#      }
#  }
#  
#  class OncePage implements Page { // introduce one more decorator class to avoid duplicate HTTP request
#
#      private final Page origin;
#      private final AtomicReference<byte[]> cache = new AtomicReference<>;
#
#      OncePage(final Page page) {
#          this.origin = page;
#      }
#
#      @Override
#      public byte[] html() throws IOException {
#          if (this.cache.get() == null) {
#              this.cache.set(this.origin.html());
#          }
#          return this.cache.get();
#      }
#  }
#  
#  // the final client code
#
#  Page page = new NeverEmptyPage(new OncePage(new DefaultPage("http://www.google.com")))
#
#  String html = new AlwaysTextPage(new TextPage(page, "ISO_8859_1"), "UTF-8").html();
#  

