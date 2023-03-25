class VenueInfo:

    def __init__(self, venue_name: str, street_address: str, city: str, state: str, postal_code: int):
        self.state = state
        self.venue_name = venue_name
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return str(self.__dict__)

    @property
    def full_address(self):
        return f'{self.venue_name} {self.street_address} {self.city}'
