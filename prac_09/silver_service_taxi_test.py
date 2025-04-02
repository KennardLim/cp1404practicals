from silver_service_taxi import SilverServiceTaxi

fancy_taxi = SilverServiceTaxi("The Shining Chariot", 100, 2.0)
print(f"\n{fancy_taxi}")

print(f"{fancy_taxi.name} drove {fancy_taxi.drive(18)}km")
assert fancy_taxi.get_fare() == 48.8, "Should be $48.8"
print(f"{fancy_taxi.get_fare():,.2f}")

president_taxi = SilverServiceTaxi("Presidential carrier", 105, 4.0)
print(f"\n{president_taxi}")

print(f"{president_taxi.name} drove {president_taxi.drive(30)}km")
assert president_taxi.get_fare() == 152.10, "Should be $152.10"
print(f"{president_taxi.get_fare():,.2f}")
