import pytest

from pages.appointment_page import AppointmentPage
from pages.history_page import HistoryPage


@pytest.fixture
def login_history(setup_login):
    history_page = HistoryPage(setup_login)
    yield history_page
@pytest.mark.skip
def test_no_appointment(login_history):
    no_appointment_text = login_history.no_appointment()

    assert no_appointment_text == "No appointment."

def test_with_appointment(setup_login, page):
    appointment_page = AppointmentPage(setup_login)

    details = {
        "visit_date": "25/12/2026",
        "facility": "Seoul CURA Healthcare Center",
        "program": "None",
        "comment": "Appointment on 25/12/2026"
    }
    appointment_page.valid_appointment(
        details["facility"],
        details["visit_date"],
        details["comment"]
    )

    history_page = HistoryPage(page)
    history_page.click_menu()
    history_page.click_history()

    actual_values = dict(zip(["visit_date", "facility", "program", "comment"],
                             history_page.get_appointment_details(details["visit_date"])))

    for key in details:
        assert details[key] == actual_values[key]




