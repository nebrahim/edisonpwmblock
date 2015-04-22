#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM

class RC(object):
  
  @staticmethod
  def map(value, fromLow, fromHigh, toLow, toHigh):
    fromRange = fromHigh - fromLow;
    toRange   = toHigh - toLow;
    return (((value - fromLow) * toRange) / fromRange) + toLow; 

  def __init__(self, servo_channel, motor_channel):
    self.servo_channel = servo_channel;
    self.motor_channel = motor_channel;
    self.servoMin      = 275; # 1ms pulse
    self.servoMax      = 550; # 2ms pulse
    self.speedMin      = 275; # 1ms pulse
    self.speedMax      = 550; # 2ms pulse
    self.pwm           = PWM(0x40);
    self.pwm.setPWMFreq(60);
    
  ######################################################################
  # Angle is in degrees. 
  # -50 degrees corresponds to full left for grasshopper
  # 50 degrees corresponds to full right for grasshopper
  #
  def setServoAngle(self, angle):
    pulse = self.map(angle, -90, 90, self.servoMin, self.servoMax);
    self.pwm.setPWM(self.servo_channel, 0, pulse);

  ##################################################################### 
  # Speed is a relative number between -2048 and 2048
  # 0     - stop
  # 2048  - full speed forward
  # -2048 - full spped backwards
  #
  # depending on surface, low numbers may not move RC car at all
  #
  def setSpeed(self, speed):
    pulse = self.map(speed * -1, -2048, 2048, self.speedMin, self.speedMax);
    self.pwm.setPWM(self.motor_channel, 0, pulse);

  

