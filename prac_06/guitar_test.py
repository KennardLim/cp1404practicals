from prac_06.guitar import Guitar

guitar_old = Guitar("Ol-reliable", 1925, 5000)
guitar_mid = Guitar("Steely wire", 2020, 3200)
guitar_new = Guitar("BTR special edition", 2024, 5600)

# First run
print(guitar_old.get_age()) #Expected 100. Got -100
print(guitar_old.is_vintage()) #Expected True. Got False
print(guitar_mid.get_age()) #Expected 5. Got -5
print(guitar_mid.is_vintage()) #Expected False. Got False
print(guitar_new.get_age()) #Expected 1. Got -1
print(guitar_new.is_vintage()) #Expected False. Got False

# Second run
print(guitar_old.get_age()) #Expected 100. Got 100
print(guitar_old.is_vintage()) #Expected True. Got True
print(guitar_mid.get_age()) #Expected 5. Got 5
print(guitar_mid.is_vintage()) #Expected False. Got False
print(guitar_new.get_age()) #Expected 1. Got 1
print(guitar_new.is_vintage()) #Expected False. Got False