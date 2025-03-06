import streamlit as st

# Set page configuration
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Function to convert length units (meters, kilometers, miles, feet)
def length_converter(value, from_unit, to_unit):
    conversions = {
        "meters": 1,  # Base unit
        "kilometers": 0.001,  # 1 meter = 0.001 kilometers
        "miles": 0.000621371,  # 1 meter = 0.000621371 miles
        "feet": 3.28084  # 1 meter = 3.28084 feet
    }
    return value * conversions[to_unit] / conversions[from_unit]

# Function to convert weight units (kilograms, grams, pounds)
def weight_converter(value, from_unit, to_unit):
    conversions = {
        "kilograms": 1,  # Base unit
        "grams": 1000,  # 1 kilogram = 1000 grams
        "pounds": 2.20462  # 1 kilogram = 2.20462 pounds
    }
    return value * conversions[to_unit] / conversions[from_unit]

# Function to convert temperature units (Celsius, Fahrenheit)
def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value  # No conversion needed if units are the same
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32  # Convert Celsius to Fahrenheit
    if from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9  # Convert Fahrenheit to Celsius
    return value

# Set up the Streamlit app title and description
st.title("🔄 Unit Converter")
st.markdown("### Convert Length, Weight, and Temperature easily!")
st.markdown("---")

# Let the user choose what type of conversion they want
conversion_type = st.selectbox("Select conversion type", ["Length", "Weight", "Temperature"])

if conversion_type == "Length":
    st.subheader("📏 Length Converter")
    from_unit = st.selectbox("From", ["meters", "kilometers", "miles", "feet"], key="length_from")
    to_unit = st.selectbox("To", ["meters", "kilometers", "miles", "feet"], key="length_to")
    value = st.number_input("Enter value", min_value=0.0, format="%.2f", key="length_value")
    if st.button("Convert", key="length_convert"):
        result = length_converter(value, from_unit, to_unit)
        st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Weight":
    st.subheader("⚖️ Weight Converter")
    from_unit = st.selectbox("From", ["kilograms", "grams", "pounds"], key="weight_from")
    to_unit = st.selectbox("To", ["kilograms", "grams", "pounds"], key="weight_to")
    value = st.number_input("Enter value", min_value=0.0, format="%.2f", key="weight_value")
    if st.button("Convert", key="weight_convert"):
        result = weight_converter(value, from_unit, to_unit)
        st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Temperature":
    st.subheader("🌡️ Temperature Converter")    
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit"], key="temp_from")
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit"], key="temp_to")
    value = st.number_input("Enter value", format="%.2f", key="temp_value")
    if st.button("Convert", key="temp_convert"):
        result = temperature_converter(value, from_unit, to_unit)
        st.success(f"✅ {value} {from_unit} = {result:.2f} {to_unit}")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center;'>
        <strong>Made by <a href='https://github.com/HammadMustafa' target='_blank'>Hammad Mustafa</a></strong>
    </div>
    """,
    unsafe_allow_html=True
)
