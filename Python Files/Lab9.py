import turtle
__author__='Joshua Pollock'


def read_coords(file):
    '''
    Opens the inputted file, reads the lines, and creates empty dictonaries.
    After that the function will set specific pieces equal to the Henry Draper
    number of that star.
    '''
    file=open(file, 'r')
    star_data=file.readlines()
    file.close()
    # Creates a variable of the lines of data from the file
    coordinates={}
    magnitudes={}
    star_names={}
    # Creates 3 empty dictionaries for future use
    for i in star_data:
        i=i.split(' ')
        # Splits along the spaces in the data
        coordinates[i[3]]=(float(i[0]), float(i[1]))
        # Sets the coordinates of the given Henry Draper number
        # to a tuple of x and y coordinates
        magnitudes[i[3]]=float(i[4])
        # Sets the magnitude of the given Henry Draper numberArray
        # to a tuple of a specific position
        if len(i) > 6:
            star_names[i[3]]=i[6:]
            # Checks to see if the star has a name
    return (coordinates, magnitudes, star_names)


def plot_plain_stars(picture_size, coordinates_dict):
    '''
    Function for drawing a picture based off the given coordinates from
    the read_coords function.
    '''
    turtle.bgcolor('black')
    turtle.color('white')
    turtle.hideturtle()
    turtle.speed(100)
    turtle.delay(0)
    turtle.tracer(0, 0)
    turtle.update()
    turtle.screensize(picture_size, picture_size)
    # Set up for the turtle commands
    for i in coordinates_dict:
        turtle.penup()
        # Picks up pen so the dots are not connected
        turtle.setx(coordinates_dict[i][0] * (picture_size / 2))
        turtle.sety(coordinates_dict[i][1] * (picture_size / 2))
        # Sets the coordinates base off the given size
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(2)
        turtle.left(90)
        turtle.forward(2)
        turtle.left(90)
        turtle.forward(2)
        turtle.end_fill()
        # turtle commands to draw a filled in rectangle


def plot_by_magnitude(picture_size, coordinates_dict, magnitudes_dict):
    '''
    Function for drawing a picture based off the given coordinates from
    the read_coords function.  Uses a specific equation to find magnitude
    and the size of a star.
    '''
    turtle.bgcolor('black')
    turtle.color('white')
    turtle.hideturtle()
    turtle.speed(100)
    turtle.delay(0)
    turtle.tracer(0, 0)
    turtle.update()
    turtle.screensize(picture_size, picture_size)
    # Set up for the turtle commands
    for i in magnitudes_dict:
        star_size=round((10 / ((magnitudes_dict[i]) + 2)))
        # Sets the star size to the specific magnitude using
        # a given equation
        if star_size > 8:
            star_size=8
            # Prevents the star size from being greater than 8
            # This is a constraint of the lab
        turtle.penup()
        # Picks up the pen
        turtle.setx(coordinates_dict[i][0] * (picture_size / 2))
        turtle.sety(coordinates_dict[i][1] * (picture_size / 2))
        # Sets the x and y coordinates base off of picture size
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(star_size)
        turtle.left(90)
        turtle.forward(star_size)
        turtle.left(90)
        turtle.forward(star_size)
        turtle.end_fill()
        # Turtle drawing commands, this time using
        # the magnitude of the star for size.

star_data=read_coords('stars.txt')
# plot_plain_stars(500,star_data[0])
plot_by_magnitude(500, star_data[0], star_data[1])
