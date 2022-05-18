import os


def cmd(command):
    r = os.system(command)
    return r


if __name__ == '__main__':
    print(cmd("adb devices"))
