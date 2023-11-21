import turtle 

  
print('Sorry but I dont know how to remove the button after clicking it.')

wording = turtle.Turtle()
wording.speed(0)
wording.color('black')
wording.penup()
wording.goto(-60,200)
wording.pendown()
wording.write('Drawing Game', font=('Cursive', 20, 'bold'))

pen = turtle.Turtle()
pen.hideturtle()

for i in range(2):
  pen.forward(80)
  pen.left(90)
  pen.forward(30)
  pen.left(90)

pen.penup()
pen.goto(0,6)
pen.write('Start Game', font=('Courier', 10, 'normal'))

def buttonClick(x,y):
  if x > 0 and x < 81 and y> 0 and y<30:
    turtle.setposition(0,0)
    turtle.pencolor('white')
    turtle.Screen().bgcolor('black')

def Forward():

  turtle.pensize(5)
  turtle.fd(20)

def Backward():
  turtle.pensize(5)
  turtle.bk(20)

def Right():
  turtle.rt(90)

def Left():
  turtle.lt(90)

def LilLeft():
  turtle.lt(30)

def LilRight():
  turtle.rt(30)

def bg1():
  turtle.Screen().bgcolor('red')

def bg2():
  turtle.Screen().bgcolor('orange')

def bg3():
  turtle.Screen().bgcolor('yellow')

def bg4():
  turtle.Screen().bgcolor('green')

def bg5():
  turtle.Screen().bgcolor('blue')

def bg6():
  turtle.Screen().bgcolor('purple')

def bg7():
  turtle.Screen().bgcolor('black')

def bg8():
  turtle.Screen().bgcolor('brown')

def bg9():
  turtle.Screen().bgcolor('gold')

def bg0():
  turtle.Screen().bgcolor('white')

def no():
  turtle.penup()

def yes():
  turtle.pendown()

def ink1():
  turtle.pencolor('red')

def ink2():
  turtle.pencolor('orange')

def ink3():
  turtle.pencolor('yellow')

def ink4():
  turtle.pencolor('green')

def ink5():
  turtle.pencolor('blue')

def ink6():
  turtle.pencolor('purple')

def ink7():
  turtle.pencolor('black')

def ink8():
  turtle.pencolor('brown')

def ink9():
  turtle.pencolor('gold')

def ink0():
  turtle.pencolor('white')

turtle.listen()
turtle.onkeypress(Forward, 'w')
turtle.onkeypress(Backward, 's')
turtle.onkeypress(Right, 'd')
turtle.onkeypress(Left, 'a')
turtle.onkeypress(LilLeft, 'q')
turtle.onkeypress(LilRight, 'e')
turtle.onkeypress(bg1, '1')
turtle.onkeypress(bg2, '2')
turtle.onkeypress(bg3, '3')
turtle.onkeypress(bg4, '4')
turtle.onkeypress(bg5, '5')
turtle.onkeypress(bg6, '6')
turtle.onkeypress(bg7, '7')
turtle.onkeypress(bg8, '8')
turtle.onkeypress(bg9, '9')
turtle.onkeypress(bg0, '0')
turtle.onkeypress(no, 'n')
turtle.onkeypress(yes, 'y')
turtle.onkeypress(ink1, 'f')
turtle.onkeypress(ink2, 'g')
turtle.onkeypress(ink3, 'h')
turtle.onkeypress(ink4, 'j')
turtle.onkeypress(ink5, 'k')
turtle.onkeypress(ink6, 'l')
turtle.onkeypress(ink7, 'z')
turtle.onkeypress(ink8, 'x')
turtle.onkeypress(ink9, 'c')
turtle.onkeypress(ink0, 'space')
turtle.onscreenclick(buttonClick, 1)
turtle.listen()

turtle.done()
