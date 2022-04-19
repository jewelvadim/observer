from observer import Doorbell, Apartment


doorbell = Doorbell()

for i in range(5):
    apartment = Apartment(i)

    doorbell.attach(apartment)

doorbell.ring(1)
# 0: Not me!
# 1: Welcome
# 2: Not me!
# 3: Not me!
# 4: Not me!

doorbell.ring(5)
# 0: Not me!
# 1: Not me!
# 2: Not me!
# 3: Not me!
# 4: Not me!
