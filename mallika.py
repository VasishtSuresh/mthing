import turtle
from pygame import mixer
import sys, subprocess

subprocess.run('clear', shell = True)

mixer.init()
mixer.music.load('temp.mp3')
val = input("Are you going to destroy your finals??: ")

if(val == "no" or val == "No" or val == "NO"):
	print("BRUH")
	while(val == "no" or val == "No" or val == "NO"):
		val = input("I SAID ARE YOU GONNA DESTROY YOUR FINALS!!!: ")

print("LETS GOOOOOOOOOOOOOOOOOOOOOOOO")

win = turtle.Screen()

mixer.music.play()
win.setup(width = 1200, height = 676)
win.bgpic('temp.gif')
#turtle.setposition(600, 150)
turtle.write("You are gonna destroy your finals", font=("Comic Sans",
                                    40, "normal"))

win.addshape('temp3.gif')
cappy = turtle.Turtle()
cappy.shape('temp3.gif')
cappy.right(90)
cappy.forward(200)
cappy.left(90)
i = 0
while(i < 1000):
	cappy.forward(200)
	cappy.backward(200)
	i +=1
turtle.done()

