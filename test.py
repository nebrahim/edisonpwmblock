from RC import RC
from getch import getch
import time

speed = 0;

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
	time.sleep(.1);
	grasshopper.setSpeed(0);
	time.sleep(.1);
	grasshopper.setSpeed(speed);

      elif key == 67: # right
        grasshopper.setServoAngle(50);

      elif key == 68: # left
        grasshopper.setServoAngle(-50);
#
#  elif key == 224: # Special Keys (arrows, functions keys, etc.)
#    key = ord(getch());
