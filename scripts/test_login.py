import os
import sys
sys.path.append(os.getcwd())
import pytest

from base.read_yaml import ReadYaml
from base.get_driver import get_driver
from page.page_login import PageLogin



def get_data():
    arrs = []
    for data in ReadYaml("data_login_01.yaml").read_yaml().values():
        arrs.append((data.get("tel"),data.get("pwd"),data.get("yzm")))
    return arrs


class TestLogin():
    def setup_class(self):
        self.test = PageLogin(get_driver())

    def teardown_class(self):
        self.test.driver.quit()


    @pytest.mark.parametrize("tel,pwd,yzm",get_data())
    def test_login(self,tel,pwd,yzm):
        self.test.page_input_tel(tel)
        self.test.page_input_pwd(pwd)
        self.test.page_input_code(yzm)
        self.test.page_click_signin()

