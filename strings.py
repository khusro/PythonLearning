
s = 'hello'
#print(s.capitalize())
#print(s)
#print(s[4])
#s[4]='a'

#print(s[0:3])
#print(s[1:4])
#print(s[2:5])


s = 'world'
print(len(s))
y = "SyedKhusro"
print(len(y))

def printSlices(str, sliceSize):
    i = 0
    for i in range(len(str)-sliceSize+1):
        print(str[i:i+sliceSize])
    if(sliceSize > len(str)):
        print("Your Slice size is larger than your given string length")

printSlices(s,4)

def is_palindrome(n):
    return str(n) == str(n)[::-1]