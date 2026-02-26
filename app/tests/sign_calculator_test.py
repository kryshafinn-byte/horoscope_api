from app.utils.sign_calculator import SignCalculator
import pytest
# WRONG INPUTS
def test_put_in_wrong():
    with pytest.raises(ValueError):
        SignCalculator.from_string("1999/12/25")
def test_date_is_wrong():
    # feb 30th wont be a date
    with pytest.raises(ValueError):
        SignCalculator.from_string("1999-02-30")
def test_empty_thing():
    # nothing in here so nothing will work
    with pytest.raises(ValueError):
        SignCalculator.from_string("")


# CUSPS or THE END
#do you believe in cusps?
def test_aries_start_cusp():
    print("checking Aries start cusp...")
    assert SignCalculator.from_string("1999-03-21") == "Aries"
def test_aries_end_cusp():
    print("checking Aries end cusp...")
    assert SignCalculator.from_string("1989-04-19") == "Aries"
def test_capricorn_start_cusp():
    print("checking Capricorn start cusp...")
    assert SignCalculator.from_string("1959-12-22") == "Capricorn"
def test_capricorn_end_cusp():
    print("checking Capricorn end cusp...")
    assert SignCalculator.from_string("1949-01-19") == "Capricorn"


# MID DATES
def test_aries_is_mid():
    print("mid Aries check")
    assert SignCalculator.from_string("1989-04-05") == "Aries"
def test_taurus_is_mid():
    print("mid Taurus check")
    assert SignCalculator.from_string("1979-05-10") == "Taurus"
def test_gemini_is_mid():
    print("mid Gemini check")
    assert SignCalculator.from_string("1909-06-10") == "Gemini"
def test_cancer_is_mid():
    print("mid Cancer check")
    assert SignCalculator.from_string("1919-07-10") == "Cancer"
def test_leo_is_mid():
    print("mid Leo check")
    assert SignCalculator.from_string("1929-08-10") == "Leo"
def test_virgo_is_mid():
    print("mid Virgo check")
    assert SignCalculator.from_string("1939-09-10") == "Virgo"
def test_libra_is_mid():
    print("mid Libra check")
    assert SignCalculator.from_string("1949-10-10") == "Libra"
def test_scorpio_is_mid():
    print("mid Scorpio check")
    assert SignCalculator.from_string("1959-11-10") == "Scorpio"
def test_sagittarius_is_mid():
    print("mid Sagittarius check")
    assert SignCalculator.from_string("1969-12-10") == "Sagittarius"
def test_capricorn_is_mid():
    print("mid Capricorn check")
    assert SignCalculator.from_string("1989-01-10") == "Capricorn"
def test_aquarius_is_mid():
    print("mid Aquarius check")
    assert SignCalculator.from_string("1999-02-10") == "Aquarius"
def test_pisces_is_mid():
    print("mid Pisces check")
    assert SignCalculator.from_string("1979-03-10") == "Pisces"