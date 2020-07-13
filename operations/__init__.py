from selenium.webdriver.common.by import By
from xeger import Xeger

URL = "http://192.168.102.50:6433/"  #定义URL

xeger = Xeger()

#登录
public_username_input = By.ID, "username"  #登录用户名ID
public_password_input = By.ID, "password"  #登录密码ID
login_button = By.CSS_SELECTOR, ".ant-btn"  #登录按钮

#竖向导航栏的功能tab切换
navigation_Tab_ZMJK = By.XPATH, "/html/body/div/section/aside/div/div/ul/li[1]/span" #点击竖向导航栏：闸门监控管理
navigation_Tab_SWJK = By.XPATH, "/html/body/div/section/aside/div/div/ul/li[2]/span" #点击竖向导航栏：水文监控管理
navigation_Tab_RYJK = By.XPATH, "/html/body/div/section/aside/div/div/ul/li[3]/span" #点击竖向导航栏：人员监控管理
navigation_Tab_CBJK = By.XPATH, "/html/body/div/section/aside/div/div/ul/li[4]" #点击竖向导航栏：船舶监控管理
navigation_Tab_LSGJ = By.XPATH, "/html/body/div/section/aside/div/div/ul/li[5]/span" #点击竖向导航栏：历史告警
navigation_Tab_XTSZ = By.XPATH, "/html/body/div/section/aside/div/div/ul/li[6]/span" #点击竖向导航栏：系统设置
navigation_Tab_SXTSZ = By.XPATH, "/html/body/div/section/aside/div/div/ul/li[7]/span" #点击竖向导航栏：摄像头设置


#闸门监控管理-历史数据
history_tab = By.XPATH, ".//*[@id='root']/section/section/main/div/div/div[1]/div/div/div/div/div[1]/div[2]"  #历史数据tab
history_tab_zmPosition = By.CSS_SELECTOR, "#upDownEnum > div > div"  #闸门位置选项
history_tab_zmPosition_WZ = By.CSS_SELECTOR, "li.ant-select-dropdown-menu-item:nth-child(1)"  #闸门位置选择二线下游
history_tab_zmJKX = By.CSS_SELECTOR, "#senseType > div > div > div"
history_tab_zmJKX_QX = By.XPATH, "/html/body/div[3]/div/div/div/ul/li[3]"  #监控项选择倾斜
history_tab_zmBeginTime = By.CSS_SELECTOR, "#beginDateStr > div > input"  #选择开始时间点击
history_tab_zmBeginTime_Now = By.LINK_TEXT, "此刻"
history_tab_zmSearch_button = By.CSS_SELECTOR, "#root > section > section > main > div > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.style_historicalContainer__2X1G5 > div.style_search__3u0Ny > form > div:nth-child(6) > div > div > span > button.ant-btn.ant-btn-primary"
history_tab_zmReset_button = By.CSS_SELECTOR, "#root > section > section > main > div > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.style_historicalContainer__2X1G5 > div.style_search__3u0Ny > form > div:nth-child(6) > div > div > span > button:nth-child(2)"


#闸门监控管理-阈值设定
thrsdhold_setting_tab  = By.XPATH, "//*[@id='root']/section/section/main/div/div/div[1]/div/div/div/div/div[1]/div[3]"  #阈值设定tab

#二线上游
angle_2XSY = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div[3]/div[2]/div/div/div[1]/form/div[2]/div[2]/div/span/div/div[2]/input" #二线上游角度差设定
angle_2XSY_switch = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div[3]/div[2]/div/div/div[1]/form/div[4]/div/div/span/button/span" #二线上游报警开关 /html/body/div/section/section/main/div/div/div[3]/div[3]/div[2]/div/div/div[1]/form/div[4]/div/div/span/button
angle_2XSY_saveButton = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div[3]/div[2]/div/div/div[1]/form/div[5]/div/div/span/button" #二线上游报警保存

#二线下游
angle_2XXY = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div[3]/div[2]/div/div/div[2]/form/div[2]/div[2]/div/span/div/div[2]/input" #二线下游角度差设定
angle_2XXY_switch = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div[3]/div[2]/div/div/div[2]/form/div[4]/div/div/span/button" #二线下游报警开关
angle_2XXY_saveButton = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div[3]/div[2]/div/div/div[2]/form/div[5]/div/div/span/button" #二线下游报警保存


#水文监控管理模块

