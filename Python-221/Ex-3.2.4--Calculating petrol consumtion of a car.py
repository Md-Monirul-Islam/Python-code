PETROL_PRICE_PER_LITIRE = 4.50
print("*** Welcome to the fuel efficiency calculation! ***")
name = input("Enter your name :")
DISTANCE_TRAVELLED = float(input("Enter distance travellde in km: "))
AMOUNT_PAID = float(input("Enter monetary value of the fuel bought for the trip: R"))
fuel_consume = AMOUNT_PAID/PETROL_PRICE_PER_LITIRE
efficiency_1_per_100_km = fuel_consume/DISTANCE_TRAVELLED*100
efficiency_km_per_1 = DISTANCE_TRAVELLED/fuel_consume
print("Hi ! ",name)
print("your car's efficiency is %.2f litire per 100 km.",efficiency_1_per_100_km)
print("this means that you can travel %.2f km on a litire of petrol.",efficiency_km_per_1)
print("\n Thanks using tha program.")