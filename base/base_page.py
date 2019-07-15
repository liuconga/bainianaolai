import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    # 1.初始化
    @allure.step(title="正在初始化driver")
    def __init__(self, driver):
        self.driver = driver

    # 2.封装查找方法
    @allure.step(title="正在查找元素")
    def base_find(self, loc, timeout=30, poll=0.5):
        allure.attach("查找的元素".format(loc), "")
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 3.封装输入文本方法
    @allure.step(title="正在输入操作")
    def base_input_text(self, loc, text):
        allure.attach("给{}元素输入:{}值".format(loc, text), "")
        el = self.base_find(loc)
        el.clear()
        el.send_keys(text)

    # 4.封装点击方法
    @allure.step(title="正在点击操作")
    def base_click(self, loc):
        allure.attach("正在点击元素{}".format(loc), "")
        self.base_find(loc).click()

    @allure.step(title="正在获取元素文本操作")
    def base_get_text(self, loc):
        allure.attach("获取元素{}的文本".format(loc), "")
        return self.base_find(loc).text

    # 5.封装获取toast信息方法
    @allure.step(title='正在获取toast信息')
    def base_get_toast(self, msg):
        # 获取toast定位的方法
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(msg)
        # 因为toast时间短暂，要更改刷新频率为0.2,超时时间弄成2s
        return self.base_find(loc, timeout=2, poll=0.2).text

    # 错误截图方法并将错误截图写入到allure报告
    @allure.step(title='正在进行错误截图')
    def get_error_screenshot(self):
        self.driver.get_screenshot_as_file('./image/fail.png')
        # 将错误截图写入报告，封装到错误截图方法中
        self.error_screenshot_allurereport()

    # 错误截图写入到allure报告
    @allure.step(title='正在将截图写入allure报告')
    def error_screenshot_allurereport(self, title="断言失败原因:"):
        # 将错误截图写入到报告
        with open('./image/fail.png', 'rb')as f:
            allure.attach(title, f.read(), allure.attach_type.PNG)

    # 封装拖拽方法
    @allure.step(title='正在进行拖拽操作')
    def base_drag_and_drop(self, start_loc, end_loc):
        allure.attach("正从元素{}拖拽到{}".format(start_loc, end_loc), "")
        start_el = self.base_find(start_loc)
        end_el = self.base_find(end_loc)
        self.driver.scroll(start_el, end_el)

    # 根据文本获取元素并点击
    @allure.step(title='正在进行通过文本获取元素并点击操作')
    def base_text_click(self, text):
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(text)
        self.base_click(loc)