#水文监控-历史数据-日精度
hydrology_history_tab = By.XPATH, "//*[@id='root']/section/section/main/div/div/div[1]/div/div/div/div/div[1]/div[2]" #历史数据tab点击
hydrology_history_day = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div[2]/div[2]/div[1]/form/div[2]/div/div/span/span/div/input" #日精度下的日期选择
hydrology_history_day_today = By.LINK_TEXT, "今天"  #选择今天
hydrology_history_day_search = By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[3]/div[2]/div[2]/div[1]/form/div[3]/div/div/span/button[1]" #查询按钮点击
hydrology_history_day_reset = By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[3]/div[2]/div[2]/div[1]/form/div[3]/div/div/span/button[2]" #重置按钮点击

#水文监控-历史数据-月精度
hydrology_history_month = By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[3]/div[2]/div[2]/div[1]/form/div[1]/div[2]/div/span/div/label[2]/span[2]" #月精度点击
hydrology_history_month_select = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div[2]/div[2]/div[1]/form/div[2]/div/div/span/span/div/input" #月精度下的日期点击
hydrology_history_month_today = By.LINK_TEXT, "六月"  #选择六月
hydrology_history_month_search = By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[3]/div[2]/div[2]/div[1]/form/div[3]/div/div/span/button[1]" #查询按钮点击
hydrology_history_month_reset = By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[3]/div[2]/div[2]/div[1]/form/div[3]/div/div/span/button[2]" #重置按钮点击


#水文监控-历史数据-年精度
hydrology_history_year = By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[3]/div[2]/div[2]/div[1]/form/div[1]/div[2]/div/span/div/label[3]/span[2]" #年精度点击
hydrology_history_year_select = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div[2]/div[2]/div[1]/form/div[2]/div/div/span/span/div/input" #年精度下的日期点击
hydrology_history_year_today = By.LINK_TEXT, "2020"  #选择2020
hydrology_history_year_search = By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[3]/div[2]/div[2]/div[1]/form/div[3]/div/div/span/button[1]" #查询按钮点击
hydrology_history_year_reset = By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[3]/div[2]/div[2]/div[1]/form/div[3]/div/div/span/button[2]" #重置按钮点击

#水文监控-阈值设定-二线上游
hydrology_threholdset_tab = By.XPATH, "/html/body/div/section/section/main/div/div/div[1]/div/div/div/div/div[1]/div[3]" #阈值设定tab点击
hydrology_threholdset_2XSY_LOW = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div[3]/div[2]/div/div/div[1]/div/form[1]/div[2]/div[2]/div/span/div/div[2]/input" #二线上游低水位
hydrology_threholdset_2XSY_LOW_switch = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div[3]/div[2]/div/div/div[1]/div/form[1]/div[4]/div/div/span/button"#二线上游低水位报警开关点击
hydrology_threholdset_2XSY_LOW_savebutton = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div[3]/div[2]/div/div/div[1]/div/div/button" #二线上游水位保存按钮

#水文监控-阈值设定-二线下游
hydrology_threholdset_2XXY_HIGH = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div[3]/div[2]/div/div/div[2]/div/form[2]/div[2]/div[2]/div/span/div/div[2]/input" #二线下游高水位
hydrology_threholdset_2XXY_HIGH_switch = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div[3]/div[2]/div/div/div[2]/div/form[2]/div[4]/div/div/span/button"#二线下游高水位报警开关点击
hydrology_threholdset_2XXY_HIGH_savebutton = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div[3]/div[2]/div/div/div[2]/div/div/button" #二线下游水位保存按钮


