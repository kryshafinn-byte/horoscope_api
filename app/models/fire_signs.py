from app.models.base_sign import BaseSign
class FireSign(BaseSign):
    """Fire signs: Aries, Leo, Sagittarius
    This is here to show what zodiac sign classes look like and will take on
    the shared properties of the BaseSign, but keeping it Fire-specific!"""
    element = "Fire"
