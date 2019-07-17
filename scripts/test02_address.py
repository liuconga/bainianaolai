import sys
import os

import pytest

sys.path.append(os.getcwd())
from tool.read_yaml import read_yaml
from page.page_in import PageIn
from tool.driver_util import DriverUtil


def get_data():
    result = read_yaml('address_data')
    #通过列表推导式生成列表
    data_list = [tuple(data.values()) for data in result.values()]
    return data_list


class TestAddress(object):
    # 初始化
    def setup_class(self):
        # 初始化地址管理对象
        self.page_address = PageIn().get_address_page()
        # 初始化登录模块对象
        self.page_login = PageIn().get_login_page()
        self.page_login.address_login("17301392675", '123456')

    # 结束
    def teardown_class(self):
        DriverUtil.quit_driver()

    # 测试方法
    @pytest.mark.parametrize('recipt,tel,dict,detail,postcode,expect', get_data())
    def test_post_address(self, recipt, tel, dict, detail, postcode, expect):
        # 依赖登录模块进行登录操作

        print(dict)
        # 正向用例
        self.page_address.add_address(recipt, tel, dict, detail, postcode)
        # 断言收件人地址列表收件人姓名+手机号是否正确
        # 获取收集人地址列表手人间姓名+手机号
        # print(self.page_address.get_address_list())
        try:
            #断言姓名+手机号
            assert expect in self.page_address.get_address_list()
            #断言地址
            address=dict['province']+dict['city']+dict['district']+detail
            print(address)
            assert address in self.page_address.get_address_detail_list()
        except Exception as e:
            # 错误截图并提交到allure报告
            self.page_address.get_error_screenshot()
            raise e
