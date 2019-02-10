# -*- coding: utf-8 -*-
from linepy import *
yinmo = LINE()
oepoll = OEPoll(yinmo)
int1 = len(yinmo.getGroupIdsInvited())
if int1 == 0:
    print("沒有發出邀請的群組")
else:
    for groups in yinmo.getGroupIdsInvited():
        print("已拒絕加入 " + yinmo.getGroup(groups).name)
        yinmo.rejectGroupInvitation(groups)
    print("\n您拒絕" + str(int1) + "個群組邀請")
    
