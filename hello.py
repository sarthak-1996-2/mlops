import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="My Custom App Title",
    page_icon="⭐",  # Can be an emoji, an image path, or a Material icon like ":material/thumb_up:"
    layout="centered"
)

st.title('My First Streamlit app.')

df = pd.DataFrame({
    "Name": ['Sarthak', 'Barsa'],
    "iq": [122, 111]
})

display = st.checkbox("Display dataset:")

if display:
    st.write(df.head())



st.header("Prediction", divider='gray')
st.subheader("My Prediction :blue[cool] :sunglasses:")

genre = st.radio(
    "What's your favorite movie genre", [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
)

st.write(f"You selected {genre}")

option = st.selectbox(
    "Default email", ["None","foo@example.com", "bar@example.com", "baz@example.com"]
    )

st.success(option)

if st.button("Predict", type="primary"):
    st.write("Your prediction is successful.")

left, middle, right = st.columns(3)
if left.button("Plain button", width="stretch"):
    left.markdown("You clicked the plain button.")
if middle.button("Emoji button", icon="😃", width="stretch"):
    middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", width="stretch"):
    right.markdown("You clicked the Material button.")

def sqr(x):
    return x * x

st.header("Square the number.")

num = st.number_input("Write a number: ")

if st.button("Calculate"):
    st.text(sqr(num))


