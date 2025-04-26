#Sunday morning, assignment 1, " Google Unit Convertor" using python and streamlit

import streamlit as st

st.markdown(
    """ 
    <style>
        body {
            background-color: #1e1e2f;
            color: white;
        }
        .stApp {
            background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
        }
        h1 {
            text-align: center;
            font-size: 36px;
            color: white;
        }
        .stButton>button {
            background: linear-gradient(45deg, #0b5394, #351c75);
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 10px;
            transition: 0.3s;
            box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
            font-weight: bold;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            background: linear-gradient(45deg, #925e9d, #00c9ff);
            color: white;
            font-weight: bold;
        }
        @keyframes fadeInUp {
            from {
                    opacity: 0;
                    transform: translateY(20px);
            }
            to {
                    opacity: 1;
                    transform: translateY(0);
            }
        }
        .result-box {
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            background: rgba(255, 255, 255, 0.1);
            padding: 25px;
            border-radius: 10px;
            color:rgb(31, 124, 150);
            margin-top: 20px;
            box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
            animation: fadeInUp 0.8s ease forwards;
        }
        .footer{
            text-align: center;
            font-size: 14px;
            color: black;
            margin-top: 50px;
        }
        .footer a {
            text-decoration: none;
            color: black;
            transition: 0.3s;
        }
        .footer a:hover {
            color: #6a11cb; /* A pretty purple */
            text-shadow: 0 0 5px #6a11cb, 0 0 10px #6a11cb;
        }
    </style>
    """,
    unsafe_allow_html=True,
    )

#Title and Description
st.markdown("<h1>Unit Convertor App 🔮</h1>", unsafe_allow_html=True)
st.write("Go ahead and play along with this easy to use convertor 🤩")

#sidebar menu
conversion_type = st.sidebar.selectbox("Which Unit do you wish to convert? 🤔", ["Length 📏", "Weight ⚖️", "Temperature 🌡️"])
value = st.number_input("Enter the value to convert 💬", value = 0.0, min_value = 0.0, max_value = 1000000.0, step = 0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length 📏":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Feet", "Yards", "Inches"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Feet", "Yards", "Inches"])
elif conversion_type == "Weight ⚖️":
    with col1:
        from_unit = st.selectbox("From", ["Kilogram", "Gram", "Milligram", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilogram", "Gram", "Milligram", "Pounds", "Ounces"])
elif conversion_type == "Temperature 🌡️":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

#converted function
def convert_length(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Millimeters': 1000, 
        'Miles': 0.000621371, 'Feet': 3.28084, 'Yards': 1.09636, 'Inches': 39.37
    }
    return (value/length_units[from_unit] * length_units[to_unit])
  

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        'Kilogram': 1, 'Gram': 1000, 'Milligram': 1000000, 'Pounds': 2.20462, 'Ounces': 35.274
    }
    return (value/weight_units[from_unit] * weight_units[to_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value 
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value

#button for conversion
if st.button("Convert 🔮"):
    if from_unit == to_unit:
        st.markdown(f"<div class='result-box'>Pshht you selected the same units! 🛡️ How am I supposed to convert that? 😭 {value} {from_unit} = {value} {to_unit}</div>", unsafe_allow_html=True)
    else:
        if conversion_type == "Length 📏":
            result = convert_length(value, from_unit, to_unit)
        elif conversion_type == "Weight ⚖️":
            result = convert_weight(value, from_unit, to_unit)
        elif conversion_type == "Temperature 🌡️":
            result = convert_temperature(value, from_unit, to_unit)
        
        st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)
    
#footer
st.markdown(f"<div class='footer'>Developed with blood sweat and tears 🩸 by Maryam Khan ✨ <a href='https://github.com/maryamkhan00' target='_blank'>@maryamkhan00</a></div>", unsafe_allow_html=True)