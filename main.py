# -*- coding: utf-8 -*-
"""
    Star Yuuki Bot - Yuuki
    ~~~~~~~~~~~
     This is a main program in SYB.
     It`s belong to Star Yuuki(pYthon) Bot Project of Star Neptune Bot

    Version: v6.5

    Copyright(c) 2019 Star Inc. All Rights Reserved.
    The software licensed under Mozilla Public License Version 2.0
"""


botStart = time.time()
cl = LINE("robertghanim582@icloud.com","36091vwz")
#cl = LINE("YOUR TOKEN")
#cl = LINE("Email","Password")

cl.log("Auth Token : " + str(cl.authToken))
channelToken = cl.getChannelResult()
readOpen = codecs.open("read.json","r","utf-8")
cl.log("Channel Token : " + str(channelToken))
settingsOpen = codecs.open("temp.json","r","utf-8")

clMID = cl.profile.mid
clProfile = cl.getProfile()
clSettings = cl.getSettings()
oepoll = OEPoll(cl)
call = cl
read = json.load(readOpen)
settings = json.load(settingsOpen)

connect1 = 'CHROME'
Headers1 = {
        'User-Agent': "Line/9.22.1",
        'X-Line-Application': "CROMEOS\t2.1.5ARIFISTIFIK\t11.2.5",
        "x-lal": "ja-US_US",
    }
connect2 = 'WIN'
Headers2 = {
        'User-Agent': "Line/9.22.1",
        'X-Line-Application': "DESKTOPWIN\t5.5.5ARIFISTIFIK\t11.2.5",
        "x-lal": "ja-US_US",
    }
connect3 = 'ios'
Headers3 = {
        'User-Agent': "Line/9.22.1",
        'X-Line-Application': "IOSIPAD\t8.14.2\tiPhone OS\t11.2.5",
        "x-lal": "ja-US_US",
    }

Admin = ["u0dedae6e6ff204f52f2e4a096630ea82"]
KickLimit = 10
CancelLimit = 10
Language = "en"
LINE_ACCESS_KEY = ""
GroupMebers_Demand = 100
helper_LINE_ACCESS_KEYs = []

########################Initializing##########################
from libs import *

Connection = Yuuki_Connection()

Connection.connectInfo = {
    'Host': '',
    'Command_Path': '',
    'LongPoll_path': ''
}

Connection.connectHeader = {
    'X-Line-Application': '',
    'X-Line-Access': LINE_ACCESS_KEY,
    'User-Agent': ''
}

Settings = Yuuki_Settings()

Settings.config["Seq"] = 0
Settings.config["Admin"] = Admin
Settings.config["SecurityService"] = True
Settings.config["Hour_KickLimit"] = KickLimit
Settings.config["Hour_CancelLimit"] = CancelLimit
Settings.config["Default_Language"] = Language
Settings.config["GroupMebers_Demand"] = GroupMebers_Demand
Settings.config["helper_LINE_ACCESS_KEYs"] = helper_LINE_ACCESS_KEYs


Console = Yuuki(Settings, Connection)
Console.cleanMyGroupInvitations()

###########################Start!#############################
print("Star Yuuki BOT - Start Successful!")

if __name__ == "__main__":
    Console.Main()
