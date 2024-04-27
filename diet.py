import streamlit as st
import pandas as pd

# Load the datasets
df = pd.read_csv("input.csv")  # Replace "input.csv" with the actual path to your dataset
substitute_df = pd.read_csv("food_substitutes.csv")  # Load the food substitutes dataset

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)

# Function to estimate daily calorie intake based on BMI, age, and activity level
def estimate_daily_calories(bmi, age, activity_level, weight, height, goal):
    # Calculate Basal Metabolic Rate (BMR) using Harris-Benedict equation
    if activity_level == "Low":
        bmr = 66 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
    elif activity_level == "Moderate":
        bmr = 66 + (13.75 * weight) + (5.003 * height) - (6.755 * age) * 1.55
    else:  # High activity level
        bmr = 66 + (13.75 * weight) + (5.003 * height) - (6.755 * age) * 1.725
    
    # Adjust BMR based on BMI and goal
    if goal == "Lose Weight":
        if bmi < 16:
            bmr *= 1.2  # Increase calorie intake for severely underweight individuals
        elif 16 <= bmi < 18.5:
            bmr *= 1.1  # Increase calorie intake for underweight individuals
        elif 25 <= bmi < 30:
            bmr *= 0.9  # Decrease calorie intake for overweight individuals
        elif bmi >= 30:
            bmr *= 0.8  # Decrease calorie intake for severely overweight individuals
    elif goal == "Gain Weight":
        if bmi < 16:
            bmr *= 0.2 # Increase calorie intake for severely underweight individuals
        elif 16 <= bmi < 18.5:
            bmr *= 0.5  # Increase calorie intake for underweight individuals
        # Add more conditions if needed for different BMI ranges
    else:
        # No adjustment for maintaining weight
        pass
    
    return bmr

# Function to generate diet plan based on daily calorie intake and goal
def generate_diet_plan(daily_calories, goal):
    if goal == "Lose Weight":
        # Filter food items for weight loss
        filtered_df = df[df["Calories"] < daily_calories]
    elif goal == "Gain Weight":
        # Filter food items for weight gain
        filtered_df = df[df["Calories"] > daily_calories]
    else:
        # Filter food items for maintaining weight
        filtered_df = df[df["Calories"] <= daily_calories]
        
    return filtered_df

# Function to find substitutes for a given food item
def find_substitute(food_item):
    try:
        substitute = substitute_df[ substitute_df['Food Item'].str.lower() == food_item.lower() ]
        return substitute["Substitute"].values[0] if not substitute.empty else "Substitute not found"
    except Exception as e:
        return f"Error occurred: {str(e)}"

# Main function to run the Streamlit app
def main():
    st.title("Daily Diet Planner")
    
    # Input fields
    age = st.number_input("Enter your age:", min_value=1, max_value=150, value=25)
    weight = st.number_input("Enter your weight (in kg):", min_value=1.0, max_value=500.0, value=60.0, step=0.1)
    height = st.number_input("Enter your height (in cm):", min_value=50.0, max_value=300.0, value=170.0, step=0.1)
    activity_level = st.selectbox("Select your activity level:", ["Low", "Moderate", "High"])
    goal = st.selectbox("Select your goal:", [ "Gain Weight","Lose Weight", "Maintain Weight"])
    # print(goal)
    
    # Estimate daily calorie intake based on BMI, age, activity level, and goal
    bmi = calculate_bmi(weight, height)
    daily_calories = estimate_daily_calories(bmi, age, activity_level, weight, height, goal)
    st.write("Estimated daily calorie intake:", daily_calories)
    
    # Generate diet plan based on daily calorie intake and goal
    diet_plan = generate_diet_plan(daily_calories, goal)
    
    st.subheader("Recommended Food Items:")
    st.write(diet_plan)

    # Get substitute for a given food item
    food_item_input = st.text_input("Enter a food item to find its substitute:")
    if food_item_input:
        substitute = find_substitute(food_item_input)
        st.write(f"Substitute for {food_item_input}: {substitute}")

if __name__ == "__main__":
    main()
