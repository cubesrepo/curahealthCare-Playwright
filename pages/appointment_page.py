
from utilities import test_data


class AppointmentPage:
    def __init__(self, page):
        self.page = page
    def click_facility(self):
        self.page.click(test_data.appointment.facility)
    def click_none(self):
        self.page.click(test_data.appointment.none)

    def fill_visit_date(self, visit_date, retries=2):
        for attempts in range(retries):
            self.page.locator(test_data.appointment.visit_date).type(visit_date)
            value = self.page.input_value(test_data.appointment.visit_date)
            if value.strip() == visit_date:
                return
        raise Exception(f"Failed to field visit date")


    def valid_appointment(self, facility, visit_date, comment, readmission=True):
        self.page.select_option(test_data.appointment.facility, facility)

        if readmission:
            self.page.check(test_data.appointment.readmission)

        self.page.click(test_data.appointment.none)
        self.fill_visit_date(visit_date)
        self.page.fill(test_data.appointment.comment, comment)
        self.page.click(test_data.appointment.book_appointment)

    def get_summary_details(self):
        details = []
        locators = ["facility", "readmission", "program", "visit_date", "comment"]
        for field in locators:
            value = self.page.locator(getattr(test_data.appointment_summary, field))
            details.append(value.text_content().strip())

        return details

    def appointment_without_visit_date(self, facility, comment, readmission=True):
        self.page.select_option(test_data.appointment.facility, facility)

        if readmission:
            self.page.check(test_data.appointment.readmission)

        self.page.click(test_data.appointment.none)
        self.page.fill(test_data.appointment.comment, comment)
        self.page.click(test_data.appointment.book_appointment)

