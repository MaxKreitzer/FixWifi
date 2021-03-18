import os
import time
print("Would you like to run FixWifi")
if str(input()) == "YES":
    os.system("nmcli radio wifi off")
    print("wifi now disabled")
    time.sleep(10)
    os.system("nmcli radio wifi on")
    print("wifi reestablished")
else:
    print("ok")