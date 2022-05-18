import re

from test_tool import win_cmd

# 安装应用
packeages= win_cmd.cmd("adb shell pm list packages -3")
print(type(packeages))
act = win_cmd.cmd('adb shell dumpsys activity activities | findstr "{}"|findstr "Hist #1"'.format("tv.danmaku.bili"))

r = re.findall("/(.*)}", str(act))[0]
print(r)
