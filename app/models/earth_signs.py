from app.models.base_sign import BaseSign
class EarthSign(BaseSign):
    """Earth signs: Taurus, Virgo, Capricorn
    This is here to show what zodiac sign classes look like and will take on
    the shared properties of the BaseSign, but keeping it Earth-specific!"""
    element = "Earth"