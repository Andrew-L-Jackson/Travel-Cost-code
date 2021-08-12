country = input("What country will you be traveling to? ")
arrival_city = input("What city will you be flying in and out of? ")
number_of_locations =  int(input("How many locations will you be traveling to on this trip? "))
days = int(input("How many days will you be staying? "))
travelers = int(input("How many people will be coming on this trip? "))
form_of_short_trans = input("Will you be traveling via taxi or rental? ")
foreign_currency = days * 50 * travelers
rental_insurance = 1.12
hotel_cost = 150 * days
rental_car_cost = days * 100 * rental_insurance
Train_1 = 150
Train_2 = 50
Train_3 = 120


if arrival_city.lower() == "Berlin":
    plane_cost = 340 * 2 * travelers

elif arrival_city.lower() == "Frankfurt":
    plane_cost = 350 * 2 * travelers

elif arrival_city.lower() == "Munich":
    plane_cost = 360 * 2 * travelers


train_cost = (Train_1 + Train_2 + Train_3) * travelers


if form_of_short_trans == "taxi":
    short_trans_cost = 75 * (days - number_of_locations)

if form_of_short_trans == "rental":
    short_trans_cost = rental_car_cost
    Train_1 = 0
    Train_2 = 0
    Train_3 = 0
elif travelers > 3 and form_of_short_trans == "rental":
    short_trans_cost = rental_car_cost * 1.3
    Train_1 = 0
    Train_2 = 0
    Train_3 = 0


trip_cost = round(hotel_cost + short_trans_cost + plane_cost + train_cost + foreign_currency)


print(f"Hotel: {hotel_cost}")
print(f"Flight: {plane_cost}")
print(f"Train: {train_cost}")
print(f"Short form transportation: {short_trans_cost}")
print(f"Spending money in foreign currency: {short_trans_cost}")
print(f"The total cost of your trip to {country} is: {short_trans_cost}")







