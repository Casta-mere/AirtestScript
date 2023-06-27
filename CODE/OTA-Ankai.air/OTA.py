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
        self.bt_uodating = poco('com.dropcoocam.ali:id/tv_device_updating')
        self.bt_passive = poco('com.dropcoocam.ali:id/tv_device_passive_update_hint')
        self.count = 0
        self.log = log.classlog("OTA")

    def run(self):
        while True:
            if self.bt_update.wait(20):
                self.bt_update.click()
                sleep(5)
                self.confirm = poco("com.dropcoocam.ali:id/confirm")
                self.confirm.click()
                sleep(5)    
                self.bt_update = poco("com.dropcoocam.ali:id/bt_update")
                while not self.bt_update.wait(5):
                    sleep(20)
                    stop_app(pkName)
                    start_app(pkName)
                self.count += 1
                self.log.log(f"OTA {self.count} times")
                sleep(20)


ota = OTA()
ota.run()