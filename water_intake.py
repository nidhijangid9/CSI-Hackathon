def calc_water_intake(activity, weight):
    water = 2000
    
    if activity.strip().lower() == 'sedentary':
        water *= 1.0  # No adjustment
    elif activity.strip().lower() == 'light activity':
        water *= 1.1  # Increase by 10%
    elif activity.strip().lower() == 'moderate':
        water *= 1.2  # Increase by 20%
    elif activity.strip().lower() == 'very active':
        water *= 1.3  # Increase by 30%
    elif activity.strip().lower() == 'extremely active':
        water *= 1.4   # Increase by 40%
    
    # rule of thumb: 30-35 ml/kg/day
    water += weight * 3.5
    
    return water

weight = float(input("Enter your weight (in kg): "))
activity = input("Enter your activity level (sedentary / light activity / moderate / very active / extremely active): ")

water = calc_water_intake(activity, weight)
print("\nRecommended daily water intake (approximately) = {:.2f} liters".format(water/1000))