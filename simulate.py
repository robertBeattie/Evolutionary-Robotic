import pybullet as p
import time

physicsClient = p.connect(p.GUI)

p.loadSDF("box.sdf")
for i in range(1000000):
    p.stepSimulation()
    time.sleep(.001)
p.disconnect()