import operations
from eles.eles import Eles
import time


class Testlsgj(Eles):
    driver = None

    """
    历史告警模块
    
    """
    #竖向导航栏：切换至历史告警tab
    def operations_history_gj_tab_click(self):
        self.eles_click(operations.navigation_Tab_LSGJ)
        time.sleep(0.5)

    #筛选条件：报警类型点击
    def operations_history_gj_type_click(self):
        self.eles_click(operations.history_type)
        time.sleep(0.5)
    #筛选条件：报警类型列表选择
    def operations_history_gj_type_lists_click(self):
        self.eles_click(operations.history_type_lists_select)
        time.sleep(0.5)
    #查询点击
    def operations_history_gj_search_click(self):
        self.eles_click(operations.history_search_button)
        time.sleep(0.5)
    #重置点击
    def operations_history_gj_reset_click(self):
        self.eles_click(operations.history_reset_button)
        time.sleep(0.5)

    #历史告警列表的前后5分钟点击查看
    def operations_history_gj_five_view_click(self):
        self.eles_click(operations.history_lists_view)
        time.sleep(0.5)

    #历史告警列表的前后5分钟前后查看关闭点击
    def operations_history_gj_five_view_close_click(self):
        self.eles_click(operations.history_lists_view_close)
        time.sleep(0.5)


    #历史告警模块的方法组装
    #历史告警查询功能
    def history_gj_search(self):
        self.operations_history_gj_tab_click()
        self.operations_history_gj_type_click()
        self.operations_history_gj_type_lists_click()
        self.operations_history_gj_search_click()
        time.sleep(0.5)

    #历史告警重置功能
    def history_gj_reset(self):
        #self.operations_history_gj_tab_click()
        self.operations_history_gj_reset_click()
        time.sleep(0.5)

    # 历史告警前后5分钟查看功能
    def history_gj_five_view(self):
        self.operations_history_gj_tab_click()
        self.operations_history_gj_five_view_click()
        self.operations_history_gj_five_view_close_click()
        time.sleep(0.5)
