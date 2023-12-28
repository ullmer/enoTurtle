# Extended interaction support for Python LOGO turtle supports
# In time, hopefully allow physical robot, 3D graphics, and VR variations
# By Brygg Ullmer, Clemson University
# Begun 2022-08-01

import turtle
import traceback

turtle.title('Turtles in motion')
turtle.setup(width=800, height=800)

global t
t = turtle.Turtle()

turtle.bgcolor("black") #make the background color black
t.color("orange")  #make the "pen color" orange
t.pensize(10)      #choose a pen width of 10


# Create shortcuts for frequent commands (cmds)
cmds       = {'r': t.right, 'l': t.left, 'f': t.fd, 'b': t.bk, 'c': t.circle,
              'u': t.penup, 'd': t.pendown}

patterns   = {'-': 'u f110 d',        # scoot  forward a bit, no marks
              '*': 'f200 r144 ' * 5,  # repeat star-leg 5 times
              'P': 'r90 f130 b100 f50 l90 c40,180 r180',
              'C': 'c60,180', 'V': 'f130 r140 f130', 'A': 'f130 r140 f130'}

################# Follow Patterns #################

def followPattern(patTxt): #follow a command sequence defined by pattern text
  global cmds, pattern

  commands = patTxt.split() #break apart 'r90 f130' into ['r90', 'f130']
  for command in commands:
    try:
      cmdChar = command[0];
      if cmdChar in patterns:
        patTxt = patterns[cmdChar]
        followPattern(patTxt)
        continue

      args = []

      if len(command) > 1:
        argTxt1 = command[1:] # break text into two parts
        if argTxt1.find(','): argTxt2 = argTxt1.split(',') #handle commas
        else:                 argTxt2 = [argTxt1]

        for arg in argTxt2: args.append(int(arg)) # turn letters into numbers

      if cmdChar in cmds:
        cmd = cmds[cmdChar]

        #if len(args) == 0: print("Running", cmdChar); cmd()
        #if len(args) == 1: print("Running", cmdChar, args[0]); cmd(args[0])
        #if len(args) == 2: cmd(args[0], args[1])

        if len(args) == 0: cmd()
        if len(args) == 1: cmd(args[0])
        if len(args) == 2: cmd(args[0], args[1])

    except:
      print("Noting + ignoring enoTurtle followPattern bug processing", command)
      traceback.print_exc()

################# exit on click #################

def exitonclick():     turtle.exitonclick()
def color(whichColor): global t; t.color(whichColor)
def pensize(size):     global t; t.pensize(size)
def speed(howFast):    global t; t.speed(howFast)

### end ###
