'''
Password Generator | (special chars == 2) and (digits >= 3)

-------------------------------------------------------------
'''

import secrets
import string
A = int(input("How many characters do you want your password to have? "))

def create_pw(pw_length=A):
   letters = string.ascii_letters
   digits = string.digits
   special_chars = string.punctuation

   alphabet = letters + digits + special_chars
   pwd = ''
   pw_strong = False

   while not pw_strong:
       pwd = ''
       for i in range(pw_length):
           pwd += ''.join(secrets.choice(alphabet))

       if (sum(char in special_chars for char in pwd) == 2 and
               sum(char in digits for char in pwd) >= 3):
           pw_strong = True

   return pwd


if __name__ == '__main__':
   print(create_pw())