#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 275  # Min pulse length out of 4096
servoMax = 550  # Max pulse length out of 4096
speedMin = 275
speedMax = 550

def arm(channel):
  setSpeed(channel, -2048)
  time.sleep(1)
  setSpeed(channel, 0)
  time.sleep(1)

# map from one value range to another
def map (value, fromLow, fromHigh, toLow, toHigh):
  fromRange = (fromHigh - fromLow)
  toRange   = (toHigh   - toLow)
  return (((value - fromLow) * toRange) / fromRange) + toLow

# -90 - left
# 90  - right
# set to -50/50 for RC car
def setAngle(channel, angle):
  pulse = map(angle, -90, 90, servoMin, servoMax)
  print "Angle: " + str(angle) + " Pulse: " + str(pulse)
  pwm.setPWM(channel, 0, pulse)

# -2048 - backwards full speed
# 0     - stop
# 2048  - forwards full speed
# 300/-200 limit for RC car
def setSpeed(channel, speed):
  speed = speed * -1;
  pulse = map(speed, -2048, 2048, speedMin, speedMax) 
  print "Speed: " + str(speed) + " Pulse: " + str(pulse)
  pwm.setPWM(channel, 0, pulse)

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
#arm(1)
while (True):
  # Change speed of continuous servo on channel O
  setAngle(0, 0);
  setSpeed(1, 500);
  time.sleep(1);
  setSpeed(1, -2048);
  setSpeed(1, 0);
#  setSpeed(1, -900);
  time.sleep(1);
  setSpeed(1, -500);
  time.sleep(1);
#  setAngle(0, -50) 
#  setSpeed(1, -700)
#  time.sleep(1)
#  setAngle(0, 0) 
#  setSpeed(1, 0)
#  time.sleep(1)
#  setAngle(0, 50) 
#  setSpeed(1, 700)
#  time.sleep(1)
#  setAngle(0, 0) 
#  setSpeed(1, 0)
#  time.sleep(1)


