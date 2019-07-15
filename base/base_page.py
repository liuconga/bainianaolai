from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    # 1.初始化
    def __init__(self, driver):
        self.driver = driver

    # 2.封装查找方法
    def base_find(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 3.封装输入文本方法
    def base_input_text(self, loc, text):
        el = self.base_find(loc)
        el.clear()
        el.send_keys(text)

    # 4.封装点击方法
    def base_click(self, loc):
        self.base_find(loc).click()

    def base_get_text(self, loc):
        return self.base_find(loc).text

    # 5.封装获取toast信息方法
    def base_get_toast(self, msg):
        # 获取toast定位的方法
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(msg)
        # 因为toast时间短暂，要更改刷新频率为0.2
        return self.base_find(loc, poll=0.2).text

    # 错误截图方法
    def get_error_screenshot(self):
        self.driver.get_screenshot_as_file('./image/fail.png')

    # 封装拖拽方法
    def base_drag_and_drop(self, start_loc, end_loc):
        start_el = self.base_find(start_loc)
        end_el = self.base_find(end_loc)
        self.driver.scroll(start_el, end_el)
