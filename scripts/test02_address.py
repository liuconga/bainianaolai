import sys
import os

import pytest

sys.path.append(os.getcwd())
from tool.read_yaml import read_yaml
from page.page_in import PageIn
from tool.driver_util import DriverUtil


def get_data(text):
    data_list = []
    if text == 'post':
        result = read_yaml('address_data')
        # 通过列表推导式生成列表
        data_list = [tuple(data.values()) for data in result.values()]
    elif text == 'update':
        data_list = [("kawayi", '16301335675', {'province': '河北省', 'city': '石家庄市', 'district': '新华区'},
                      'HELLOOSS', '052360', 'kawayi  16301335675')]

    return data_list


def upadate_date():
    return [("kawayi", '16301335675', {'province': '广东省', 'city': '广州市', 'district': '天河区'},
             'HELLOOSS', '052360', 'kawayi  16301335675')]


class TestAddress(object):
    # 初始化
    def setup_class(self):
        # 初始化地址管理对象
        self.page_address = PageIn().get_address_page()
        # 初始化登录模块对象
        self.page_login = PageIn().get_login_page()
        # 登录操作
        self.page_login.address_login("17301392675", '123456')

    # 结束
    def teardown_class(self):
        DriverUtil.quit_driver()

    # 测试新增方法
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('recipt,tel,dict,detail,postcode,expect', get_data('post'))
    def test_post_address(self, recipt, tel, dict, detail, postcode, expect):

        # 正向用例
        self.page_address.add_address(recipt, tel, dict, detail, postcode)
        # 断言收件人地址列表收件人姓名+手机号是否正确
        # 获取收集人地址列表手人间姓名+手机号
        # print(self.page_address.get_address_list())
        try:
            # 断言姓名+手机号
            assert expect in self.page_address.get_address_list()
            # 断言地址
            address = dict['province'] + dict['city'] + dict['district'] + detail
            print(address)
            assert address in self.page_address.get_address_detail_list()
        except Exception as e:
            # 错误截图并提交到allure报告
            self.page_address.get_error_screenshot()
            raise e

    # 测试新增方法
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('recipt,tel,dict,detail,postcode,expect', get_data('update'))
    def test_upadate_address(self, recipt, tel, dict, detail, postcode, expect):

        # 更新地址
        self.page_address.upadate_address(recipt, tel, dict, detail, postcode)
        try:
            # 断言toast
            assert '保存成功' == self.page_address.base_get_toast('保存成功')
            # 断言姓名+手机号
            assert expect in self.page_address.get_address_list()
            # 断言地址
            address = dict['province'] + dict['city'] + dict['district'] + detail
            # print(address)
            assert address in self.page_address.get_address_detail_list()
        except Exception as e:
            # 错误截图并提交到allure报告
            self.page_address.get_error_screenshot()
            raise e

        # 测试删除方法
    @pytest.mark.run(order=3)
    def test_delete_address(self):
        # 先得查询地址列表
        # 删除地址
        if not self.page_address.page_exsits_address():
            self.page_address.delete_address()
        # 断言删除是否成功
        assert self.page_address.page_exsits_address()
