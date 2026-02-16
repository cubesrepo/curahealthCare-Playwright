from utilities import test_data


class HistoryPage:
    def __init__(self, page):
        self.page = page

    def click_menu(self):
        self.page.click(test_data.menu.menu_toggle)

    def click_history(self):
        self.page.click(test_data.menu.history)

    def no_appointment(self):
        self.click_menu()
        self.click_history()

        no_appointment_text = self.page.locator(test_data.history.no_appointment).text_content()

        return no_appointment_text.strip()

    def get_appointment_details(self, visit_date):
        locators = ["facility", "program", "comment"]
        history_details = [visit_date]
        for locator in locators:
            element = self.page.locator(getattr(test_data.appointment_summary, locator))
            history_details.append(element.text_content().strip())
        return history_details
