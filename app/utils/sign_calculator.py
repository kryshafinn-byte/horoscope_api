from datetime import datetime

class SignCalculator:
    """
    A class to calculate zodiac signs from the birthdates.
    """

    @staticmethod
    def from_string(date_str: str) -> str:
        """
        If you put in the date string to be '1999-12-31', a zodiac sign should be returned.
        If not, ValueError appears with a nice message if the date is invalid.
        """
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Seems like the stars have crossed and missed! Make sure that you are using the correct date format (YYYY-MM-DD)!")
        return SignCalculator.from_date(date_obj)

    @staticmethod
    def from_date(date_obj: datetime) -> str:
        """
        The class takes a datetime object and returns the zodiac sign
        as a string.
        """
        print("Seeing what sign your birthdate belongs to:", date_obj)
        month = date_obj.month
        day = date_obj.day

        if (month == 3 and day >= 21) or (month == 4 and day <= 19):
            return "Aries"
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            return "Taurus"
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            return "Gemini"
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            return "Cancer"
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            return "Leo"
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            return "Virgo"
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            return "Libra"
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            return "Scorpio"
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            return "Sagittarius"
        elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
            return "Capricorn"
        elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
            return "Aquarius"
        elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
            return "Pisces"

        print("Error: The stars have not aligned with your birthdate, so we cannot find your sign.")
        raise ValueError("I couldn't work out your sign — you must have been born on a day when the stars were crossing and missed!")
