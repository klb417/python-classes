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


eight_hundred_eighth = Building("800 8th Street", 12)
umpire_state_building = Building("23 Umpire Blvd", 40)
central_town_hall = Building("123 Main Ave", 3)
batman_building = Building("400 Gotham Drive", 50)
that_building = Building("45023 Madeup Pkwy", 8)

eight_hundred_eighth.purchase("Monopoly Guy")
umpire_state_building.purchase("Jane Mogul")
central_town_hall.purchase("Richie Rich")
batman_building.purchase("Trust Fund Baby")
that_building.purchase("Bucky Dollarroo")

eight_hundred_eighth.construct()
umpire_state_building.construct()
central_town_hall.construct()
batman_building.construct()
that_building.construct()

building_list = [
    eight_hundred_eighth,
    umpire_state_building,
    central_town_hall,
    batman_building,
    that_building,
]

for building in building_list:
    print(
        f"{building.address} was purchased by {building.owner} on {building.date_constructed} and has {building.stories} stories."
    )

