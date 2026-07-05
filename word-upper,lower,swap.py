c=input("Enter a word: ")
upper=""
lower=""
swap=""
for i in c:
    ascii_val=ord(i)
    if 97<=ascii_val<=122:
        upper+=chr(ascii_val-32)
        lower+=i
        swap+=chr(ascii_val-32)
    elif 65<=ascii_val<=90:
        upper+=i
        lower+=chr(ascii_val+32)
        swap+=chr(ascii_val+32)
    else:
        upper+=i
        lower+=i
        swap+=i

print("Original: ",c)
print("Upper: ",upper)
print("Lower: ",lower)
print("Swap: ",swap)
        
