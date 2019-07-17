import page
from base.base_page import BasePage


class PageAddress(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # 点击新增地址
    def page_add_new_address(self):
        self.base_click(page.add_new_address)

    # 输入收件人姓名
    def page_input_recipients_name(self, receipt):
        self.base_input_text(page.receipt_name, receipt)

    # 输入手机号
    def page_input_tel(self, tel):
        self.base_input_text(page.add_phone, tel)

    # 输入所在地区
    def page_select_area(self, dict={"province": '广东省', "city": '广州市', "district": '天河区'}):
        # 点击所在区域
        self.base_click(page.address_province)
        # 选择省/直辖市
        self.base_text_click(dict['province'])
        # 选择地级市/区
        self.base_text_click(dict['city'])
        # 选择区/县级市
        self.base_text_click(dict['district'])
        pass

    # 输入详细地址
    def page_input_detail_address(self, text):
        self.base_input_text(page.address_info, text)

    # 输入邮编
    def page_input_postcode(self, text):
        self.base_input_text(page.address_post_code, text)

    # 点击设为默认地址
    def page_default_address(self):
        self.base_click(page.address_default)

    # 点击保存
    def page_save(self):
        self.base_click(page.save_btn)
    # 组合业务方法
    def add_address(self, recepit, tel, dict, detail, postcode):
        # 点击新增
        self.page_add_new_address()
        # 输入收件人姓名
        self.page_input_recipients_name(recepit)
        # 输入收件人电话
        self.page_input_tel(tel)
        # 点击输入所在地区
        self.page_select_area(dict)
        # 输入详细地址
        self.page_input_detail_address(detail)
        # 输入邮编
        self.page_input_postcode(postcode)
        # 设为默认地址
        self.page_default_address()
        # 点击保存
        self.page_save()

    # 获取收件人手机号+姓名
    def get_address_list(self):
        # elements = self.base_find_elements(page.address_assert_info)
        # address_list = []
        # for element in elements:
        #     address_list.append(element.text)
        # return address_list
        # 以下为通过行内循环式也叫列表推导式
        return [element.text for element in self.base_find_elements(page.address_assert_info)]
    # 获取收件人地址列表
    def get_address_detail_list(self):
        # elements = self.base_find_elements(page.address_assert_info)
        # address_list = []
        # for element in elements:
        #     address_list.append(element.text)
        # return address_list
        # 以下为通过行内循环式也叫列表推导式
        return [element.text for element in self.base_find_elements(page.address_assert)]