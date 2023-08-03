import turtle
new_screen = turtle.Screen()
new_screen.bgcolor("lightgrey")
print("Welcome to Scotty's shape drawer")

def determine_draw():  # create a function
    print("What would you like to draw? R = Rectangle, T = triangle, S = Square, C = Circle")  # ask user what they would like to draw
    what_to_draw = input()  # put the input into a variable what_to_draw
    if what_to_draw == 'T' or what_to_draw == 't':
        draw_tri = turtle.Turtle()  # create a turtle instance
        draw_tri.color("orange")
        cotriangle = int(input("Enter a number for the sides :"))
        ''' used int to change the input to a number because the input defaults into a string '''
        for _ in range(3):  # this for loop will loop 3 times only by  using the range option
            draw_tri.forward(cotriangle)  # this will draw the length of the lines with the input above
            draw_tri.right(120) # turn the pen 120 degrees

        print("Click the screen to exit") # tells the user to click the drawing screen to close
        new_screen.exitonclick() # sets the screen to close once clicked
    elif what_to_draw == 'R' or what_to_draw == 'r':
        draw_rec = turtle.Turtle()
        ''' draw_rec.shape("rectangle") '''
        draw_rec.color("green")
        corectangle_l = int(input("Enter the length please :"))
        corectangle_w = int(input("Enter a width please :"))

        draw_rec.forward(corectangle_l)
        draw_rec.right(90)
        draw_rec.forward(corectangle_w)
        draw_rec.right(90)
        draw_rec.forward(corectangle_l)
        draw_rec.right(90)
        draw_rec.forward(corectangle_w)
        draw_rec.right(90)
        print("Click the screen to exit")
        new_screen.exitonclick()
    elif what_to_draw == 'S' or what_to_draw == 's':
        '''  '''
        cosquare_r = int(input("Please enter a value for the sides of the Square :"))

        draw_square = turtle.Turtle()
        draw_square.shape("square")
        draw_square.color("blue")
        for _ in range(4):
            draw_square.forward(cosquare_r)
            draw_square.right(90)
        print("Click the screen to exit")
        new_screen.exitonclick()
    elif what_to_draw == 'C' or what_to_draw == 'c':
        cocircle = int(input("Please enter a value for the size of the circle : "))
        draw_circle = turtle.Turtle()
        draw_circle.color("green")
        draw_circle.circle(cocircle)
        print("Click the screen to exit")
        new_screen.exitonclick()
    else:  # if the input is not C, T , R , S than tell the user that they did not enter a correct value
        print("Sorry you did not enter a valid answer - Pleae try again")
        determine_draw() # call the function again looking for a correct value this will keep hapenning until a valid value is entered

determine_draw()
''' call the function for the first time, the reason you call the function here and not at the top of this
program is because the function has to be created first '''