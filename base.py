print("hai welcome to python")
import streamlit as st

st.balloons()
#image

st.image("C:\\Users\\rc6so\\OneDrive - T-Square Cloud\\Pictures\\my-photo\\Family-Life-insurance-under-MWP-Act.webp")



# title

st.title("We1come to python")

# Header

st.header("welcome to streamlit")

# sub header
st.subheader("Functions")

#To give Information
st.info("My information")
# Warning message
st.warning("Come on time or else you will be marked absent")
# write
st.write( "Employee name")
st. write(range(100))


# Error msg

st.error("wrong msg")

st.success("nice success")

#markdown
st.markdown("T-squart")
st.markdown("# T-squart")
st.markdown("## T-squart")
st.markdown("### T-squart")

st.markdown(":moon:")
st.markdown("☀️🌄🌅")

#Text
st.text("I am try to make web application ")

#To write a caption

st.caption("there is caption")


#to display maths

st.latex(r''' a+b+c x^2''')


#widget

st.checkbox("login")

#button

st.button("click")

#Radio button

st.radio("click gender",["male",'female'])

#select box

st.selectbox("Pick your course" ,[ "ML" , "Cloud" , "Data science"])


#multi select

st.multiselect("select dept",['sales','admin','marketting'])

#selectslider

st.select_slider("Rating",['goog','bad','excellent'])


#slider
st.slider("Enter your number",0,50)

#number input
st.number_input("pick a number",0,30)

#txt
st.text_input("Enter Email : ")


#date input

st.date_input("Set date")

# Time input

st.time_input("Set time")


#Text area
st.text_area("214571461364              jgdfljksdhf             746872364")


#file upload

st.file_uploader("upload your file")

#color
st.color_picker("color")

st.progress(50)

#spinner
import time as t
with st.spinner("Just wait"):
    t.sleep(5)


#sidebar

st.sidebar.title("Welcome to my world")
st.sidebar.text_input("E-mail :")
st.sidebar.text_input("password : ")
st.button("submit")



# Embed YouTube video
st.video('https://www.youtube.com/watch?v=2hIBYguD-pU')

# Embed audio file
st.audio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3')


# .streamlit/config.toml
#[theme]
primaryColor = "#F63366"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"




























































