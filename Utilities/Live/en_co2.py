def calculate_carbon_footprint():
    print("Carbon Footprint Calculator")
    
    car_distance = float(input("Enter the distance traveled by car in kilometers: "))
    car_consumption = float(input("Enter the car fuel consumption in liters per kilometer: "))
    
    electricity_consumed = float(input("Enter the amount of electricity consumed in kilowatt-hours: "))
    
    car_emission_factor = 2.3
    electricity_emission_factor = 0.6
    
    car_footprint = car_distance * car_consumption * car_emission_factor
    electricity_footprint = electricity_consumed * electricity_emission_factor
    
    total_footprint = car_footprint + electricity_footprint
    
    print("\nResults:")
    print(f"Carbon footprint for car: {car_footprint} kg of CO2")
    print(f"Carbon footprint for electricity: {electricity_footprint} kg of CO2")
    print(f"Total carbon footprint: {total_footprint} kg of CO2")

calculate_carbon_footprint()
