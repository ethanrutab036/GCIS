'''def name():
    name = input("enter your name")
    print(name)
name()'''
'''
def main():
    print("practice")
main()'''

'''def parameters():
    x = int(input("x:"))
    y = int(input("y:"))
    return x*y
print(parameters())'''
'''
def circle(radius):
    return 4.13 * radius **2
def main():
    radius = circle(4)
    print(radius)
main()'''

'''loop'''
'''for number in range(1,4):
    print("atttempt",number, number*".")'''
'''
successful = True
for number in range(1):
    print("attempt")
    if successful:
        print("succesful")
        break
    else:
        print("failed attempt")'''

'''for x in range(5):
    for y in range (3):
        print(f"({x},{y})")'''

'''home: x coordinate
    home y coordidinate
    set heading:rotate turtle to a diffeent angle 90:north 230 south
    10 is radius turtle draws a circle'''
'''import turtle
def octagon():
    turtle.forward(100)
    turtle.left(45)

    turtle.forward(100)
    turtle.left(45)

    turtle.forward(100)
    turtle.left(45)

    turtle.forward(100)
    turtle.left(45)
   
    turtle.forward(100)
    turtle.left(45)

    turtle.forward(100)
    turtle.left(45)

    turtle.forward(100)
    turtle.left(45)

    turtle.forward(100)
    turtle.left(45)

octagon()
turtle.done()'''
'''import turtle
def triangle():
    turtle.forward(90)
    turtle.left(30)

    turtle.forward(90)
    turtle.left(30)

    turtle.forward(90)
    turtle.left(30)

    turtle.forward(90)
    turtle.left(90)

    turtle.pensize()
turtle.pencolor()
turtle.fill()
triangle()
turtle.done()'''

'''import turtle
def square():
    turtle.forward(100)
    turtle.left(90)
    
    turtle.forward(100)
    turtle.left(90)

    turtle.forward(100)
    turtle.left(90)

    turtle.forward(100)
    turtle.left(90)

    turtle.forward(100)
    turtle.left(100)
    
    turtle.forward(200)
    turtle.left(100)

    turtle.forward(200)
    turtle.left(100)

    turtle.forward(200)
    turtle.left(100)
square()
turtle.done()'''
'''import turtle
turtle.pensize(4)
turtle.pencolor("blue")
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.done()'''

'''import turtle

turtle.pencolor("orange")

def centered_circle(x,y,r,color,angle=360):
    turtle.setheading(0)
    turtle.penup()
    turtle.goto(x,y)
    turtle.forward(r)
    turtle.left(90)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r,angle)
    turtle.end_fill()
    turtle.penup()

def smile(x,y,r,color,angle):
    turtle.setheading(0)
    turtle.penup()
    turtle.goto(x,y)
    turtle.forward(r)
    turtle.left(90)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r,angle)
    turtle.end_fill()
    turtle.penup()

def face_nose(x,y,r,face_color):
    centered_circle(x,y,r,face_color)
    centered_circle(x,y,r/10,"pink")

def draw_eye(x,y,r,color):
    centered_circle(x,y,r,"white")
    centered_circle(x,y,(r*2)/3,color)
    centered_circle(x,y,r/3,"black")

x=20
y=20
r=100
    
face_nose(20,20,100,"yellow")

draw_eye(x+r*6/20,y+r*5/20,r*5/20,"brown")
draw_eye(x-r*6/20,y+r*5/20,r*5/20,"brown")

smile(x,y-r*4/20,r*6/20,"red",-180)'''
    



'''def square():
    turtle.pencolor("green")

    turtle.fillcolor()

    turtle.begin_fill()
    turtle.forward(100)
    turtle.left(90)
    
    turtle.forward(100)
    turtle.left(90)

    turtle.forward(100)
    turtle.left(90)

    turtle.forward(100)
    turtle.left(90)

    turtle.forward(100)
    turtle.left(90)
    
    turtle.forward(150)
    turtle.left(90)

    turtle.forward(150)
    turtle.left(90)

    turtle.forward(150)
    turtle.left(90)

    turtle.forward(150)
    turtle.left(90)

    turtle.forward(200)
    turtle.left(90)

    turtle.forward(200)
    turtle.left(90)

    turtle.forward(200)
    turtle.left(90)

    turtle.forward(200)
    turtle.left(90)
    turtle.end_fill()
square()
turtle.done()'''


'''points=float(input("enter points scored per game"))
rebounds=int(input("enter rebounds"))
if points>=10 and rebounds>=10:
    print(" all star")
else:
    print("not an all star")'''
'''temp=int(input("input temp"))
if temp>30:
    print("warm")
elif temp<=20:
    print("cold")
else:
    print("n.a")
print("done")'''

'''age = 12
if age >= 22:
    message="eligible"
else:
    message="not eligible"
message = "eligible" if age >=18 else "not eligible"
print(message)'''
'''
high_income=int(input("enter income"))
good_credit= int(input("enter credit score"))

if high_income>=20000 and good_credit<=420:
    print("eligible")
else: 
    print("you are not eligible for this loan")'''
i =0
while i<5:
    print(i)
i=i-1