#人员监控管理-二线上游
#闸门打开
people_2XSY_open_alarm = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[1]/div/form[1]/div[2]/div[2]/div/span/div/label[2]/span[1]/input" #二线上游闸门打开时报警级别选项
people_2XSY_open_switch = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[1]/div/form[1]/div[3]/div/div/span/button/span" #二线上游闸门打开时开关点击
#闸门关闭
people_2XSY_close_alarm = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[1]/div/form[2]/div[2]/div[2]/div/span/div/label[2]/span[1]/input" #二线上游闸门打开时报警级别选项
people_2XSY_close_switch = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[1]/div/form[2]/div[3]/div/div/span/button/span" #二线上游闸门打开时开关点击
#闸门运动
people_2XSY_running_alarm = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[1]/div/form[3]/div[2]/div[2]/div/span/div/label[2]/span[1]/input" #二线上游闸门打开时报警级别选项
people_2XSY_running_switch = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[1]/div/form[3]/div[3]/div/div/span/button/span" #二线上游闸门打开时开关点击
#上游保存
people_2XSY_saveButton = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[1]/div/div/button" #二线上游闸门打开时报警级别选项
#二线下游
#闸门打开
people_2XXY_open_alarm = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[2]/div/form[1]/div[2]/div[2]/div/span/div/label[2]/span[1]/input" #二线上游闸门打开时报警级别选项
people_2XXY_open_switch = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[2]/div/form[1]/div[3]/div/div/span/button/span" #二线上游闸门打开时开关点击
#闸门关闭
people_2XXY_close_alarm = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[2]/div/form[2]/div[2]/div[2]/div/span/div/label[2]/span[1]/input" #二线上游闸门打开时报警级别选项
people_2XXY_close_switch = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[2]/div/form[2]/div[3]/div/div/span/button/span" #二线上游闸门打开时开关点击
#闸门运动
people_2XXY_running_alarm = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[2]/div/form[3]/div[2]/div[2]/div/span/div/label[2]/span[1]/input" #二线上游闸门打开时报警级别选项
people_2XXY_running_switch = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[2]/div/form[3]/div[3]/div/div/span/button/span" #二线上游闸门打开时开关点击
#上游保存
people_2XXY_saveButton = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[2]/div/div/button" #二线上游闸门打开时报警级别选项


#船舶监控管理-二线上游
#闸首外
ship_2XSY_outside_alarm = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[1]/div/form[1]/div[2]/div[2]/div/span/div/label[2]/span[1]/input" #二线上游闸门打开时报警级别选项
ship_2XSY_outside_switch = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[1]/div/form[1]/div[3]/div/div/span/button/span" #二线上游闸门打开时开关点击
#闸首内东
ship_2XSY_inside_east_alarm = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[1]/div/form[2]/div[2]/div[2]/div/span/div/label[2]/span[1]/input" #二线上游闸门打开时报警级别选项
ship_2XSY_inside_east_switch = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[1]/div/form[2]/div[3]/div/div/span/button/span" #二线上游闸门打开时开关点击
#闸首内西
ship_2XSY_inside_weast_alarm = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[1]/div/form[3]/div[2]/div[2]/div/span/div/label[2]/span[1]/input" #二线上游闸门打开时报警级别选项
ship_2XSY_inside_weast_switch = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[1]/div/form[3]/div[3]/div/div/span/button/span" #二线上游闸门打开时开关点击
#上游保存
ship_2XSY_cb_saveButton = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[1]/div/div/button" #二线上游闸门打开时报警级别选项

#二线下游
#闸首外
ship_2XXY_outside_alarm = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[2]/div/form[1]/div[2]/div[2]/div/span/div/label[1]/span[1]/input" #二线上游闸门打开时报警级别选项
ship_2XXY_outside_switch = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[2]/div/form[1]/div[3]/div/div/span/button/span" #二线上游闸门打开时开关点击
#闸首内东
ship_2XXY_inside_east_alarm = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[2]/div/form[2]/div[2]/div[2]/div/span/div/label[1]/span[1]/input" #二线上游闸门打开时报警级别选项
ship_2XXY_inside_east_switch = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[2]/div/form[2]/div[3]/div/div/span/button/span" #二线上游闸门打开时开关点击
#闸首内西
ship_2XXY_inside_weast_alarm = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[2]/div/form[3]/div[2]/div[2]/div/span/div/label[1]/span[1]/input" #二线上游闸门打开时报警级别选项
ship_2XXY_inside_weast_switch = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[2]/div/form[3]/div[3]/div/div/span/button/span" #二线上游闸门打开时开关点击
#上游保存
ship_2XXY_cb_saveButton = By.XPATH, "/html/body/div/section/section/main/div/div/div[3]/div/div[2]/div/div/div[2]/div/div/button" #二线上游闸门打开时报警级别选项



#历史告警模块
history_type = By.XPATH, "/html/body/div/section/section/main/div/form/div[1]/div[2]/div/span/div/div/div/div" #报警类型点击
history_type_lists_select = By.XPATH,"/html/body/div[2]/div/div/div/ul/li[1]" #报警类型列表选择
history_search_button = By.XPATH, "/html/body/div[1]/section/section/main/div/form/div[5]/div/div/span/button[1]" #历史告警查询按钮
history_reset_button = By.XPATH, "/html/body/div[1]/section/section/main/div/form/div[5]/div/div/span/button[2]"  #历史告警重置按钮
history_lists_view = By.XPATH, "/html/body/div/section/section/main/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[8]/div/button" #历史告警列表查看前后5分钟数据
history_lists_view_close = By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button" #历史告警前后5分钟数据框关闭

