import streamlit as st

st.title("🚚 Truck Volume Calculator (ट्रक आयतन कैलकुलेटर)")

def convert_to_inches(value):
    """Convert input like '12.5' (12ft 5in) to inches"""
    try:
        if "." in value:
            feet, inch = value.split(".")
            return int(feet) * 12 + int(inch)
        else:
            return int(value) * 12
    except ValueError:
        raise ValueError("Invalid number format")

height = st.text_input("Height ऊँचाई (जैसे 12.5 = 12ft 5in)")
width = st.text_input("Width चौड़ाई (जैसे 4.5 = 4ft 5in)")
breadth = st.text_input("Breadth लंबाई (जैसे 24.5 = 24ft 5in)")

if st.button("Calculate हिसाब लगाएँ"):
    try:
        h_in = convert_to_inches(height)
        w_in = convert_to_inches(width)
        b_in = convert_to_inches(breadth)
        cu_in = h_in * w_in * b_in
        cu_ft = cu_in / 1728
        st.success(f"आयतन (Volume) = {cu_ft:.2f} cubic feet")
    except ValueError:
        st.error("कृपया सही संख्या डालें (Please enter valid numbers)")
