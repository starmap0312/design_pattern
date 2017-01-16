# write a function that accepts arbitrary number of arguments

def func(*args):
  print("arguments: {}".format(args))

func("Hello,", 123, " is one, two, three.")

