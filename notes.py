def parameters(a,b,c,d):
    x=a+b

    print(x)
    print(c,d)
parameters("a","b","c","d")
parameters(4,3,2,1)

GLOBAL_1 = "Hello"
GLOBAL_2 = "Goodbye"

def function_1(parameter_1, paramenter_2):
    print(parameter_1)

    local_1 = "test"

    parameter_1 = 123
    print(parameter_1,paramenter_2,local_1)
function_1(GLOBAL_1,GLOBAL_2)
def square_are(length):
    return length * length
def main():
    area = square_are(4)
    print(area)
def triangle(base, height):
    return 0.5 * base * height



    

def circle_area(r):
    return 3.14 * r **2
def main():
    x = circle_area(12)
    print(x)

main()
def square(length,width):
    return length * width
def main():
    area= square(3*4)

#1. quadrant function: takes 2 parameters, x and y and accordingly returns the location as a String datatype.
def quadrant_function1(x,y):
    if x==0 and y==0:
        return "the point is at the origin"

    #checking x and y axis
    if x ==0:
        return "the point lies on the y axis"
    if y == 0: 
        print("")
    
    #quadrants
    if x >0 and y >0:
        quadrant="quadrant I"
    elif x<0 and y > 0:
        quadrant = "quadrant II"
    elif x< 0 and y< 0:
        quadrant = "quadrant III"
    else:
        quadrant = "quadrant IV"

    return quadrant
