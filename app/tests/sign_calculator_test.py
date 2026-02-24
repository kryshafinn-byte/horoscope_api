from app.utils.sign_calculator import SignCalculator
import pytest

# Mid-range dates for each sign (all 1999) to make sure the basics are working! 

def test_aries_mid():
    assert SignCalculator.from_string("1999-04-05") == "Aries"

def test_taurus_mid():
    assert SignCalculator.from_string("1999-05-10") == "Taurus"

def test_gemini_mid():
    assert SignCalculator.from_string("1999-06-10") == "Gemini"

def test_cancer_mid():
    assert SignCalculator.from_string("1999-07-10") == "Cancer"

def test_leo_mid():
    assert SignCalculator.from_string("1999-08-10") == "Leo"

def test_virgo_mid():
    assert SignCalculator.from_string("1999-09-10") == "Virgo"

def test_libra_mid():
    assert SignCalculator.from_string("1999-10-10") == "Libra"

def test_scorpio_mid():
    assert SignCalculator.from_string("1999-11-10") == "Scorpio"

def test_sagittarius_mid():
    assert SignCalculator.from_string("1999-12-10") == "Sagittarius"

def test_capricorn_mid():
    assert SignCalculator.from_string("1999-01-10") == "Capricorn"

def test_aquarius_mid():
    assert SignCalculator.from_string("1999-02-10") == "Aquarius"

def test_pisces_mid():
    assert SignCalculator.from_string("1999-03-10") == "Pisces"


# Boundary tests (all 1999 except Capricorn ends due to how it falls)
def test_aries_start():
    assert SignCalculator.from_string("1999-03-21") == "Aries"

def test_aries_end():
    assert SignCalculator.from_string("1999-04-19") == "Aries"

def test_capricorn_start():
    assert SignCalculator.from_string("1999-12-22") == "Capricorn"

def test_capricorn_end():
    assert SignCalculator.from_string("1999-01-19") == "Capricorn"

#Invalid inputs/dates not in the calendar or lack of info
def test_invalid_format():
    with pytest.raises(ValueError):
        SignCalculator.from_string("1999/12/25")

def test_impossible_date():
    with pytest.raises(ValueError):
        SignCalculator.from_string("1999-02-30")

def test_empty_string():
    with pytest.raises(ValueError):
        SignCalculator.from_string("")
