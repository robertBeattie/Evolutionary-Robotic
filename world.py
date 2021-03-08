import pybullet as p
import pybullet_data


class WORLD:

    def __init__(self):

        # add environment and objects
        self.planeId = p.loadURDF("plane.urdf")
        self.robot = p.loadURDF("body.urdf")
        p.loadSDF("world.sdf")
