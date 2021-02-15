import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5

for i in range(6):
    x += i
    for j in range(6):
        y += 1
        _length = length
        _width = width
        _height = height

        for k in range(10):
            _length *= .9
            _width *= .9
            _height *= .9
            pyrosim.Send_Cube(name="Box" + str(k), pos=[x, y, z + k],
                              size=[_length, _width, _height])
    y = 0
    x = 0



pyrosim.End()
