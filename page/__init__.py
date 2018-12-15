from selenium.webdriver.common.by import By

lg_tel = By.ID,"username"
lg_pwd = By.ID,"password"
lg_yzm = By.ID,"verify_code"
lg_dl = By.CLASS_NAME,"J-login-submit"



lg_sy = By.LINK_TEXT,"首页"
lg_search = By.ID,"q"
lg_click_search = By.CLASS_NAME,"ecsc-search-button"
lg_add = By.LINK_TEXT,"加入购物车"
lg_color = By.ID,"goods_spec_a_56"
lg_join_cart = By.ID,"join_cart"
lg_go_buy = By.XPATH,'//a[contains(text(),"去购物车结算")]'
lg_js = By.CLASS_NAME,"gwc-qjs"