# -*- coding: utf-8 -*-
from linepy import *
yinmo = LINE ()
oepoll = OEPoll(yinmo)
for groups in yinmo.getGroupIdsInvited():
    yinmo.rejectGroupInvitation(groups)
    print("已拒絕群組邀請")