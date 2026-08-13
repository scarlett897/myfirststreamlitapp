import streamlit as st

st.title("Breakfast")
st.header("The use of Breakfast")
st.write("Breakfast is one of the most important things in life. People rely on it to maintain their daily needs.")
st.subheader("Coffee")
st.write("Coffee has been used widely at the start of the morning. It is known to keep people up and give them a head start for the day. There are many kinds of coffee, and everyone has their special choice of their own.")
st.subheader("Eggs")
st.write("Eggs are known to contain many protein and nutrients. You can have eggs in many ways: sunny side up, scrambled, hard boiled, etc. People have different ways to eat eggs, and it is recommended for people to eat two eggs every day. ")
st.subheader("Bacon")
st.write("Bacon is one of the most known partner with eggs. Many hotels offer bacon and eggs as a breakfast menu. Bacon comes from pork, and it is know for its good taste. There are many kinds of bacon. The typical way people eat bacon is to fry them on a pan. They have a savoury taste and are commonly eaten.")
st.subheader("Toast")
st.write("Toast is also a common food eaten during breakfast. It is bread being fried, or put in the toaster. Some people put butter on toast, while others put jam on top. There are also people who eat toast without anything and with honey. Toast has a crispy taste, and basically everyone can eat it.")

with st.sidebar:
    st.header("Settings")
    name=st.text_input("Name")
    mood=st.selectbox("Select your AI's mood", ["Happy", "Sad", "Angry","Bored","I don't want to do homework"])
    gender=st.selectbox("Your gender", ["Male", "Female","Other"])
    creativity=st.slider("Select your creativity", 0, 10)
    if st.button("Save"):
        st.write(f"Saved.")