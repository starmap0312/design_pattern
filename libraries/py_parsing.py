from pyparsing import Word, Suppress, alphas, nums, alphanums

# example 1:
pattern = Word(alphas) + "," + Word(alphas) + "!" # a tokenized pattern
parsed = pattern.parseString("Hello,     World!") # spaces between tokens are skipped by default
print(parsed)                                     # ['Hello', ',', 'World', '!'] 
parsed = pattern.parseString("Hello,John!")
print(parsed)                                     # ['Hello', ',', 'John', '!']

# example 2:
pattern = Word(alphas, max=1) + "=" + Word(nums) + Word("+-*/", max=1) + Word(nums)
parsed = pattern.parseString("x=2+2")
print(parsed)                                     # ['x', '=', '2', '+', '2']
parsed = pattern.parseString("r= 1234/ 100000")
print(parsed)                                     # ['r', '=', '1234', '/', '100000']

# example 3:
pattern = Suppress('<') + Word(alphanums + '_-') + Suppress('>') # Suppress: clears matched tokens
parsed = pattern.parseString("<my_var>")
print(parsed)                                     # ['my_var']

