
char=input("Input character: ")

if  char>="0" and   char<="9":          #alternative char.isnumeric():
    print("Digit")
elif  char>="A" and char<="Z":          #alternative char.isupper():
    print("Uppercase")
elif char>="a" and char<="z":          #char.islower():
    print("Lowercase")
else:
    print("Symbol")
