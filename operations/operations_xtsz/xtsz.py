import operations
import time
from eles.eles import Eles

class Testxtsz(Eles):
    driver = None

    """
    系统设置模块
    
    """

    #竖向导航栏：系统设置tab点击
    def system_set_click(self):
        self.eles_click(operations.navigation_Tab_XTSZ)
        time.sleep(0.5)

    """
    闸门tab
    
    """
    #切换至闸门tab
    def system_zm_tab_click(self):
        self.eles_click(operations.system_zm_tab)
        time.sleep(0.5)

    #闸门tab下的闸门关闭精确角度值修改
    def system_zm_close_input(self):
        self.eles_input(operations.system_zm_close,u'69.8')
        time.sleep(0.5)

    #闸门tab下的可确定闸门打开值修改
    def system_zm_open_sure_input(self):
        self.eles_input(operations.system_zm_open_sure,u'0.8')
        time.sleep(0.5)

    #闸门tab下的可确定闸门关闭值修改
    def system_zm_close_sure_input(self):
        self.eles_input(operations.system_zm_close_sure,u'69.7')
        time.sleep(0.5)

    #闸门tab下的闸门角度最小变化值修改
    def system_zm_samll_input(self):
        self.eles_input(operations.system_zm_small,u'0.3')
        time.sleep(0.5)

    #闸门tab下的保存按钮
    def system_zm_savebutton(self):
        self.eles_click(operations.system_zm_savebutton)
        time.sleep(0.5)


    """
    其他tab
    
    """

    #其他tab点击跳转
    def system_other_click(self):
        self.eles_click(operations.system_other_tab)
        time.sleep(0.5)

    #其他tab下的实时计算周期值修改
    def system_other_reality_update(self):
        self.eles_input(operations.system_other_reality,u'6')
        time.sleep(0.5)

    # 其他tab下的可开闸门水位差值修改
    def system_other_open_update(self):
        self.eles_input(operations.system_other_open,u'5')
        time.sleep(0.5)

    # 其他tab下的通闸允许水位差值修改
    def system_other_all_update(self):
        self.eles_input(operations.system_other_allopen,u'8')
        time.sleep(1)

    # 其他tab下的可视为报警的连续异常值数量值修改
    def system_other_yc_num_update(self):
        self.eles_input(operations.system_other_num,u'2')
        time.sleep(0.5)

    # 其他tab下的地面到闸底的距离值修改
    def system_other_palcetozd_update(self):
        self.eles_input(operations.system_other_placetozm,u'11.5')
        time.sleep(0.5)

    # 其他tab下的地面到人行桥的距离值修改
    def system_other_palcetorxq_update(self):
        self.eles_input(operations.system_other_placetorxq,u'5.7')
        time.sleep(0.5)

    # 其他tab下的可通行的最小桥梁净空值修改
    def system_other_samllbridge_update(self):
        self.eles_input(operations.system_other_Bridge_num,u'8.0')
        time.sleep(0.5)

    # 其他tab下的上游高程值修改
    def system_other_SYGC_update(self):
        self.eles_input(operations.system_other_SYGC_num,u'-2.2')
        time.sleep(0.5)

    # 其他tab下的下游高程值修改
    def system_other_XYGC_update(self):
        self.eles_input(operations.system_other_XYGC_num,u'-1.1')
        time.sleep(0.5)

    # 其他tab下的闸室高程值修改
    def system_other_ZSGC_update(self):
        self.eles_input(operations.system_other_ZSGC_num,u'-2.2')
        time.sleep(0.5)

    # 其他tab下的从上游到下游传感器距离底部值修改
    def system_other_Four_update(self):
        self.eles_input(operations.system_other_Four_nums,u'0.97,1.55,2.48,0.38')
        time.sleep(0.5)

    # 其他tab下的保存按钮
    def system_other_savebutton(self):
        self.eles_click(operations.system_other_savebutton)
        time.sleep(0.5)


    #系统设置模块组装方法
    #闸门tab
    def system_setting_zm(self):
        #self.system_set_click()
        self.system_zm_tab_click()
        self.system_zm_close_input()
        self.system_zm_open_sure_input()
        self.system_zm_close_sure_input()
        self.system_zm_savebutton()
        time.sleep(0.5)

    #其他tab
    def system_setting_other(self):
        self.system_set_click()
        self.system_other_click()
        self.system_other_reality_update()
        time.sleep(0.5)
        self.system_other_open_update()
        time.sleep(0.5)
        self.system_other_all_update()
        time.sleep(0.5)
        self.system_other_yc_num_update()
        time.sleep(1)
        self.system_other_palcetozd_update()
        time.sleep(0.5)
        self.system_other_palcetorxq_update()
        time.sleep(0.5)
        self.system_other_samllbridge_update()
        time.sleep(0.5)
        self.system_other_SYGC_update()
        time.sleep(0.5)
        self.system_other_XYGC_update()
        time.sleep(0.5)
        self.system_other_ZSGC_update()
        time.sleep(0.5)
        self.system_other_Four_update()
        time.sleep(0.5)
        self.system_other_savebutton()
        time.sleep(0.5)



