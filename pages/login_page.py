from utilities import test_data


class LoginPage:
    def __init__(self,page):
        self.page = page

    def navigate_to(self):
        self.page.goto(test_data.base_url)

    def click_make_appointment(self):
        self.page.click(test_data.login.make_appointment)

    def input_username_password(self, username, password):
        self.page.fill(test_data.login.username, username)
        self.page.fill(test_data.login.password, password)

    def click_login_btn(self):
        self.page.click(test_data.login.login_btn)

    def login(self, username, password):
        self.click_make_appointment()
        self.input_username_password(username,
                                     password)
        self.click_login_btn()

    def get_alert_message(self):
        return self.page.text_content(test_data.login.alert_message)

