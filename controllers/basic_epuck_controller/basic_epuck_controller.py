"""basic_epuck_controller controller."""
from controller import Robot
import numpy as np

robot = Robot()

timestep = int(robot.getBasicTimeStep())

motor_left = robot.getDevice('left wheel motor')
motor_right = robot.getDevice('right wheel motor')

motor_left.setPosition(float('Inf'))
motor_right.setPosition(float('Inf'))

# ds = robot.getDevice('ps0')
# ds.enable(timestep)

ds = []
for i in range(8):
    ds.append(robot.getDevice(f'ps{i}'))
    ds[-1].enable(timestep)

print("Sensors initialized :)")

while robot.step(timestep) != -1:

    values = []
    for dist in ds:
        values.append(dist.getValue())

    print(values)

    motor_left.setVelocity(np.pi)
    motor_right.setVelocity(np.pi)




