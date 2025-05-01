import getpass
import os
import shutil

def error():
    print(ERROR + " ------------------------------------------------")
    print(ERROR + " + 按任意键退出FixGreenHub")
    print(ERROR + " ------------------------------------------------")


def end():
    print(INFO + " ------------------------------------------------")
    print(INFO + " + 已重置GreenHub时间为60分钟，请重新打开GreenHub")
    print(INFO + " + 按任意键退出FixGreenHub")
    print(INFO + " ------------------------------------------------")


def fix(path):
    try:
        shutil.rmtree(path)
        end()
    except OSError as e:
        print(ERROR + "重置GreenHub失败！")
        print(ERROR + " ------------------------------------------------")
        print(ERROR + " + 请检查GreenHub是否关闭")
        print(ERROR + " + 请检查FixGreenHub是否拥有权限")
        print(ERROR + " + 若非以上问题，请联系：2049621985@qq.com")
        print(ERROR + " ------------------------------------------------")
        error()


def getpath():
    user = getpass.getuser()
    path = f'C:\\Users\\{user}\\AppData\\Roaming\\GreenHub'
    return path

def check_path():
    path=getpath()
    status = os.path.exists(path)
    if status:
        print(INFO + "获取GreenHub数据储存路径（非安装路径）成功")
        print(INFO + " ------------------------------------------------")
        print(INFO + " + 路径: "+path)
        print(INFO + " ------------------------------------------------")
        fix(path)
    else:
        print(ERROR + "获取GreenHub数据储存路径（非安装路径）错误！")
        print(ERROR + " ------------------------------------------------")
        error()


if __name__ == '__main__':
    attempt=False
    INFO = "[\033[92mINFO\033[0m]"
    ERROR = "[\033[91mERROR\033[0m]"
    try:
        os.system("taskkill /im Greenhub.exe /f")
    except:
        pass
    check_path()
    input()

