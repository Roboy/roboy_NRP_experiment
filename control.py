from roboy_communication_middleware.msg import MotorCommand, MotorStatus, JointStatus
from roboy_communication_middleware.srv import ControlMode

import rospy

rospy.wait_for_service("/roboy/middleware/ControlMode")
control_mode = rospy.ServiceProxy("/roboy/middleware/ControlMode", ControlMode, persistent=True)
# default control mode: displacement
control_mode(2,0)

t_prev = 0.0

@nrp.MapRobotPublisher('motor_command',Topic('/roboy/middleware/MotorCommand', MotorCommand))
@nrp.MapRobotSubscriber('motor_status', Topic('/roboy/middleware/MotorStatus', MotorStatus))
@nrp.MapVariable("t_prev", global_key="t_prev", initial_value=0.0)
# @nrp.MapRobotSubscriber('joint_status', Topic('/roboy/middleware/JointStatus', JointStatus))
# @nrp.MapVariable("control_mode", initial_value=rospy.ServiceProxy("/roboy/middleware/ControlMode", ControlMode, persistent=True))
@nrp.Robot2Neuron()

def control(t, t_prev, motor_status, motor_command):

	from roboy_communication_middleware.msg import MotorCommand
	import time

	time.sleep(0.02)
	if not isinstance(motor_status.value, type(None)):
		id = motor_status.value.id
	command = MotorCommand()
	command.id = id
	command.motors = [0]
	if (t_prev.value==0.0 or t-t_prev.value>10):
		t_prev.value = t
		command.setPoints = [2]
		clientLogger.info("Moving")
		motor_command.send_message(command)
	elif (t-t_prev.value>5 and t-t_prev.value<10):
		command.setPoints = [0]
		motor_command.send_message(command)
		clientLogger.info("Not")


