import streamlit as st


# Title
st.write(" # Welcome to BMI Calculator")

# Take weight input in kg
weight = st.number_input("Enter your weight (in kg)")

# Take height input

status = st.radio("Select your height format : ", ("cms", "feet","meters"))

if(status == "cms"):
    height = st.number_input("Centimeters")
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter some value of height")
elif(status == "feet"):
    height = st.number_input("Feet")
    try:
        bmi = weight /((height/3.28)**2)
    except:
        st.text("Enter some value of height")
else:
    height = st.number_input("Meters")
    try:
        bmi = weight /(height**2)
    except:
        st.text("Enter some value of height")


# checked if the button is pressed or not
        
if(st.button("Calculate MBI")):
    st.text("Your BMI index is {}".format(bmi))
    
    if(bmi < 16):
         st.error("You are extremely underwight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
    elif (bmi >= 25 and bmi < 30):
        st.warning("You are Overweight")
    elif (bmi > 30):
        st.error("You are Extremely Overweight")







