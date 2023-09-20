import pybullet as p
import time
import pybullet_data

# Initialize PyBullet
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
# Load the ground
planeId = p.loadURDF("plane.urdf")

# Load the cube URDF
cube_id = p.loadURDF("URDF\\test.urdf")

# Set the initial position of the cube
p.resetBasePositionAndOrientation(cube_id, [0, 0, 0.5], [0, 0, 0, 1])

# Target position [x, y, z]
target_position = [2, 2, 1]

# Move the cube to the target position
for i in range(2000):
    current_position, _ = p.getBasePositionAndOrientation(cube_id)
    displacement = [t - c for t, c in zip(target_position, current_position)]
    
    # Update position
    new_position = [c +   d for c, d in zip(current_position, displacement)]
    p.resetBasePositionAndOrientation(cube_id, new_position, [0, 0, 0, 1])
    
    # Step simulation
    p.stepSimulation()
    time.sleep(1./240.)
p.disconnect()