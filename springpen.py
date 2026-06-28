from vpython import *
import math
import time

initpenlen = float(input("Unstretched Spring Length (metres) >>> "))
penlen = float(input("Initial Spring Length (metres >>> "))
dpenlen = float(input("Initial rate of extension of spring >>> "))
k= float(input("Spring Constant of Spring (Nm^-1) >>> "))
m = float(input("Mass of particle (kg) >>> "))
theta = math.radians(float(input("Initial angle of displacement from vertical (degrees) >>> ")))
dtheta = math.radians(float(input("Initial angular velocity (degrees/second)")))
dt = float(input("Timestep (seconds) >>> "))

t = 0
vertical = cylinder(pos=vector(0,-penlen,0),color=color.red,radius=0.02*penlen,length=penlen,axis=vector(0,1,0))
x = penlen*math.sin(theta)
y = penlen*math.cos(theta)

mass = sphere(pos = vector(x,-y,0),color = color.blue , radius = penlen*0.08,make_trail=False)
spring = helix(pos = vector(0,0,0),axis=vector(x,-y,0),color=color.blue,radius=penlen*0.05,length=penlen)


while t <= 1000:

    ddpenlen = (m*dtheta**2*penlen+k*initpenlen-k*penlen+m*9.81*math.cos(theta))/m
    ddtheta = -1*((9.81*math.sin(theta)+2*dpenlen*dtheta)/penlen)
    dpenlen += ddpenlen*dt
    dtheta += ddtheta*dt
    theta += dtheta*dt
    penlen += dpenlen*dt



    x = penlen*math.sin(theta)
    y = penlen*math.cos(theta)

    mass.pos = vector(x,-y,0)
    spring.axis = vector(x,-y,0)
    spring.length = penlen
    
    time.sleep(dt)
    t += dt
    

    
