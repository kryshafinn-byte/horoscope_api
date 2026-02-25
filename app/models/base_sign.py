class BaseSign:
    """Base class for all zodiac signs
    It stores the name, the date range, and the element of the sign.
    It also puts it into a JSON format for the API to use.
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

