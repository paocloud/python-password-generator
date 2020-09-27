'''
Password Genertor Tool.
COPYRIGHT 2020 , PAOCLOUD CO., LTD.
'''

import string
from random import *

characters = string.ascii_letters + string.punctuation  + string.digits

def calPass():
    return "".join(choice(characters) for x in range(randint(8, 16)))

for i in range(5):
 print (calPass())
