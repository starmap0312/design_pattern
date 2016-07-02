# 1) bridge pattern
#
#   both interface and implementation are abstracted, so that they are decoupled and can be developed independently
#   
#   (conventional: interface and implementation are coupled)
#
#             interface
#              |     |(IS_A)
#         ------     ------
#         |               |
#    implementation  implementation
#
#   (bridge pattern: interface and implementation are decoupled by adding an abstraction layer to them)
#
#                          (HAS_A)
#   interface abstraction  ------>  implementation abstraction
#        |     |                              |     |
#     ---      ---(IS_A)                    ---     ---(IS_A)
#     |          |                          |         |
#  actual      actual                  actual         actual
# interface   interface                implementation implementation
#
#
