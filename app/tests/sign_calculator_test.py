from datetime import datetime
from app.utils.sign_calculator import SignCalculator
import pytest

def test_correct_sign():
    assert SignCalculator.from_string("1999-01-13") == "Capricorn"

def test_start_of_zodiac_sign():
    assert SignCalculator.from_string("2001-03-21") == "Aries"

def test_end_of_zodiac_sign():
    assert SignCalculator.from_string("2001-04-19") == "Aries"

def test_wrong_date_structure():
    with pytest.raises(ValueError):
        SignCalculator.from_string("2001-13-45")
    
    def test_wrong_date():
        with pytest.raises(ValueError):
            SignCalculator.from_string("2001/12/25")