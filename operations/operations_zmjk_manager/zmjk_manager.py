import operations
import time
from eles.eles import Eles

class Testzmjkmanager(Eles):
    """
    闸门监控管理-历史数据功能tab切换

    """
    #点击功能“历史数据”tab
    def operations_tab_click(self):
        self.eles_click(operations.history_tab)
        time.sleep(1)

    #点击功能“阈值设定”tab
    def operations_threholdset_tab_click(self):
        self.eles_click(operations.thrsdhold_setting_tab)
        time.sleep(1)

    #闸门位置选择框点击操作
    def operations_history_zm_click(self):
        self.eles_click(operations.history_tab_zmPosition)
        time.sleep(1)

    #闸门位置选择“二线下游”操作
    def operations_history_zm_select(self):
        self.eles_click(operations.history_tab_zmPosition_WZ)
        time.sleep(1)

    #监控项选择框点击操作
    def operations_history_JKX_click(self):
        self.eles_click(operations.history_tab_zmJKX)
        time.sleep(1)

    #监控项选择"倾斜"操作
    def operations_history_JKX_select(self):
        self.eles_click(operations.history_tab_zmJKX_QX)
        time.sleep(1)

    #开始时间选择框点击操作
    def operations_history_BeginTime_click(self):
        self.eles_click(operations.history_tab_zmBeginTime)
        time.sleep(1)

    #开始时间选择"此刻"操作
    def operations_history_BeginTime_select(self):
        self.eles_click(operations.history_tab_zmBeginTime_Now)
        time.sleep(1)

    #查询按钮点击操作
    def operations_history_Search_click(self):
        self.eles_click(operations.history_tab_zmSearch_button)
        time.sleep(1)

    #重置按钮点击操作
    def operations_history_Reset_click(self):
        self.eles_click(operations.history_tab_zmReset_button)
        time.sleep(1)

    #组装“历史数据”tab下的搜索功能方法
    def history_search(self):
        self.operations_tab_click()
        self.operations_history_zm_click()
        self.operations_history_zm_select()
        self.operations_history_JKX_click()
        self.operations_history_JKX_select()
        self.operations_history_BeginTime_click()
        self.operations_history_BeginTime_select()
        self.operations_history_Search_click()

    #组装“历史数据”tab下的重置功能方法
    def history_reset(self):
        self.operations_history_Reset_click()


    """
    
    闸门监控管理-阈值设定功能
    
    """
    #二线上游角度差修改
    def operations_threhold_setting_2XSY_angle_input(self):
        self.eles_input(operations.angle_2XSY,u'0.5')
        time.sleep(0.5)

    #二线上游角度差报警开关点击
    def operations_threhold_setting_2XSY_angle_click(self):
        self.eles_click(operations.angle_2XSY_switch)
        time.sleep(0.5)

    #二线上游保存按钮
    def operations_threhold_setting_2XSY_angle_button(self):
        self.eles_click(operations.angle_2XSY_saveButton)
        time.sleep(0.5)

    #二线下游角度差修改
    def operations_threhold_setting_2XXY_angle_input(self):
        self.eles_input(operations.angle_2XXY,u'0.5')
        time.sleep(0.5)

    #二线下游角度差报警开关点击
    def operations_threhold_setting_2XXY_angle_click(self):
        self.eles_click(operations.angle_2XXY_switch)
        time.sleep(0.5)

    #二线下游保存按钮
    def operations_threhold_setting_2XXY_angle_button(self):
        self.eles_click(operations.angle_2XXY_saveButton)
        time.sleep(0.5)

    #组装阈值设定的操作方法
    def threhold_setting(self):
        self.operations_threholdset_tab_click()
        self.operations_threhold_setting_2XSY_angle_input()
        self.operations_threhold_setting_2XSY_angle_click()
        self.operations_threhold_setting_2XSY_angle_button()
        self.operations_threhold_setting_2XXY_angle_input()
        self.operations_threhold_setting_2XXY_angle_click()
        self.operations_threhold_setting_2XXY_angle_button()
        time.sleep(0.5)
