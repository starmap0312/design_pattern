# to design robust software, make it fragile
#
# example
#
# (bad design: a fail-safe method)
#
#   public int size(File file) {
#       if (!file.exists()) {    // the program won't fail if the file does not exist
#           return 0;            // the error is hidden
#       }
#       return file.length();
#   }
#
# (good design: a fail-fast method)
#
#   public int size(File file) {
#       if (!file.exists()) {   // throw an exception whenever an error happens
#           throw new IllegalArgumentException("There is no such file; I can't get its length.");
#       }
#       return file.length();
#   }
