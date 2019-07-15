from page.page_login import PageLogin
from tool.driver_util import DriverUtil


# page对象入口类
class PageIn(object):
    def __init__(self):
        self.driver = DriverUtil.get_driver()

    def get_login_page(self):
        return PageLogin(self.driver)
