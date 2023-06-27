# -*- encoding=utf8 -*-
__author__ = "Castamere"

import requests,json
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import log

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

# 看看云APP包名
pkName = 'com.dropcoocam.ali'
start_app(pkName)
class OTA:

    def __init__ (self):
        self.bt_update = poco("com.dropcoocam.ali:id/bt_update")
        self.bt_updating = poco('com.dropcoocam.ali:id/tv_device_updating')
        self.bt_passive = poco('com.dropcoocam.ali:id/tv_device_passive_update_hint')
        self.count = 0
        self.log = log.classlog("OTA")

    def reboot(self):
        flag = True
        count = 0
        device_name="002"
        while(flag):
            try:
                while poco(text="立即配网").exists():
                    sleep(5) # 等待设备联网
                poco(text=device_name).click()
                sleep(3)
                poco("com.dropcoocam.ali:id/btn_settings").click()
                sleep(3)
                poco.swipe([0.5, 0.6], [0.5, 0.1], duration=1) 
                poco(text="重启设备").click()
                poco(text="确定").click()
                sleep(5)
                keyevent('back')
                keyevent('back')
                flag = False
            except:
                if(count==5):
                    exit(0)
                print("Error in Rebooting")
                stop_app(pkName)
                start_app(pkName)
                count+=1

    def run(self):
        while True:
            if self.bt_update.wait(20):
                self.bt_update.click()
                sleep(5)
                self.confirm = poco("com.dropcoocam.ali:id/confirm")
                self.confirm.click()
                sleep(5)    
                self.bt_update = poco("com.dropcoocam.ali:id/bt_update")
                sleep(60)
                self.reboot()
                sleep(5)
                while not self.bt_update.wait(5):
                    sleep(20)
                    stop_app(pkName)
                    start_app(pkName)
                self.count += 1
                self.log.log(f"OTA {self.count} times")
                sleep(20)

ota = OTA()
ota.run()