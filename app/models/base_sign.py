class BaseSign:
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

