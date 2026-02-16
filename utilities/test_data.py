

base_url = 'https://katalon-demo-cura.herokuapp.com/'
credentials = {
    "valid_username": "John Doe",
    "valid_password": "ThisIsNotAPassword",
    "invalid_username": "John",
    "invalid_password": "ThisIsNot"
}
class login:
    make_appointment = "#btn-make-appointment"
    username = "#txt-username"
    password = "#txt-password"
    login_btn = "#btn-login"
    alert_message = ".lead.text-danger"

class appointment:
    facility = "#combo_facility"
    readmission = "#chk_hospotal_readmission"
    none = "#radio_program_none"
    visit_date = "#txt_visit_date"
    comment = "#txt_comment"
    book_appointment = "#btn-book-appointment"

class appointment_summary:
    facility = "#facility"
    readmission = "#hospital_readmission"
    program = "#program"
    visit_date = "#visit_date"
    comment = "#comment"

class menu:
    menu_toggle = "#menu-toggle"
    history = "a[href='history.php#history']"

class history:
    no_appointment = "div[class='col-sm-12 text-center'] p"
    visit_date = ".panel-heading"


