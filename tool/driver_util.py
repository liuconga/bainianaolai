import allure
from appium import webdriver


class DriverUtil(object):
    driver = None

    @classmethod
    @allure.step(title="正在初始化driver对象")
    def get_driver(cls):
        if cls.driver is None:
            # 初始化driver
            desired_caps = {}
            # 必填参数，且一定要正确，Android中a不区分大小写
            desired_caps['platformName'] = 'Android'
            # 可以不填，但是要填就要填正确，跟模拟器一样或跟手机一样
            desired_caps['platformVerison'] = '5.1'
            # Android中可以填错，但不可以为空
            desired_caps['deviceName'] = '192.168.56.102:5555'
            # 为了获取toast添加uiautomator2的库
            desired_caps['automationName'] = 'Uiautomator2'
            # 解决send_keys()输入中文问题
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True
            # 是否重置应用
            # desired_caps['noRest'] =True
            # app包名
            desired_caps['appPackage'] = 'com.yunmall.lc'
            # app启动名
            desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
            cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
        return cls.driver

    @classmethod
    @allure.step(title="正在关闭driver对象")
    def quit_driver(cls):
        if cls.driver is not None:
            cls.driver.quit()
            # 置空
            cls.driver = None

