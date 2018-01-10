from roboy_communication_middleware.msg import MotorCommand, MotorStatus, JointStatus


@nrp.MapRobotPublisher('motor_command',Topic('/roboy/middleware/MotorCommand', MotorCommand))
@nrp.MapRobotSubscriber('motor_status', Topic('/roboy/middleware/MotorStatus', MotorStatus))
# @nrp.MapRobotSubscriber('joint_status', Topic('/roboy/middleware/JointStatus', JointStatus))
@nrp.Robot2Neuron()

def control(t, motor_status, motor_command):
	from roboy_communication_middleware.msg import MotorCommand, MotorStatus, JointStatus
	import time
	time.sleep(0.02)
	if not isinstance(motor_status.value, type(None)):
		id = motor_status.value.id
	command = MotorCommand()
	command.id = id
	command.motors = [0,1,2,3]
	command.setPoints = [1,2,3,4]
	motor_command.send_message(command)
