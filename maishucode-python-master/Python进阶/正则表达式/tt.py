import turtle as t

game = t.Screen()
game.bgcolor('black')
game.setup(600, 600)

pen = t.Turtle()
pen.ht()
pen.speed(0)
pen.down()
pen.color('green')
pen.pensize(3)
pen.circle(210)

game.mainloop()