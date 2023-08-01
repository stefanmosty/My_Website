import json
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# find more emojis here : (https://www.webfx.com/tools/emoji-cheat-sheet/)
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


#  - - - - Use local CSS - - - - 
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)

local_css("style/style.css")



# - - - - Load Assets - - - -
lacrosse_pic = Image.open("Images/laxpic2.png")
trihelix_pic = Image.open("Images/trihelix_pic.png")
kansaswheat_pic = Image.open("Images/kansaswheat_pic.png")
cti_pic = Image.open("Images/cti.png")

lottie_coding = load_lottiefile("lottiefiles/trading_animation.json")

# - - - - HEADER Section - - - -
st.header("Hi, I am Stefan :wave:")
st.write("I am passionate about the rise and use of data science, specifically in the realm of algorithmic trading and sports.\n I'm currently pursuing a Master of Science degree in Information Systems and Operations Management with a focus in Data Science.")
st.write("Connect with me on LinkedIn! [Learn More >](https://www.linkedin.com/in/stefan-mostovych-a63287193/)")


# My goals, skills, and what I want to do
with st.container():
    st.write("---")
    left_column, right_column = st.columns((1,2))
    with left_column:
        st.subheader("What I Do")
        st.write("##")
        st.write(
        """
          Outside of the classroom, the work I do includes:
          - Trade Futures (NQ and ES)
          - Take coding course in Python and C
          - Work on building my own websites like this one
          - Create my own trading algos

          My hobbies include reading, learning the ukulele, hanging with friends, and playing any and all sports.

             """)
    with right_column:
        st_lottie(lottie_coding,height=300, key="coding")


# My Project
        
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with text_column:
        st.subheader("Exploring the Impact of Climatic and Economic Variables on Wheat Yield and Market Prices in Kansas: A Regression Analysis")
        st.write("[Presentation >](https://uflorida-my.sharepoint.com/:p:/g/personal/faith_aiya_ufl_edu/EeOjrY085MxJjX4ZB3xpmsEBMP9c6V8oonVtfIbCjkXsZw?rtime=9-ehMC6S20g)")
        st.write("[Paper >](https://docs.google.com/document/d/1wcS7qVfZjoDosmVED7NMke3RfUrnj6e4U9iLiWYDQxc/edit)")
    with image_column:
        st.image(kansaswheat_pic)
    image_column, text_column = st.columns((1,2))
    with text_column:
        st.subheader("TriHelix Revenue Consulting Project")
        st.write(("[Presentation >](https://docs.google.com/presentation/d/1ekZMl4hW_ikC1y3TXqBAbjGS1DBUHe-OCtSEb5_rWvI/edit#slide=id.g238e7d9357a_4_143)"))
    with image_column:
        st.image(trihelix_pic)
    image_column, text_column = st.columns((1,2))
    with text_column:
        st.subheader("Other Bot")

# --- What I DO OUTSIDE THE CLASSROOM ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Outside the Classroom")
        st.write("##")
        st.write(
            """
            I also am captain of the Club Lacrosse Team at the University of Florida. Over the past 2 years I've received the following awards:
            - 2022 SELC Div. 1 First-Team All-American
            - 2022 MCLA Div. 1 Second-Team All-American
            - 2022 MCLA Div. 1 Scholar Athlete
            - 2023 SELC Div. 1 First-Team All-American
            - 2023 MCLA Div. 1 Second-Team All-American
            - 2023 MCLA Div. 1 Scholar Athlete
            - 2023 SELC Specialty PLayer of the Year


            Check out the news articles on the MCLA website! """
        )
        st.write("[MCLA Div. 1 All-American teams](https://mcla.us/news/2023/05/d-i-all-american-teams-announced)")
        st.write("[SELC Scholar Athletes](https://mcla.us/news/2023/07/division-i-scholar-athletes-announced)")
    with right_column:
         st.image(lacrosse_pic)
    

        

        
# - - - - CONTACT - - - - 

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documentation
    contact_form = """<form action="https://formsubmit.co/stefanmostovych@ufl.edu" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required> 
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>"""
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()