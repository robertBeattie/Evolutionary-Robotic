import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# add gravity
p.setGravity(0,0,-9.8)

# add environment and objects
planeId = p.loadURDF("plane.urdf")
p.loadSDF("box.sdf")

for i in range(1000000):
    p.stepSimulation()
    time.sleep(.001)
p.disconnect()