#系统设置
#系统设置模块-闸门tab
system_zm_tab = By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/form/div[1]/div[1]/div/div/div/div/div[1]/div[1]" #闸门tab
system_zm_close = By.XPATH,"/html/body/div/section/section/main/div/div/div/form/div[1]/div[3]/div[1]/div[3]/div[2]/div/span/div/div[2]/input" #闸门关闭精确角度值修改
system_zm_open_sure = By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/form/div[1]/div[3]/div[1]/div[4]/div[2]/div/span/div/div[2]/input"  #闸门确定打开值修改
system_zm_close_sure = By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/form/div[1]/div[3]/div[1]/div[5]/div[2]/div/span/div/div[2]/input"  #闸门确定关闭值修改
system_zm_small = By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/form/div[1]/div[3]/div[1]/div[6]/div[2]/div/span/div/div[2]/input"  #闸门角度变化最小值修改
system_zm_savebutton = By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/form/div[2]/div/div/span/button" #闸门保存按钮

#系统设置模块-其他tab
system_other_tab = By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/form/div[1]/div[1]/div/div/div/div/div[1]/div[3]"  #其他tab点击
system_other_reality = By.XPATH,    "/html/body/div[1]/section/section/main/div/div/div/form/div[1]/div[3]/div[3]/div[2]/div[2]/div/span/div/div[2]/input" #实时计算周期
system_other_open = By.XPATH,       "/html/body/div[1]/section/section/main/div/div/div/form/div[1]/div[3]/div[3]/div[3]/div[2]/div/span/div/div[2]/input" #可开闸门水位差修改
system_other_allopen = By.XPATH,    "/html/body/div[1]/section/section/main/div/div/div/form/div[1]/div[3]/div[3]/div[4]/div[2]/div/span/div/div[2]/input" #通闸允许水位差修改

system_other_num = By.XPATH,        "/html/body/div[1]/section/section/main/div/div/div/form/div[1]/div[3]/div[3]/div[5]/div[2]/div/span/div/div[2]/input" #可视为报警的连续异常数修改
system_other_placetozm = By.XPATH,  "/html/body/div[1]/section/section/main/div/div/div/form/div[1]/div[3]/div[3]/div[6]/div[2]/div/span/div/div[2]/input" #地面到闸底的距离修改
system_other_placetorxq = By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/form/div[1]/div[3]/div[3]/div[7]/div[2]/div/span/div/div[2]/input" #地面到人行桥的距离修改
system_other_Bridge_num = By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/form/div[1]/div[3]/div[3]/div[8]/div[2]/div/span/div/div[2]/input" #可通行的最小桥梁净空值修改
system_other_SYGC_num = By.XPATH,   "/html/body/div[1]/section/section/main/div/div/div/form/div[1]/div[3]/div[3]/div[9]/div[2]/div/span/div/div[2]/input" #上游高程值修改
system_other_XYGC_num = By.XPATH,   "/html/body/div[1]/section/section/main/div/div/div/form/div[1]/div[3]/div[3]/div[10]/div[2]/div/span/div/div[2]/input" #下游高程值修改
system_other_ZSGC_num = By.XPATH,   "/html/body/div[1]/section/section/main/div/div/div/form/div[1]/div[3]/div[3]/div[11]/div[2]/div/span/div/div[2]/input" #闸室高程值修改
system_other_Four_nums = By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/form/div[1]/div[3]/div[3]/div[12]/div[2]/div/span/div/div[1]/input" #从上游到下游传感器距底部距离值修改
system_other_savebutton = By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/form/div[2]/div/div/span/button" #保存按钮


#摄像头设置
camera_close = By.CSS_SELECTOR, "#root > section > section > main > div > div > div > div.ant-col.ant-col-20 > div > div:nth-child(1) > div > i > svg"  #将视频窗口关闭
camera_close_savebutton = By.XPATH, "/html/body/div[1]/section/section/main/div/div/button"  #视频删除保存
camera_update_windows_select = By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/div[2]/div/div[1]" #选择窗口新增视频
#camera_update_lists_select = By.XPATH, ""  #摄像头列表选择已被删除的摄像头
#camera_update_lists_select = By.CSS_SELECTOR, ""
camera_update_savebutton = By.XPATH, "/html/body/div[1]/section/section/main/div/div/button" #新增视频保存