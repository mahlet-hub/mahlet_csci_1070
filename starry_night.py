from cs1graphics import *

paper = Canvas(1200, 800)

paper.setTitle('starry night')
paper.setBackgroundColor('darkblue')

moon = Circle(100,Point(200,100))
moon.setFillColor('gray')
moon.setBorderWidth(0)
paper.add(moon)

crescent1 = Circle(25,Point(225,50))
crescent1.setFillColor('darkgray')
crescent1.setBorderWidth(0)
paper.add(crescent1)

crescent2 = Circle(12,Point(250,150))
crescent2.setFillColor('darkgray')
crescent2.setBorderWidth(0)
paper.add(crescent2)

crescent3 = Circle(17,Point(150,150))
crescent3.setFillColor('darkgray')
crescent3.setBorderWidth(0)
paper.add(crescent3)

crescent4 = Circle(17,Point(275,100))
crescent4.setFillColor('darkgray')
crescent4.setBorderWidth(0)
paper.add(crescent4)

star = Circle(3,Point(400,100))
star.setFillColor('white')
star.setBorderWidth(0)
paper.add(star)

star1 = Circle(3,Point(500,300))
star1.setFillColor('white')
star1.setBorderWidth(0)
paper.add(star1)

star2 = Circle(3,Point(100,300))
star2.setFillColor('white')
star2.setBorderWidth(0)
paper.add(star2)

star3 = Circle(3,Point(700,200))
star3.setFillColor('white')
star3.setBorderWidth(0)
paper.add(star3)

star4 = Circle(3,Point(200,500))
star4.setFillColor('white')
star4.setBorderWidth(0)
paper.add(star4)


star5 = Circle(3,Point(900,100))
star5.setFillColor('white')
star5.setBorderWidth(0)
paper.add(star5)

star6 = Circle(3,Point(300,300))
star6.setFillColor('white')
star6.setBorderWidth(0)
paper.add(star6)
               
ice = Rectangle(1200,400,Point(600,800))
ice.setFillColor('white')
ice.setBorderWidth(0)
paper.add(ice)


tree_trunk = Rectangle(200,300)
tree_trunk.setFillColor('brown')
tree_trunk.setBorderWidth(0)
tree_trunk.move(1000,550)   
paper.add(tree_trunk)

leaf1 = Polygon(Point(1000, 300), 
	   Point(850, 500), 
	   Point(1150,500))
leaf1.setFillColor('darkgreen')
leaf1.setBorderWidth(0) 
paper.add(leaf1)

leaf2 = Polygon(Point(1000,200),
	    Point(800, 450),
	    Point(1200, 450))
leaf2.setFillColor('darkgreen') 
leaf2.setBorderWidth(0) 
paper.add(leaf2)

leaf3 = Polygon(Point(1000, 100),
                Point(800, 300),
                Point(1200, 300))
leaf3.setFillColor('darkgreen')
leaf3.setBorderWidth(0)
paper.add(leaf3)

leaf4 = Polygon(Point(1000, 200), 
	    Point(825, 350), 
	    Point(1175, 350))
leaf4.setFillColor('darkgreen')
leaf4.setBorderWidth(0)
paper.add(leaf4)

leaf5 = Polygon(Point(1000,380),
                    Point(800,600),
                    Point(1200,600))
leaf5.setFillColor('darkgreen')
leaf5.setBorderWidth(0)
paper.add(leaf5)

carbody = Rectangle(300,200,Point(150,600))
carbody.setFillColor('skyblue')
carbody.setBorderWidth(0)
paper.add(carbody)


carpart = Rectangle(100,100,Point(350,650))
carpart.setFillColor('skyblue')
carpart.setBorderWidth(0)
paper.add(carpart)

window1 = Rectangle(100,75,Point(200,550))
window1.setFillColor('darkblue')
window1.setBorderWidth(1)
paper.add(window1)

window2 = Rectangle(100,75,Point(75,550))
window2.setFillColor('darkblue')
window2.setBorderWidth(1)
paper.add(window2)

tire1 = Circle(50,Point(300,700))
tire1.setFillColor('black')
paper.add(tire1)
                    
tire2 = Circle(50,Point(0,700))
tire2.setFillColor('black')
paper.add(tire2)

rim1 = Circle(25,Point(300,700))
rim1.setFillColor('gray')
paper.add(rim1)

rim2 = Circle(25,Point(0,700))
rim2.setFillColor('gray')
paper.add(rim2)
                                 


penguin = Layer()




body = Ellipse(200, 350, Point(600, 600))
body.setFillColor('black')
penguin.add(body)


belly = Ellipse(160, 280, Point(600, 570))
belly.setFillColor('white')
belly.setBorderWidth(0)  
penguin.add(belly)
          

head = Circle(80, Point(600, 450))
head.setFillColor('black')
penguin.add(head)


left_eye = Circle(15, Point(580, 440))
left_eye.setFillColor('white')
penguin.add(left_eye)

right_eye = Circle(15, Point(620, 440))
right_eye.setFillColor('white')
penguin.add(right_eye)


