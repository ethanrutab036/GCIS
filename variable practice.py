def variable_practice():
     age= 228
     days= 365
     name= "ethan"
     pi = 3.1415926
     pet = 'daboos'

     print("age is:" ,age)
     print("days are:",days)
     print("name is:",name)
     print('pi:',pi)
     print('pet name is:',pet)
variable_practice()
def prompt_and_print():
    
     variable_practice()

'''x=5
y=2
z=10
print(x**y)
print(x+z*y)'''
a=int(input("enter first side"))
b=int(input("enter second side"))
c=int(input("enter third side"))
if a==b and b==c:
     print("equilateral triangle")
elif a==b and b==c:
     print("isosceles triangle")
else:
     print("scalene triangle")
