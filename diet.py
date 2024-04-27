import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv("input.csv")  # Replace "input.csv" with the actual path to your dataset

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)

# Function to generate diet plan based on BMI and goal
def generate_diet_plan(bmi, goal, total_calories):
    if goal == "Lose Weight":
        st.subheader("Here is some exercise you should also look :")
        return ['loss1.webp', 'loss1.webp']

        # Filter food items for weight loss
        filtered_df = df[df["Calories"] < total_calories]
    elif goal == "Gain Weight":
        # Filter food items for weight gain
        st.subheader("Here is some exercise you should also look :")
        return ['gain1.webp', 'gain2.webp']
        filtered_df = df[df["Calories"] > total_calories]
    else:
        # Filter food items for maintaining weight
        st.subheader("Here is some exercise you should also look :")
        return ['heal.webp']
        filtered_df = df[df["Calories"] <= total_calories]
        
    # Select food items based on BMI category
    if bmi < 16:
        bmi_category = "Severely Underweight"
    elif 16 <= bmi < 18.5:
        bmi_category = "Underweight"
    elif 18.5 <= bmi < 25:
        bmi_category = "Healthy"
    elif 25 <= bmi < 30:
        bmi_category = "Overweight"
    else:
        bmi_category = "Severely Overweight"
    
    # Filter food items based on BMI category
    diet_plan = filtered_df[filtered_df["Food_items"].isin(df[df["Calories"] <= total_calories]["Food_items"])]
    diet_plan = diet_plan[["Food_items", "Breakfast", "Lunch", "Dinner", "Calories"]]  # Select required columns

    return diet_plan

# Main function to run the Streamlit app
def main():
    st.title("Daily Diet Planner")
    
    # Input fields
    age = st.number_input("Enter your age:", min_value=1, max_value=150, value=25)
    weight = st.number_input("Enter your weight (in kg):", min_value=1.0, max_value=500.0, value=60.0, step=0.1)
    height = st.number_input("Enter your height (in cm):", min_value=50.0, max_value=300.0, value=170.0, step=0.1)
    goal = st.selectbox("Select your goal:", ["Lose Weight", "Gain Weight", "Maintain Weight"])
    total_calories = st.number_input("Enter your total calorie intake (kcal):", min_value=0, value=2000)
    
    if st.button("Calculate BMI and Diet Plan"):
        bmi = calculate_bmi(weight, height)
        st.write("Your body mass index is: ", bmi)
        diet_plan = generate_diet_plan(bmi, goal, total_calories)
        
        st.subheader("Recommended Food Items:")
        st.write(diet_plan)

if __name__ == "__main__":
    main()
