import pytest
from playwright.sync_api import expect

from pages.appointment_page import AppointmentPage
from utilities import test_data


@pytest.fixture
def login(setup_login):
    appointment_page = AppointmentPage(setup_login)
    yield appointment_page

def test_valid_appointment(login):

    expected_values = {
        "facility": "Seoul CURA Healthcare Center",
        "readmission": "Yes",
        "program": "None",
        "visit_date": "25/03/2026",
        "comment": "Appointment on 25/03/2026"
    }
    login.valid_appointment(
        expected_values["facility"],
        expected_values["visit_date"],
        expected_values["comment"]
    )

    expect(login.page).to_have_url("https://katalon-demo-cura.herokuapp.com/appointment.php#summary")

    actual_values = dict(zip(["facility", "readmission", "program", "visit_date", "comment"],
                             login.get_summary_details()))

    for key in expected_values:
        assert expected_values[key] == actual_values[key]

def test_appointment_without_visit_date(login):

    facility = "Seoul CURA Healthcare Center"
    comment = "Appointment on 25/03/2026"

    login.appointment_without_visit_date(
        facility,
        comment
    )

    validation_message = login.page.eval_on_selector(
        test_data.appointment.visit_date, "el => el.validationMessage"
    )

    assert validation_message.strip() == "Please fill out this field."

