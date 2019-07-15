import sys
import os

import pytest

sys.path.append(os.getcwd())
from tool.read_yaml import read_yaml
from page.page_in import PageIn
from tool.driver_util import DriverUtil


def get_data():
    result = read_yaml('address_data')
    list_data = []
    list_data.append(tuple(result.values()))
    return list_data


class TestAddress(object):
    # 初始化
    def setup_class(self):
        # 初始化地址管理对象
        self.page_address = PageIn().get_address_page()
        # 初始化登录模块对象
        self.page_login = PageIn().get_login_page()

    # 结束
    def teardown_class(self):
        DriverUtil.quit_driver()

    # 测试方法
    @pytest.mark.parametrize('recipt,tel,dict,detail,postcode', get_data())
    def test_post_address(self, recipt, tel, dict, detail, postcode):
        # 依赖登录模块进行登录操作
        self.page_login.address_login("17301392675", '123456')

        # 正向用例
        self.page_address.add_address(recipt, tel, dict, detail, postcode)
        # 断言


