import operations
import time
from eles.eles import Eles

class Testswjkmanager(Eles):
    """
    水文监控管理

    """
    #竖向功能导航栏切换至：水文监控管理,点击操作
    def operations_hydrology_tab_click(self):
        self.eles_click(operations.navigation_Tab_SWJK)
        time.sleep(0.5)

    #历史数据tab点击操作
    def operations_hydrology_history_tab_click(self):
        self.eles_click(operations.hydrology_history_tab)
        time.sleep(0.5)

    #历史数据下日精度-日期点击选择操作
    def operations_hydrology_history_day_click(self):
        self.eles_click(operations.hydrology_history_day)
        self.eles_click(operations.hydrology_history_day_today)
        time.sleep(0.5)

    # 历史数据下月精度-日期点击选择操作
    def operations_hydrology_history_month_click(self):
        self.eles_click(operations.hydrology_history_month)
        self.eles_click(operations.hydrology_history_month_select)
        self.eles_click(operations.hydrology_history_month_today)
        time.sleep(0.5)

    # 历史数据下年精度-日期点击选择操作
    def operations_hydrology_history_year_click(self):
        self.eles_click(operations.hydrology_history_year)
        self.eles_click(operations.hydrology_history_year_select)
        self.eles_click(operations.hydrology_history_year_today)
        time.sleep(0.5)

    #历史数据下日精度-查询操作
    def operations_hydrology_history_day_search(self):
        self.eles_click(operations.hydrology_history_day_search)
        time.sleep(0.5)

    #历史数据下月精度-查询操作
    def operations_hydrology_history_month_search(self):
        self.eles_click(operations.hydrology_history_month_search)
        time.sleep(0.5)

    #历史数据下年精度-查询操作
    def operations_hydrology_history_year_search(self):
        self.eles_click(operations.hydrology_history_year_search)
        time.sleep(0.5)

    #历史数据下日精度-重置操作
    def operations_hydrology_history_day_reset(self):
        self.eles_click(operations.hydrology_history_day_reset)
        time.sleep(0.5)

    #历史数据下月精度-重置操作
    def operations_hydrology_history_month_reset(self):
        self.eles_click(operations.hydrology_history_month_reset)
        time.sleep(0.5)

    #历史数据下年精度-重置操作
    def operations_hydrology_history_year_reset(self):
        self.eles_click(operations.hydrology_history_year_reset)
        time.sleep(0.5)

    #阈值设定tab点击操作
    def operations_hydrology_threholdset_tab_click(self):
        self.eles_click(operations.hydrology_threholdset_tab)
        time.sleep(0.5)

    #阈值设定-二线上游低水位阈值修改操作
    def operations_hydrology_threholdset_2XSY_low(self):
        self.eles_input(operations.hydrology_threholdset_2XSY_LOW,u'1.5')
        time.sleep(0.5)

    #阈值设定-二线上游低水位报警开关点击操作
    def operations_hydrology_threholdset_2XSY_swicth_click(self):
        self.eles_click(operations.hydrology_threholdset_2XSY_LOW_switch)
        time.sleep(0.5)

    #阈值设定-二线上游低水位保存操作
    def operations_hydrology_threholdset_2XSY_saveButton_click(self):
        self.eles_click(operations.hydrology_threholdset_2XSY_LOW_savebutton)
        time.sleep(0.5)

    # 阈值设定-二线下游高水位阈值修改操作
    def operations_hydrology_threholdset_2XXY_high(self):
        self.eles_input(operations.hydrology_threholdset_2XXY_HIGH, u'8.5')
        time.sleep(0.5)

    # 阈值设定-二线下游高水位报警开关点击操作
    def operations_hydrology_threholdset_2XXY_swicth_click(self):
        self.eles_click(operations.hydrology_threholdset_2XXY_HIGH_switch)
        time.sleep(0.5)

    # 阈值设定-二线下游高水位保存操作
    def operations_hydrology_threholdset_2XXY_saveButton_click(self):
        self.eles_click(operations.hydrology_threholdset_2XXY_HIGH_savebutton)
        time.sleep(0.5)


    '''水文监控管理-历史数据-组装方法'''

    #查询方法
    def hydrology_manager_history_search(self):
        self.operations_hydrology_tab_click()
        self.operations_hydrology_history_tab_click()
        self.operations_hydrology_history_day_click()
        self.operations_hydrology_history_day_search()
        time.sleep(0.5)
        self.operations_hydrology_history_month_click()
        self.operations_hydrology_history_month_search()
        time.sleep(0.5)
        self.operations_hydrology_history_year_click()
        self.operations_hydrology_history_year_search()
        time.sleep(0.5)


    #重置方法
    def hydrology_manager_history_reset(self):
        self.operations_hydrology_tab_click()
        self.operations_hydrology_history_tab_click()
        self.operations_hydrology_history_day_reset()
        time.sleep(0.5)
        self.operations_hydrology_history_month_click()
        self.operations_hydrology_history_month_search()
        self.operations_hydrology_history_month_reset()
        time.sleep(1)
        self.operations_hydrology_history_year_click()
        self.operations_hydrology_history_year_search()
        self.operations_hydrology_history_year_reset()
        time.sleep(1)

    '''水文监控管理-阈值设定-组装方法'''

    # 阈值设定
    def hydrology_manager_threholdset(self):
        self.operations_hydrology_threholdset_tab_click()
        self.operations_hydrology_threholdset_2XSY_low()
        self.operations_hydrology_threholdset_2XSY_swicth_click()
        self.operations_hydrology_threholdset_2XSY_saveButton_click()
        self.operations_hydrology_threholdset_2XXY_high()
        self.operations_hydrology_threholdset_2XXY_swicth_click()
        self.operations_hydrology_threholdset_2XXY_saveButton_click()
        time.sleep(0.5)
