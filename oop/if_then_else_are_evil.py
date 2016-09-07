# in most cases, if-then-else must be replaced by a decorator or simply another object
#
# example: 
#
#  (bad design)
#
#  // both the validation & modify functionality are defined in the DyTalk class
#  class DyTalk implements Talk {
#
#      void modify(Collection<Directive> dirs) {
#          if (!dirs.isEmpty()) {
#              // apply the modification and save the new XML document to the DynamoDB table
#          }
#      }
#
#  }
#  
#  // extract the validation to an decorator and delegate the modify functionality to the decoratee
#
#  class QuickTalk implements Talk {
#
#      private final Talk origin;
#
#      void modify(Collection<Directive> dirs) {
#          if (!dirs.isEmpty()) {
#              this.origin.modify(dirs);
#          }
#      }
#  }