left_pupil = Circle(5, Point(580, 440))
left_pupil.setFillColor('black')
penguin.add(left_pupil)

right_pupil = Circle(5, Point(620, 440))
right_pupil.setFillColor('black')
penguin.add(right_pupil)


beak = Rectangle(30, 15, Point(600, 470))
beak.setFillColor('orange')
beak.setBorderWidth(0)
penguin.add(beak)


left_wing = Ellipse(100, 30, Point(520, 600))
left_wing.setFillColor('black')
left_wing.rotate(-75)  
penguin.add(left_wing)

right_wing = Ellipse(100, 30, Point(680, 600))
right_wing.setFillColor('black')
right_wing.rotate(75)  
penguin.add(right_wing)

left_foot = Rectangle(40, 20, Point(570, 750))
left_foot.setFillColor('orange')
left_foot.setBorderWidth(0)
penguin.add(left_foot)

right_foot = Rectangle(40, 20, Point(630, 750))
right_foot.setFillColor('orange')
right_foot.setBorderWidth(0)
penguin.add(right_foot)

paper.add(penguin)

import time
from time import sleep

for _ in range(60):  
    penguin.move(10, 0)  
    paper.refresh() 
    time.sleep(0.05)

text = Text('hey anna do you want to watch the stars with me ?', 30, Point(900, 350))

text.setFontColor('white')
text.setFontSize(20)

paper.add(text)

import time

time.sleep(2)

paper.remove(text)

text2 = Text('yeah ofc I will travis', 30, Point(900, 250))

text2.setFontColor('white')
text2.setFontSize(20)

paper.add(text2)

import time

time.sleep(2)

paper.remove(text2)

penguin2 = Layer()

body = Ellipse(200, 350, Point(1300, 600))
body.setFillColor('black')
penguin2.add(body)

belly = Ellipse(160, 280, Point(1300, 570))
belly.setFillColor('white')
belly.setBorderWidth(0)
penguin2.add(belly)

head = Circle(80, Point(1300, 450))
head.setFillColor('black')
penguin2.add(head)

left_eye = Circle(15, Point(1280, 440))
left_eye.setFillColor('white')
penguin2.add(left_eye)

right_eye = Circle(15, Point(1320, 440))
right_eye.setFillColor('white')
penguin2.add(right_eye)

left_pupil = Circle(5, Point(1280, 440))
left_pupil.setFillColor('black')
penguin2.add(left_pupil)

right_pupil = Circle(5, Point(1320, 440))
right_pupil.setFillColor('black')
penguin2.add(right_pupil)

beak = Rectangle(30, 15, Point(1300, 470))
beak.setFillColor('orange')
beak.setBorderWidth(0)
penguin2.add(beak)

left_wing = Ellipse(100, 30, Point(1220, 600))
left_wing.setFillColor('black')
left_wing.rotate(-75)
penguin2.add(left_wing)

right_wing = Ellipse(100, 30, Point(1380, 600))
right_wing.setFillColor('black')
right_wing.rotate(75)
penguin2.add(right_wing)

left_foot = Rectangle(40, 20, Point(1270, 750))
left_foot.setFillColor('orange')
left_foot.setBorderWidth(0)
penguin2.add(left_foot)

right_foot = Rectangle(40, 20, Point(1330, 750))
right_foot.setFillColor('orange')
right_foot.setBorderWidth(0)
penguin2.add(right_foot)

bow1 = Circle(10, Point(1300, 375))
bow1.setFillColor('pink')
bow1.setBorderWidth(0)
penguin2.add(bow1)

bow2 = Polygon(Point(1300, 375), Point(1250, 350), Point(1250, 400))
bow2.setFillColor('pink')
bow2.setBorderWidth(0)
bow2.rotate(-15)
penguin2.add(bow2)

bow3 = Polygon(Point(1300, 375), Point(1350, 350), Point(1350, 400))
bow3.setFillColor('pink')
bow3.setBorderWidth(0)
bow3.rotate(-15)
penguin2.add(bow3)





for _ in range(60):  
    penguin.move(-10, 0)  
    paper.refresh() 
    time.sleep(0.05)



paper.add(penguin2)


for _ in range(40):
    penguin2.move(-10, 0)
    paper.refresh()
    time.sleep(0.05)


text3 = Text('wow the sky at night is so beautiful', 30, Point(900, 250))

text3.setFontColor('white')
text3.setFontSize(20)

paper.add(text3)


import time

time.sleep(2)

paper.remove(text3)

text4 = Text('its amazing lets get the camera so we can capture it', 30, Point(600, 250))
text4.setFontColor('white')
text4.setFontSize(20)
paper.add(text4)

time.sleep(2)
paper.remove(text4)

text5 = Text('okay bet that', 30, Point(900, 250))
text5.setFontColor('white')
text5.setFontSize(20)
paper.add(text5)


time.sleep(2)
paper.remove(text5)

for _ in range(60):
    penguin2.move(0,10)
    paper.refresh()
    time.sleep(0.05)

for _ in range(60):
    penguin.move(0,10)
    paper.refresh()
    time.sleep(0.05)













  








