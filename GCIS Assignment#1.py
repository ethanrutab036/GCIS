#1. quadrant function: takes 2 parameters, x and y and accordingly returns the location as a String datatype.
def quadrant_function1(x,y):
    x = int(input("input x"))
    y = int(input("input y"))

    if x == 0 and y == 0:
        return "the point is at the origin"

    if x == 0:
        return "the point lies on the y axis"
    if y == 0: 
        return "the point lies on the x axis"
    
    #quadrants
    if x > 0 and y > 0:
        return "quadrant I"
    elif x < 0 and y > 0:
        return "quadrant II"
    elif x < 0 and y < 0:
        return "quadrant III"
    else:
        return "quadrant IV"


#function call
print(quadrant_function1(0, 0))


#proximity
x = int(input("enter points for x"))
y = int(input("enter points for y"))



    



