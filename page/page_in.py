import allure

from page.page_address import PageAddress
from page.page_login import PageLogin
from tool.driver_util import DriverUtil


# page对象入口类
class PageIn(object):
    def __init__(self):
        self.driver = DriverUtil.get_driver()

    @allure.step(title="正在获取PageLogin对象")
    def get_login_page(self):
        """获取登录模块page对象"""
        return PageLogin(self.driver)

    def get_address_page(self):
        """获取地址管理模块page对象"""
        return PageAddress(self.driver)
