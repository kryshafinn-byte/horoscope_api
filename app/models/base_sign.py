class BaseSign:
    """
    The base class for every zodiac sign.
    It holds the name, the date range, and the element.
    I have this so that I don't need to keep on writing code for all 12 signs and it can just be nice and simple.
    """
    def __init__(self, name, date_range, element):
        self.name = name
        self.date_range = date_range
        self.element = element

    def as_json(self):
        return {
            "name": self.name,
            "date_range": self.date_range,
            "element": self.element
        }