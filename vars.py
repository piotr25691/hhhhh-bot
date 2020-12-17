import os
import datetime
from main import client
import json

forbidden = ["luna tiene sexo con**﻿ ﻿**gatos", "luna tiene sexo con gatos", "luna has sex with a cat",
                 "luna tiene sexo con gato-s", "luna tiene sexo con cats", "luna sexi koty",
                 "luna tiene sexo con gato s", "luna tiene sexo con catos"]
pings = ['<@742388119516741642>', '<@!742388119516741642>']
owner = "603635602809946113"
version = "1.6.3"
version_ = "1.6.3"
build = "20201217"
totalcommands = len(client.commands)
global msg_
msg_ = None
startTime = datetime.datetime.utcnow()
clear = lambda: os.system('clear')

with open("removed.txt") as f:
    removed = int(f.read().strip())
with open("hcount.txt") as f:
    hcount = int(f.read().strip())
tos = ["nigga", "nigger", "nigguh"]
admins = [603635602809946113, 444550944110149633, 429935667737264139, 350325552344858624]
token_msgs = ["hh!eval token", "hh!eval TOKEN", "hh!e token", "hh!e TOKEN", "hh!evaluate token",
                  "hh!evaluate TOKEN"]
token = ":no_entry: **NO!** I'm not leaking my token!"

with open("prefixes.json") as f:
    prefixes = json.load(f)