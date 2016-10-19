# class to create players' ships
class Ship:
    SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
    ]

    
    def __init__(self, ship_type, size)
        self.ship_type = ship_type
        self.location = []
        self.size = size
