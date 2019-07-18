"""以下为登录模块配置数据"""
from selenium.webdriver.common.by import By

my_btn = By.ID, 'com.yunmall.lc:id/tab_me'
account_btn = By.ID, 'com.yunmall.lc:id/textView1'
login_username = By.ID, 'com.yunmall.lc:id/logon_account_textview'
login_password = By.ID, 'com.yunmall.lc:id/logon_password_textview'
login_btn = By.ID, 'com.yunmall.lc:id/logon_button'
nick_name = By.ID, 'com.yunmall.lc:id/tv_user_nikename'

setting_btn = By.ID, 'com.yunmall.lc:id/ymtitlebar_left_btn_image'

end_loc = By.ID, 'com.yunmall.lc:id/setting_modify_pwd'
start_loc = By.ID, 'com.yunmall.lc:id/setting_clear_cache'
logout = By.ID, 'com.yunmall.lc:id/setting_logout'
logout_confirm = By.ID, 'com.yunmall.lc:id/ymdialog_right_button'
# 地址管理
address_message = By.ID, 'com.yunmall.lc:id/setting_address_manage'
area_title=By.ID,"com.yunmall.lc:id/area_title"

"""以下数据为地址管理模块配置数据"""
add_new_address = By.ID, 'com.yunmall.lc:id/address_add_new_btn'
receipt_name = By.ID, 'com.yunmall.lc:id/address_receipt_name'
add_phone = By.ID, 'com.yunmall.lc:id/address_add_phone'
address_province = By.ID, 'com.yunmall.lc:id/address_province'
address_info = By.ID, 'com.yunmall.lc:id/address_detail_addr_info'
address_post_code = By.ID, 'com.yunmall.lc:id/address_post_code'
address_default = By.ID, 'com.yunmall.lc:id/address_default'
save_btn = By.ID, 'com.yunmall.lc:id/button_send'
address_assert_info = By.ID, 'com.yunmall.lc:id/receipt_name'
address_assert = By.ID, 'com.yunmall.lc:id/receipt_address'
address_edit_btn=By.ID,'com.yunmall.lc:id/ymtitlebar_right_btn'
address_update=By.ID,'com.yunmall.lc:id/modify'
address_delete=By.ID,'com.yunmall.lc:id/delete'
address_delete=By.ID,'com.yunmall.lc:id/delete'
address_delete_confirm=By.ID,'com.yunmall.lc:id/ymdialog_left_button'


