import operations
import time
from eles.eles import Eles

class Testsxtsz(Eles):
    driver = None

    """
    摄像头设置模块
    
    """
    #竖向导航栏：切换至摄像头设置tab
    def operations_sxtsz_tab_click(self):
        self.eles_click(operations.navigation_Tab_SXTSZ)
        time.sleep(0.5)

    #摄像头删除点击
    def operations_sxtsz_delete_click(self):
        self.eles_click(operations.camera_close)
        time.sleep(0.5)

    #摄像头删除保存点击
    def operations_sxtsz_delete_save_click(self):
        self.eles_click(operations.camera_close_savebutton)
        time.sleep(0.5)

    #摄像头窗口选择
    def operations_sxtsz_windows_select_click(self):
        self.eles_click(operations.camera_update_windows_select)
        time.sleep(0.5)

    #获取选中的摄像头窗口中的文字信息
    def operations_sxtsz_windows_select_text(self):
        self.eles_get_value(operations.camera_update_windows_select)
        time.sleep(0.5)

    #摄像头列表选择：根据被删除的摄像头对应的文字取
    def operations_sxtsz_lists_select_by_text(self):
        self.eles_click(self.eles_get_value(operations.camera_update_windows_select))
        time.sleep(0.5)

    #摄像头新增保存点击
    def operations_sxtsz_update_save_click(self):
        self.eles_click(operations.camera_update_savebutton)
        time.sleep(0.5)


    #组装方法

    #摄像头删除方法
    def camera_delete(self):
        self.operations_sxtsz_tab_click()
        self.operations_sxtsz_delete_click()
        self.operations_sxtsz_delete_save_click()
        time.sleep(0.5)

    #摄像头新增方法
    def camera_update(self):
        self.operations_sxtsz_tab_click()
        self.operations_sxtsz_windows_select_click()
        self.operations_sxtsz_windows_select_text()
        self.operations_sxtsz_lists_select_by_text()
        self.operations_sxtsz_update_save_click()
        time.sleep(0.5)
