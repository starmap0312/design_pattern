# Prompt the user for a value, usually a password, without echoing what they type to the console

import getpass

p = getpass.getpass(prompt='Enter your password: ')
print(p)
