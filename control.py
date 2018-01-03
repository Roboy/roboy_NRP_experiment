from roboy_communication_middleware.msg import MotorCommand, MotorStatus, JointStatus

@nrp.MapRobotPublisher('motor_command',Topic('/roboy/middleware/MotorCommand', MotorCommand))
@nrp.MapRobotSubscriber('motor_status', Topic('/roboy/middleware/MotorStatus', MotorStatus))
@nrp.MapRobotSubscriber('joint_status', Topic('/roboy/middleware/MotorStatus', JointStatus))
@nrp.Robot2Neuron()

def transferfunction():
	x=MotorStatus()