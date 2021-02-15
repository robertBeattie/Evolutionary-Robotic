import pybullet as p
import time

physicsClient = p.connect(p.GUI)
p.setGravity(0,0,-9.8)

p.loadSDF("box.sdf")
for i in range(1000000):
    p.stepSimulation()
    time.sleep(.001)
p.disconnect()