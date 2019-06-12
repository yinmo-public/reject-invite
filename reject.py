# -*- coding: utf-8 -*-
from linepy import *
from time import sleep
yinmo = LINE()
int1 = len(yinmo.getGroupIdsInvited())
if int1 == 0:
    print("沒有發出邀請的群組")
else:
    for groups in yinmo.getGroupIdsInvited():
        print("已拒絕加入 " + yinmo.getGroup(groups).name)
        sleep(0.5)
        yinmo.rejectGroupInvitation(groups)
    print("\n已拒絕" + str(int1) + "個群組邀請")
    
