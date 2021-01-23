from visual import *
from visual.graph import *
from math import*
import numpy as np

scene.width = 1090
scene.height = 720
scene.title = "Heart"
scene.center = vector(0,2.5,0)
ball2 = sphere(pos=vector(-20,-2,0),color = color.red, radius = 0.1,make_trail=True,trail_type="points",retain=3000)
name = extrusion(pos=[(0,0,0.5),(0,0,0.0)], shape="Niranjan", color=color.red,length=20,material=materials.shiny)

l1 = local_light(pos=ball2.pos, color=ball2.color)

dt = 0.01
t=-6
while(True):        
    rate(100)    
    if(t>6):
        t=-6
    ball2.pos.y =  (2.5*(sin(-5*t)**2)*(2**cos(cos(4.28*2.38*t))))*sin(np.pi/2)+(2.5*sin(sin(-5*t))*(cos(4.28*2.3*t))**2)*cos(np.pi/2)+1   
    ball2.pos.x =  (2.5*(sin(-5*t)**2)*(2**cos(cos(4.28*2.38*t))))*cos(np.pi/2)-(2.5*sin(sin(-5*t))*(cos(4.28*2.3*t))**2)*sin(np.pi/2)
    
    l1.pos.x = ball2.pos.x
    l1.pos.y = ball2.pos.y

    t=t+dt
    
