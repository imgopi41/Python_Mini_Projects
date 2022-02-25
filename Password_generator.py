import string   #importing Library string
import random   #importing Library random 

a1 = string.ascii_lowercase #initializing lowercase strings to 'a1'.
a2 = string.ascii_uppercase #initializing uppercase strings to 'a2'.
a3 = string.digits  #initializing digits to 'a3'.
a4 = string.punctuation #initializing special characters in 'a4'.
a5 = string.octdigits   #initializing oct digits in 'a5'.
a6 = string.hexdigits   #initializing hex digits in 'a6'.

string_length = int(input("Enter your Password length: "))  #Asking user to enter the password length.
a = []  #extending all the values in a = []
a.extend(a1)   
a.extend(a2)            
a.extend(a3)    #Extending all initialized values
a.extend(a4)
a.extend(a5)
a.extend(a6)
print("This is your Password: ")    #user message
# print("".join(random.sample(a,string_length)))    #random.sample and .shuffle() are used to mix all items
random.shuffle(a)   #shuffling all the extended items with library random.
print("".join(a[0:string_length]))  #joining items from 0 to user required length.
