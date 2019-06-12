# -*- coding: utf-8 -*-
from linepy import *
from time import sleep
yinmo = LINE()
int1 = len(yinmo.getGroupIdsInvited())
if int1 == 0:
    print("No groups inviting")
else:
    for groups in yinmo.getGroupIdsInvited():
        print("Reject " + yinmo.getGroup(groups).name)
        sleep(0.5)
        yinmo.rejectGroupInvitation(groups)
    print("\nYou reject" + str(int1) + "groups invitation")
    
