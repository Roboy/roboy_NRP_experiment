from roboy_communication_middleware.msg import MotorCommand, MotorStatus, JointStatus
from std_msgs.msg import Int32

@nrp.MapRobotPublisher('motor_command',Topic('/roboy/middleware/MotorCommand', MotorCommand))
@nrp.MapRobotSubscriber('motor_status', Topic('/roboy/middleware/MotorStatus', MotorStatus))
# @nrp.MapRobotSubscriber('joint_status', Topic('/roboy/middleware/JointStatus', JointStatus))
@nrp.Robot2Neuron()

def control(t, motor_status, motor_command):
	x=1