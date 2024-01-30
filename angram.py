str1=input("give str1: ")
str2=input("give str2: ")
if(len(str1)==len(str2)):
    sorted_str1=sorted(str1)
    sorted_str2=sorted(str2)

    if(sorted_str1==sorted_str2):
        print(str1 + " and "+ str2 +" is valid angram")
    else:
        print("not a angram")
