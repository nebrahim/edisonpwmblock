from RC import RC
import time

grasshopper = RC(0, 1);

while (True):
  grasshopper.setServoAngle(0);
  grasshopper.setSpeed(0);
  time.sleep(1); 

  grasshopper.setSpeed(500);
  grasshopper.setServoAngle(50);
  time.sleep(1);

  grasshopper.setSpeed(-500);
  grasshopper.setServoAngle(-50);
  time.sleep(.1);
  grasshopper.setSpeed(0);
  time.sleep(.1);
  grasshopper.setSpeed(-500);
  time.sleep(1);

