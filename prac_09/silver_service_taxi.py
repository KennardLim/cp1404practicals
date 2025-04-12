from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialized version of Taxi that includes flagfall and fanciness that affects rates."""
    flagfall = 4.50

    def __init__(self, name="", fuel=0, fanciness=1.0):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Taxi but with the flagfall cost"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:,.2f}"

    def get_fare(self):
        """Return the price for the taxi trip, also accounts for flagfall cost."""
        return super().get_fare() + self.flagfall
