# streamlit
import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", project_icon="✨")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.title("🚀 Welcome To Growth Mindset Challenge")
st.write(""""What is a Growth Mindset?
A growth mindset means that your abilities and intelligence can improve through **hard work, perseverance, and learning**.
""")

# Quite Section
st.header ("💡 Today Growth Mindset Quite Challange")
st.write("Success is not final, Failure is not fatal: It is the courage to continue that counts.""- winston Churchill")

st.header("🎯 What's Your Challange Today??")
user_input = st.text_input("Describe a challange you're facing: ")

# Condition
if user_input:
    st.success(f"💪 You are facing: {user_input}. keep pushing forword towords your goal!🎯")
else:
    st.warning("Tell us about your challange to get started!")

# Reflection
st.header("🔥Reflect On Your Learning")
reflection = st.text_area("Write your reflection here:")
if reflection:
    st.success(f"✨Greate Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experiance help you grow! Share your difficulties")

# Acheivements
st.header("🏆 Celebrate Your Acheivement!")
acheivement = st.text_input("Share something you've recently accomplished:")

if acheivement:
    st.success(f"🥇 Amazing! You achieved: {acheivement}")
else:
    st.info("Big or small , Every acheivement counts! Share one now 🤩")

# Footer
st.write("- - -")
st.write("🏅Keep believing in yourself. Growth is a journey, Not a distination! ✨")
st.write("** 🎉Created By Kashan Taj✨ **")