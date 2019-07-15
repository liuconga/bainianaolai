from page.page_in import PageIn
from tool.driver_util import DriverUtil


class TestAddress(object):
    # 初始化
    def setup_class(self):
        # 初始化地址管理对象
        self.page_address = PageIn().get_address_page()
        # 初始化登录模块对象
        self.page_login = PageIn.get_login_page()

    # 结束
    def teardown_class(self):
        DriverUtil.quit_driver()

    # 测试方法
    def test_post_address(self):
        self.page_login.address_login("17301392675", '123456')

        dict = {"province": '广东省', "city": '广州市', "district": '天河区'}
        # 正向用例
        self.page_address.add_address('currya', "18301225040", dict, '国风美唐', '052360')
        # 断言
    # 逆向用例
    # 断言