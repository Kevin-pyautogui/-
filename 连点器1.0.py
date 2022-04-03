import pyautogui as pg
import time
pg.FAILSAFE=True
#输入ldq（连点器），移到要点的上面，然后就开始自己点了
kjj=input('')#快捷键输入

if kjj=='ldq':#连点器刷赞功能
    time.sleep(7)#延迟7秒
    x,y=pg.position()#获得鼠标位置
    while True:
        pg.PAUSE=0.000000000000000000000000000000000001#每隔0.1秒执行pyautogui
        pg.click(x,y)
        #按alt-control-del退出