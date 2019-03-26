#second_class
#1
x = 2
y = 3
if x > y:
    print("big")
else:
    print("small")
#2
for x in range(5):
    print(x)
#3
season = 2
if season == 1:
    print("summer vacation")
elif season == 2:
    print("winter is comming")
elif season == 3:
    print("fall")
elif season == 4:
    print("spring break")

#4
count = 1
while count<11:
    print(count)
    count = count+1

#5
age = 18
letter = "s"
currency = 3.76
flew = True
apartment_num = 3

print(age)
print(letter)
print(currency)
print(flew)
print(apartment_num)
print(currency+age)

#6
number = input("phone number is: ")
print("Phone number is: ", number)

#7
def printhello():
    print("hello:")
printhello()
def calculate():
    print(5+3.2)
calculate()
#8
def print_name():
    return "shaked"
print(print_name())

def divide_number(number):
    print(number/2)
divide_number(10)

#9
def return_sum(x,y):
    return x+y
return_sum(1,1)

#chalenge
rows = input("nummbers of row to print: ")
rows = int (rows)
for i in range (0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

#chalenge2
N = 7

for i in range(N):
    for j in range(N):
        if (i == j) or ((N - j -1) == i):
            print('*', end = '')
        else:
            print(' ', end = '')
    print('')