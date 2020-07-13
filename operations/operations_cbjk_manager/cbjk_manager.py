import operations
import time
from eles.eles import Eles

class Testcbjkmanager(Eles):
    """
    船舶监控管理

    """
    #竖向导航栏切换至船舶监控管理
    def operations_ship_tab_click(self):
        self.eles_click(operations.navigation_Tab_CBJK)
        time.sleep(0.5)

    #二线上游下的闸首外时的报警类型选择
    def operations_ship_2XSY_outside_alarm_click(self):
        self.eles_click(operations.ship_2XSY_outside_alarm)
        time.sleep(0.5)

    #二线上游下的闸首外时的报警开关点击选择
    def operations_ship_2XSY_outside_switch_click(self):
        self.eles_click(operations.ship_2XSY_outside_switch)
        time.sleep(0.5)

    # 二线上游下的闸首内东时的报警类型点击选择
    def operations_ship_2XSY_inside_east_alarm_click(self):
        self.eles_click(operations.ship_2XSY_inside_east_alarm)
        time.sleep(0.5)

    #二线上游下的闸首内东时的报警开关点击选择
    def operations_ship_2XSY_inside_east_switch_click(self):
        self.eles_click(operations.ship_2XSY_inside_east_switch)
        time.sleep(0.5)

    # 二线上游下的闸首内西时的报警类型点击选择
    def operations_ship_2XSY_inside_weast_alarm_click(self):
        self.eles_click(operations.ship_2XSY_inside_weast_alarm)
        time.sleep(0.5)

    #二线上游下的闸首内西时的报警开关点击选择
    def operations_ship_2XSY_inside_weast_switch_click(self):
        self.eles_click(operations.ship_2XSY_inside_weast_switch)
        time.sleep(0.5)

    #二线上游下的保存按钮点击选择
    def operations_ship_2XSY_savebutton_click(self):
        self.eles_click(operations.ship_2XSY_cb_saveButton)
        time.sleep(0.5)

    #二线下游下的闸首外时的报警类型选择
    def operations_ship_2XXY_outside_alarm_click(self):
        self.eles_click(operations.ship_2XXY_outside_alarm)
        time.sleep(0.5)

    #二线下游下的闸首外时的报警开关点击选择
    def operations_ship_2XXY_outside_switch_click(self):
        self.eles_click(operations.ship_2XXY_outside_switch)
        time.sleep(0.5)

    # 二线下游下的闸首内东时的报警类型点击选择
    def operations_ship_2XXY_inside_east_alarm_click(self):
        self.eles_click(operations.ship_2XXY_inside_east_alarm)
        time.sleep(0.5)

    #二线下游下的闸首内东时的报警开关点击选择
    def operations_ship_2XXY_inside_east_switch_click(self):
        self.eles_click(operations.ship_2XXY_inside_east_switch)
        time.sleep(0.5)

    # 二线下游下的闸首内西时的报警类型点击选择
    def operations_ship_2XXY_inside_weast_alarm_click(self):
        self.eles_click(operations.ship_2XXY_inside_weast_alarm)
        time.sleep(0.5)

    #二线下游下的闸首内西时的报警开关点击选择
    def operations_ship_2XXY_inside_weast_switch_click(self):
        self.eles_click(operations.ship_2XXY_inside_weast_switch)
        time.sleep(0.5)

    #二线下游下的保存按钮点击选择
    def operations_ship_2XXY_savebutton_click(self):
        self.eles_click(operations.ship_2XXY_cb_saveButton)
        time.sleep(0.5)

    #船舶监控管理组装方法
    #二线上游的船舶监控操作方法
    def ship_manager_2XSY(self):
        self.operations_ship_tab_click()
        self.operations_ship_2XSY_outside_alarm_click()
        self.operations_ship_2XSY_outside_switch_click()
        self.operations_ship_2XSY_inside_east_alarm_click()
        self.operations_ship_2XSY_inside_east_switch_click()
        self.operations_ship_2XSY_inside_weast_alarm_click()
        self.operations_ship_2XSY_inside_east_switch_click()
        self.operations_ship_2XSY_savebutton_click()
        time.sleep(1)

    #二线下游的船舶监控操作方法
    def ship_manager_2XXY(self):
        self.operations_ship_tab_click()
        self.operations_ship_2XXY_outside_alarm_click()
        self.operations_ship_2XXY_outside_switch_click()
        self.operations_ship_2XXY_inside_east_alarm_click()
        self.operations_ship_2XXY_inside_east_switch_click()
        self.operations_ship_2XXY_inside_weast_alarm_click()
        self.operations_ship_2XXY_inside_east_switch_click()
        self.operations_ship_2XXY_savebutton_click()
        time.sleep(1)