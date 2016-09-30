# configuralble class/object is evil
#   there should not be any "configurations" in OOP, ex. Spring XML configuration mechanisms
#   using object properties as configuration parameters is a very common mistake
#   this makes objects implicitly mutable: we configure them
#     we "change their behavior" by injecting parameters or an entire setting/configuration object into them
#   encapsulated properties must not be used to change the behavior of an object
#     an object's properties are its inherent characteristics (in order to represent a real-world entity)
#     an object's behavior should be immutable
#
# example:
#
# (bad design: procedural programming)
#
# // from simple to complex, adding configuration fields or one complex, configuration object
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
# 2) extend the functionality of the class: can decode by "UTF-8" or others
# 
#   // the class becomes a configurable class
#   class Page {
#
#       private final String uri;
#       private final String encoding;      // add a configurable field
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
#  
# 3) extend the functionality of the class: can handle an empty page
#
#   class Page {
#
#       private final String uri;
#       private final String encoding;      // a configurable field
#       private final boolean alwaysHtml;   // add another configurable field
#
#       Page(final String address, final String enc, final boolean always) {
#           this.uri = address;
#           this.encoding = enc;
#           this.alwaysHtml = always;
#       }
#
#       public String html() throws IOException {
#           String html = IOUtils.toString(new URL(this.uri).openStream(), this.encoding);
#           if (html.isEmpty() && this.alwaysHtml) { // the method can have different behaviors
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
#       private final boolean encodeAnyway; // add one more configurable field
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
#               html = new String(bytes, this.encoding); // try to encode the bytes based on this.encoding
#           } catch (UnsupportedEncodingException ex) {
#               if (!this.encodeAnyway) {                // if encodeAnyway is set, use default "UTF-8" encoding
#                   throw ex;
#               }
#               html = new String(bytes, "UTF-8");
#           }
#
#           if (html.isEmpty() && this.alwaysHtml) {     // if alwaysHtml is set, return "<html/>"
#               html = "<html/>";
#           }
#           return html;
#       }
#   }
#  
# 5) encapsulate the configuration fields in an object
#
#   class Page {
#
#       private final String uri;
#       private final PageSettings settings;             // encapsulate the setting in one object
#
#       Page(final String address, final PageSettings setting) {
#           this.uri = address;
#           this.settings = setting;
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
#  why is it bad?
#    the object is responsible for too many things, a big and non-cohesive object
#    the code becomes less testable, less maintainable and less readable
#    
#
#  (good design: distribute the responsibilities by using composable decorators)
#
#  // the client code
#  Page page = new NeverEmptyPage(new DefaultPage("http://www.google.com"))
#
#  String html = new AlwaysTextPage(new TextPage(page, "ISO_8859_1"), page).html();
#  
#
#  // the core class: responsible for one simple thing (a cohesive object)
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
#  // a decorator class: extend the functionality of the html() method 
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
#  // the client code
#  Page page = new NeverEmptyPage(new DefaultPage("http://www.google.com"));
#  
#  // a decorator class: has a single configuration field for encoding
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
#  // the client code
#  Page page = new TextPage(Page, "ISO_8859_1");
#
#  // a decorator class
#  class AlwaysTextPage {
#
#      private final TextPage origin;
#      private final Page source;
#
#      AlwaysTextPage(final TextPage origin, final Page source) {
#          this.origin = origin;                 // an encoded page (the encoding may be unknown)
#          this.source = source;                 // default original page
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
#  // the client code
#  Page page = new NeverEmptyPage(new DefaultPage("http://www.google.com"))
#  Page textpage = new AlwaysTextPage(new TextPage(page, "ISO_8859_1"), page)
#  
#  // one more decorator class to avoid duplicate HTTP request (optional)
#  class OncePage implements Page {
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
#  // the final client code: create a multi-decorated page and then get its html content
#  Page page = new NeverEmptyPage(
#      new OncePage(
#          new DefaultPage(
#              "http://www.google.com"
#          )
#      )
#  )
#  String html = new AlwaysTextPage(new TextPage(page, "ISO_8859_1"), page).html();
#  

