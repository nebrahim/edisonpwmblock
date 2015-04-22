from RC import RC
from getch import getch
import time

speed = 0;
angle = 0;

grasshopper = RC(0, 1);
grasshopper.setServoAngle(0);
grasshopper.setSpeed(0);
 
while (True):
  key = ord(getch());
  print key;

  if key == 3: # ctrl-C
    grasshopper.setServoAngle(0);
    grasshopper.setSpeed(0);
    break;

  if key == 115: # s
    grasshopper.setServoAngle(0);
    if speed > 0:
      grasshopper.setSpeed(-2048);
      time.sleep(.1);
    grasshopper.setSpeed(0);
    speed = 0;
  
  elif key == 27: # up/down/left/right
    key = ord(getch());
    
    if key == 91: # up/down/left/right
      key = ord(getch());

      if key == 65: # up
        if (speed < 1500):
	  speed = speed + 500;
        grasshopper.setSpeed(speed);

      elif key == 66: # down
        if (speed > -1500):
	  speed = speed - 500;
        grasshopper.setSpeed(speed);

      elif key == 67: # right
        if (angle == -50):
	  angle = 0;
        else:
	  angle = 50;
	grasshopper.setServoAngle(angle);

      elif key == 68: # left
	if (angle == 50):
	  angle = 0;
        else:
	  angle = -50;

        grasshopper.setServoAngle(angle);
#
#  elif key == 224: # Special Keys (arrows, functions keys, etc.)
#    key = ord(getch());
