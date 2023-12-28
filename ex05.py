# First examples of Turtle (Python Logo) extensions
# Brygg Ullmer, Clemson University
# Begun 2022-08-01

# https://opensource.com/article/21/9/logo-python-turtle
# https://realpython.com/beginners-guide-python-turtle/
# https://pythonguides.com/python-turtle-draw-letters/
# https://docs.python.org/3/library/turtle.html

import enoTurtle as et #note that turtle.setup must occur first!

square = "f50 r90 "  * 4 # describe a square
star   = "f75 r144 " * 5 # describe a star

et.followPattern(square)          #draw a square
et.followPattern("l90 u f50 d")   #shift up

et.followPattern(star)            #draw a star
et.followPattern("r54 u f70 d")   #shift up

et.followPattern("P - r180 C u f130 l100 f130 d r205 V")
et.followPattern("u r90 f20 r90 f140 r220 d A")

et.speed(1000)
et.pensize(1)
et.color("purple")
for i in range(700):
  et.followPattern('f%i l91' % i)

et.exitonclick()

### end ###
