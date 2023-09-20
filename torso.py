import pybullet as p
import time
import pybullet_data

# Initialize PyBullet
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
# Load the ground
plainid = p.loadURDF("plane.urdf")
# p.setGravity(0,0,-10)
# Load the arm and torso URDF
startPos = [0,0,0]
startOrientation = p.getQuaternionFromEuler([0,0,0])
arm_id = p.loadURDF(r"URDF\arm_with_torso.urdf",startPos,startOrientation)

# Set the initial position of the cube
# p.resetBasePositionAndOrientation(arm_id, [0, 0, 0], [0, 0, 0, 1])
# Joint index (replace with the actual index)
# joint_index = 2  # For example, for the 'upper_arm_to_forearm' joint

# Specific location (x, y, z) and orientation (quaternion: x, y, z, w)
# position = [0, 0, 0]
# orientation = p.getQuaternionFromEuler([0, 0, 0])
# orientation = [x for x in orientation]
# Set the joint's child link to the specific location
# p.resetBasePositionAndOrientation(arm_id, joint_index, position, 1)
trarget = 1
# Simulation loop
for _ in range(10000):
    p.stepSimulation()
    time.sleep(1./240.)
    maxForce = 10
    
    mode = p.POSITION_CONTROL
    p.setJointMotorControl2(arm_id, 1,
 	controlMode=mode, force=maxForce,targetPosition=trarget)
    p.setJointMotorControl2(arm_id, 3,
 	controlMode=mode, force=maxForce,targetPosition=trarget)
    trarget += 0.5