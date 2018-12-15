import page
from base.base import Base


class PageLogin(Base):
    def page_input_tel(self,tel):
        self.base_input(page.lg_tel,tel)

    def page_input_pwd(self,pwd):
        self.base_input(page.lg_pwd,pwd)


    def page_input_code(self,yzm):
        self.base_input(page.lg_yzm,yzm)


    def page_click_signin(self):
        self.base_click_btn(page.lg_dl)