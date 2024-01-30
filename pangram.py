import string
def ispangram(str):
    alphabet="abcdefghijklmnopqrstuvwxyz"

    for char in alphabet:
        if char not in str.lower():
            return False
        
        return True
    

#driver code

string="qwertyuiopasdfghjklzxcvbnm"

if(ispangram(string)==True):
    print("valid pangram")

else:
    print("not pangram")

