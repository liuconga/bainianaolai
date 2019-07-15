import allure

import page
from base.base_page import BasePage


class PageLogin(BasePage):
    # 初始化
    def __init__(self, driver):
        super().__init__(driver)

    # 点击我操作
    @allure.step(title="正在点击我")
    def click_me(self):
        # 获取首页包名和Activity名
        # print(self.driver.current_package)
        # print(self.driver.current_activity)
        self.base_click(page.my_btn)

    # 点击已有账号去登录
    @allure.step(title="点击已有账号去登录")
    def click_account_btn(self):
        self.base_click(page.account_btn)

    # 输入账号操作
    @allure.step(title="正在输入用户名")
    def input_username(self, username):
        allure.attach("用户名：", username)
        self.base_input_text(page.login_username, username)

    # 输入密码操作
    def input_password(self, password):
        allure.attach("密码：", password)
        self.base_input_text(page.login_password, password)

    # 点击登录操作
    @allure.step(title="正在点击登录按钮")
    def click_login_btn(self):
        self.base_click(page.login_btn)

    # 正向-获取登录后昵称操作
    @allure.step(title="正在获取登录后昵称")
    def get_nick_name(self):
        return self.base_get_text(page.nick_name)

    # 逆向-获取异常toast消息
    @allure.step(title="正在获取toast消息")
    def error_login_toast(self, msg):
        allure.attach("获取的登录信息为:", msg)
        self.base_get_toast(msg)

    # 点击设置
    @allure.step(title="正在点击设置")
    def click_setting(self):
        self.base_click(page.setting_btn)

    # 点击退出操作
    @allure.step(title="调用退出组合业务方法")
    def click_quit(self):
        # 拖拽元素信息
        self.base_drag_and_drop(page.start_loc, page.end_loc)
        # 点击退出按钮
        self.base_click(page.logout)
        # 点击退出操作

    # 点击确认退出
    @allure.step(title='正在点击确认退出操作')
    def click_quit_confirm(self):
        # 点击确认退出按钮
        self.base_click(page.logout_confirm)

    # 点击地址管理
    def click_address_message(self):
        # 点击确认退出按钮
        self.base_click(page.address_message)

    # 组合业务-登录 注意：一个页面的元素在进行组合
    @allure.step(title='正在进行组合登录操作')
    def login(self, username, password):
        # 输入账号
        self.input_username(username)
        # 输入密码
        self.input_password(password)
        # 点击登录
        self.click_login_btn()

    # 组合业务-点击已有账号去登录
    @allure.step(title='正在进行点击我和点击已有账户登录组合业务')
    def click_me_and_account(self):
        # 点击我
        self.click_me()
        # 点击以后账号登录
        self.click_account_btn()

    # 组合业务-退出登录
    @allure.step(title="正在进行退出-组合业务操作")
    def logout(self):
        # 点击我的
        self.click_me()
        # 点击设置
        self.click_setting()
        # 点击退出
        self.click_quit()
        # 点击确认退出
        self.click_quit_confirm()

    # 组合业务-地址管理依赖登录业务
    def address_login(self, username, password):
        # 点击我并点击已有账号登录
        self.click_me_and_account()
        # 组合业务-登录
        self.login(username, password)
        # 点击设置
        self.click_setting()
        # 点击地址管理
        self.click_address_message()
