import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Vacation Planner",
    page_icon="logo.webp",
    layout="wide",
)

header_col, logo_col = st.columns([5, 1])
with header_col:
    st.title("Vacation Planner")
with logo_col:
    st.image("logo.webp", width=120)

st.header("Plan Your Dream Vacation")
st.write("Use this app to plan your perfect vacation. Select your destination, activities, and budget to get started!")

# Read hotel data from CSV
hotel_data = pd.read_csv("hotels.csv")

# Destination selector with no default selected option
available_destinations = ["Select a destination"] + sorted(hotel_data["destination"].unique().tolist())
selected_destination = st.selectbox(
    "Choose a destination:",
    available_destinations,
    index=0,
)

# Only show recommendations after a destination is selected
if selected_destination == "Select a destination":
    st.info("Choose a destination to see hotel recommendations.")
else:
    matching_hotels = hotel_data[hotel_data["destination"] == selected_destination].head(3).copy()

    st.subheader(f"Recommended hotels in {selected_destination}")

    if matching_hotels.empty:
        st.warning("No hotels available for this destination yet.")
    else:
        for _, hotel in matching_hotels.iterrows():
            st.markdown(
                f"### {hotel['hotel_name']}\n"
                f"- Location: {hotel['location']}\n"
                f"- Price per night: ${hotel['price_per_night']:.0f}\n"
                f"- Rating: {'★' * int(hotel['stars'])}{'☆' * (5 - int(hotel['stars']))} ({hotel['stars']} stars)"
            )

# Additional pages
with st.sidebar:
    st.header("Additional Information")
    st.write("This section can contain links to other resources, such as:")
    st.markdown("- Travel tips")
    st.markdown("- Destination guides")
    st.markdown("- Hotel booking links")
    st.markdown("- Contact information for travel agencies")