Destination = input("Enter your destination:").strip().title()
Distance_in_Kilometer = float(input("Enter the distance to your destination in kilometers:"))
Speed_in_Km_per_h = float(input("Enter your speed in kilometers per hour:"))
Travel_Time_in_Hours = Distance_in_Kilometer / Speed_in_Km_per_h
print(f"Your travel time to {Destination} is: {Travel_Time_in_Hours} hours")