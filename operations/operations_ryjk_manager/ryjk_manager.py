import operations
import time
from eles.eles import Eles

class Testryjkmanager(Eles):
    """
    人员监控管理

    """
    #竖向导航栏切换至人员监控管理
    def operations_people_tab_click(self):
        self.eles_click(operations.navigation_Tab_RYJK)
        time.sleep(0.5)

    #二线上游下的闸门打开时的报警类型选择
    def operations_people_2XSY_open_alarm_click(self):
        self.eles_click(operations.people_2XSY_open_alarm)
        time.sleep(0.5)

    #二线上游下的闸门打开时的报警开关点击选择
    def operations_people_2XSY_open_switch_click(self):
        self.eles_click(operations.people_2XSY_open_switch)
        time.sleep(0.5)

    # 二线上游下的闸门关闭时的报警类型点击选择
    def operations_people_2XSY_close_alarm_click(self):
        self.eles_click(operations.people_2XSY_close_alarm)
        time.sleep(0.5)

    #二线上游下的闸门关闭时的报警开关点击选择
    def operations_people_2XSY_close_switch_click(self):
        self.eles_click(operations.people_2XSY_close_switch)
        time.sleep(0.5)

    # 二线上游下的闸门运动时的报警类型点击选择
    def operations_people_2XSY_running_alarm_click(self):
        self.eles_click(operations.people_2XSY_running_alarm)
        time.sleep(0.5)

    #二线上游下的闸门运动时的报警开关点击选择
    def operations_people_2XSY_running_switch_click(self):
        self.eles_click(operations.people_2XSY_running_switch)
        time.sleep(0.5)

    #二线上游下的保存按钮点击选择
    def operations_people_2XSY_savebutton_click(self):
        self.eles_click(operations.people_2XSY_saveButton)
        time.sleep(0.5)

    # 二线下游下的闸门打开时的报警类型选择
    def operations_people_2XXY_open_alarm_click(self):
        self.eles_click(operations.people_2XXY_open_alarm)
        time.sleep(0.5)

    # 二线下游下的闸门打开时的报警开关点击选择
    def operations_people_2XXY_open_switch_click(self):
        self.eles_click(operations.people_2XXY_open_switch)
        time.sleep(0.5)

    # 二线下游下的闸门关闭时的报警类型点击选择
    def operations_people_2XXY_close_alarm_click(self):
        self.eles_click(operations.people_2XXY_close_alarm)
        time.sleep(0.5)

    # 二线下游下的闸门关闭时的报警开关点击选择
    def operations_people_2XXY_close_switch_click(self):
        self.eles_click(operations.people_2XXY_close_switch)
        time.sleep(0.5)

    # 二线下游下的闸门运动时的报警类型点击选择
    def operations_people_2XXY_running_alarm_click(self):
        self.eles_click(operations.people_2XXY_running_alarm)
        time.sleep(0.5)

    # 二线下游下的闸门运动时的报警开关点击选择
    def operations_people_2XXY_running_switch_click(self):
        self.eles_click(operations.people_2XXY_running_switch)
        time.sleep(0.5)

    # 二线下游下的保存按钮点击选择
    def operations_people_2XXY_savebutton_click(self):
        self.eles_click(operations.people_2XXY_saveButton)
        time.sleep(0.5)


    #人员监控管理组装方法
    #二线上游的人员监控操作方法
    def people_manager_2XSY(self):
        self.operations_people_tab_click()
        self.operations_people_2XSY_open_alarm_click()
        self.operations_people_2XSY_open_switch_click()
        self.operations_people_2XSY_close_alarm_click()
        self.operations_people_2XSY_close_switch_click()
        self.operations_people_2XSY_running_alarm_click()
        self.operations_people_2XSY_running_switch_click()
        self.operations_people_2XSY_savebutton_click()
        time.sleep(1)

    #二线下游的人员监控操作方法
    def people_manager_2XXY(self):
        self.operations_people_2XXY_open_alarm_click()
        self.operations_people_2XXY_open_switch_click()
        self.operations_people_2XXY_close_alarm_click()
        self.operations_people_2XXY_close_switch_click()
        self.operations_people_2XXY_running_alarm_click()
        self.operations_people_2XXY_running_switch_click()
        self.operations_people_2XXY_savebutton_click()
        time.sleep(1)