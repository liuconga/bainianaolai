import pytest
import sys
import os
sys.path.append(os.getcwd())
from tool.read_yaml import read_yaml
from page.page_in import PageIn
from tool.driver_util import DriverUtil


def get_data():
    """登录测试数据"""
    result = read_yaml()
    data_list = []
    for data in result.values():
        data_list.append(tuple(data.values()))
    return data_list


class TestLogin(object):
    page_login = None

    # 初始化操作
    def setup_class(self):
        # 初始化page_login对象
        self.page_login = PageIn().get_login_page()
        # 点击我
        self.page_login.click_me()
        # 点击已有账户登录
        self.page_login.click_account_btn()

    # 结束操作
    def teardown_class(self):
        # 关闭driver对象
        DriverUtil().quit_driver()

    # 测试方法
    @pytest.mark.parametrize("username, password, expect_nickname, expect_toast", get_data())
    def test_login(self, username, password, expect_nickname, expect_toast):
        # 正向用例-登录
        self.page_login.login(username, password)
        if expect_nickname:
            try:
                # 断言：
                assert expect_nickname == self.page_login.get_nick_name()
            except Exception as e:
                # 错误截图
                self.page_login.get_error_screenshot()
                # 重新抛出异常
                raise e
            finally:
                # 退出登录
                self.page_login.logout()
                # 点击我的
                self.page_login.click_me()
                # 点击已有账户登录
                self.page_login.click_account_btn()
        # 逆向用例
        else:
            try:
                assert expect_toast in self.page_login.base_get_toast(expect_toast)
            except Exception as e:
                # 错误截图
                self.page_login.get_error_screenshot()
                # 重新抛出异常
                raise e
