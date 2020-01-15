import datetime


class Building:
    def __init__(self, address, stories):
        self.designer = "Ben Koyd"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.datetime.now().strftime("%-m/%-d/%Y")

    def purchase(self, new_owner):
        self.owner = new_owner
