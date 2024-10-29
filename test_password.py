from password import generate_password, password_change, password_storage
import pytest
from datetime import datetime, timedelta

current_date = datetime.now()

def test_generate_password():
    password = generate_password("test","123456")
    assert password[0] == "T" #at least 1 uppercase
    assert len(password) > 8 #at least 8 characters
    assert " " not in password #no spaces in between
    assert any(char.isdigit() for char in password) #at least 1 number
    special_char_list = ["@", "$", "#", "%", "?", "!"] #at least 1 special character
    assert any(char in special_char_list for char in password) #

def test_password_change():
    update_date = current_date + timedelta(days=90)
    new_pw = password_change(current_date)
    assert new_pw == update_date

def test_password_storage():
    assert password_storage("M@nl3h!123456", current_date) == "password-storage.txt"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])