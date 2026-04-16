'''import turtle
turtle.speed(5)
turtle.forward(100)
turtle.left(90)
turtle.tracer(False)
turtle.circle(50)
turtle.tracer(True)
turtle.hideturtle()
turtle.done()'''

'''import turtle
turtle.circle(50)
turtle.circle(270)
turtle.done'''

'''def is_equilateral(a,b,c):
    if a==b and b==c and c==a:
        return "Yes"
    else:
        return "No"
print(is_equilateral(5,5,2))
print(is_equilateral(2,2,2))'''
#check if the number is positive

'''
#check if a number is odd or even
num = int(input("enter a number"))
if num % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")
# age checker
num = int(input("enter your age"))
if num >=18:
    print("you are old enough to vote")
else:
    print("you are not old enough to vote")

#password
password= int(input("enter password"))
if password ==1234:
    print ("Access Granted")
else:
    print("Access Denied")'''

#elif statement
'''num= int(input("enter a number"))
if num > 0:
    print("the number is positive")
elif num< 0:
    print("Negative")
else:
    print("zero")
#elsif statement 2
score= int(input("enter student marks"))
if  score >=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
else:
    print("FAIL!")
#elsif statement 3 
age =int(input("enter your age"))
if age>=18:
    print("adult")
elif age >15:
    print("teenager")
elif age<=13:
    print("child")'''
'''
#while statement
i =2
while i<=50:
    print(i)
    i+=2
'''
'''#assert() boolean expression to decide what should happen
#pytest
def test():
    assert "Green" == "Blue"'''
'''score= int(input("input your grade"))
 if '''

# homework
'''score= int(input("enter student marks"))
if  score >=94:
    print("A")
elif score>=90:
    print("A-")
elif score>=87:
    print("B+")
elif score>=86:
    print("B")
elif score>=80:
    print("B-")
elif score>=79:
    print("C+")
elif score>=74:
    print("C")
elif score>=70:
    print("C-")
elif score>=60:
    print("D")
elif score<59:
    print("FAIL")'''

'''times=0
while times<5:
    print("hi")
    times = times+1 
    print("bye")'''

''''a=int(input("enter first side"))
b=int(input("enter second side"))
c=int(input("enter third side"))
if a==b and b==c:
     print("equilateral triangle")
elif a==b and b==c:
     print("isosceles triangle")
else:
     print("scalene triangle")
if a>b and b>c:
     print("a is greatest")
elif b>a and b>b:
     print("A is greatest")
elif a==b and b==c:
     print("they are the same")
else:
     print("c is the greatest")'''
'''age = int (input("enter your age"))
if age<=2:
    print("infant")
elif age<=13:
    print("child")
elif age <= 20:
    print("teenager")
elif age <= 60:
    print("senior citizen")
else:
    print("adult")'''

'''score= float(input("enter student marks"))
if  score >=94:
    print("A")
elif score>=93.99:
    print("A-")
elif score>=87:
    print("B+")
elif score>=86:
    print("B")
elif score>=80:
    print("B-")
elif score>=79:
    print("C+")
elif score>=74:
    print("C")
elif score>=70:
    print("C-")
elif score>=60:
    print("D")
else:
    print("FAIL")'''



'''a =int(input("enter number"))
b = int(input("enter number"))
if a>b:
    print("a is greatest")
else:
    print("b is greatest")'''

'''i = 1
total =0
while i<=10:
    total+=1
    i+=1
print(total)'''



#coundown
'''ef countdown(number):
    total = 0
    i=1
    while i >= number:
        print("1")
        total +=1
        i +=1
    return total
def countup(number):
    total= 0 
    i = 1 
    while i <= number: 
        print(i)
        total +=1
        i+=1
    return total
def main():
    num = int(input("enter a number"))
    result = countup(num)
    print("the sum is:",result)
main()'''
#strings
#sequence of characters
'''def printspace():
    print("Hello\nWorld")
    print("name\tAge\tGrade")
    print("She said:\"python is fun\"")
printspace()'''

#positive indexing:Ethan= e=0 t=1 h=2 a=3 n=4
#negative indexing: ethan=e=-5 t=-4 h=-3 a=-2 n=-1
'''name = "ethan"
print(name)
print(len(name))
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

print(name[::-1])
print(name[])
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])'''
#control statement:break and continue: continue
'''count=0
while True:
    count = count+1
    if count % 5==0:
        continue
    elif count >=20:
        break
    print(count)
print("done")'''

#palindrome
'''word = input("Enter a word")
print(word)
print(word[::-1])
if word ==word[::-1]:
    print("palindrome")
else:
    print("not a palindrome")'''
'''def hello_you(name='ethan'):
    print('hello', name)
hello_you('ethan')
hello_you()'''
#string:sequence of character and range is sequence of integer
'''range(10)'''

#0,10 star 0 stop 11 step 

'''for i in range(1,10,-1):
    print(i);'''
'''text= "i need a break"
tokens=text.split()
print(tokens)'''

'''word="mango"
for x in word:
    print(x)'''

'''for i in range(1,6):
    print("*"* i)
    print("*"*i)'''


#file method
'''my_file=open("file.txt")
for line in my_file:
    length= len(line)
    print(length)'
    ''file =open("file.txt")
for i in file:
    print(len(i))'''
import csv
with open("students.csv") as file:
    next(file)
    for line in file:
       name,m1,m2,m3,= line.strip().split(",")
       avg=(int(m1)+int(m2)+int(m3))/3
       print(name,"average:", avg)





