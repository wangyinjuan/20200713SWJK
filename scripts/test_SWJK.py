import unittest
import pytest
import allure
import time
#import operations
from operations.operations_swjk_manager.swjk_manager import Testswjkmanager
from eles.get_driver import GetDriver

class TestSWJKManager(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.sw = Testswjkmanager(cls.driver)
        cls.sw.system_login()


    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    @allure.step(title="水文监控管理下的历史数据模块的查询功能")
    @pytest.mark.run(order=1)
    def test_sw_1history(self):
        #self.sw.eles_click(operations.hydrology_history_tab)
        self.sw.hydrology_manager_history_search()
        time.sleep(1)

    #@allure.step(title="水文监控管理下的历史数据模块的重置功能")
    @pytest.mark.run(order=2)
    def test_sw_2history_reset(self):
        self.sw.hydrology_manager_history_reset()
        time.sleep(1)

    # @allure.step(title="水文监控管理下的阈值设定功能")
    # @pytest.mark.run(order=3)
    # def test_sw_3threholdset(self):
    #     self.sw.eles_click(operations.hydrology_threholdset_tab)
    #     self.sw.hydrology_manager_threholdset()
    #     time.sleep(1)

if __name__ == '__main__':
    pytest.main()
