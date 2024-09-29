import time
""" a=5
b=6
print(a < b)
a=7
print(a > b)
a=9
print(a >= b) #Greater than OR equal to
print(a < b) """

# OR Truth Table -- or
# T OR T = T 
# T OR F = T
# F OR T = T
# F OR F = F

# AND Truth Table -- or
# T AND T = T 
# T AND F = F
# F AND T = F
# F AND F = F

# NOT Truth Table -- not
# NOT T = F
# NOT F = T

# print (a==6 and b==6)

#I want to print all the even numbers from 1-20
""" for i in range(1,21):
    if i%2!=0:
        print(i,end="",flush=True) """

# for i in range(1,21):
#     print(i,end="",flush=True)
#     print("\r",end="",flush=True)
#     time.sleep(1)
hour = 10
min = 58
sec = 50

while True:
    
    print(f"{hour:02d}:{min:02d}:{sec:02d}", end="", flush=True)
    print("\r", end="", flush=True)
    time.sleep(1)
    sec = sec + 1
    if sec == 59:
        sec = 0
        min = min + 1
    if min == 60:
        min = 0
        hour = hour + 1
    if hour == 24:
        hour = 0