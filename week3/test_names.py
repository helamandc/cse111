from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Manleh","Castillo") == "Castillo;Manleh"
    assert make_full_name("Eva","Castillo-Guatno") == "Castillo-Guatno;Eva"
    assert make_full_name("J","Li") == "Li;J"
    assert make_full_name("","") == ";"

def test_extract_family_name():
    assert extract_family_name("Castillo;Manleh") == "Castillo"
    assert extract_family_name("Castillo-Guatno;Eva") == "Castillo-Guatno"
    assert extract_family_name("Li;J") == "Li"
    assert extract_family_name(";") == ""

def test_extract_given_name():
    assert extract_given_name("Castillo;Manleh") == "Manleh"
    assert extract_given_name("Castillo-Guatno;Eva") == "Eva"
    assert extract_given_name("Li;J") == "J"
    assert extract_given_name(";") == ""

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])