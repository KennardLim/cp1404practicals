from prac_09.unreliable_car import UnreliableCar

NUMBER_OF_DRIVES = 100

bad_car = UnreliableCar("Ol' Unreliable", 100, 30)
successful_drive_count = 0

for i in range(NUMBER_OF_DRIVES):
    bad_car.fuel = 100
    bad_car.drive(30)
    if bad_car.fuel < 100:
        successful_drive_count += 1

successful_drive_percent = successful_drive_count / NUMBER_OF_DRIVES * 100
print(f"{bad_car.name} successfully drove {successful_drive_percent:.0f}% of the drives!")