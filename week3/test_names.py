from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Manleh","Castillo") == "Castillo;Manleh"

def test_extract_family_name():
    full_name = make_full_name("Manleh","Castillo")
    family_name = extract_family_name(full_name)
    assert family_name == "Castillo"

def test_extract_given_name():
    full_name = make_full_name("Manleh","Castillo")
    given_name = extract_given_name(full_name)
    assert given_name == "Manleh"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])