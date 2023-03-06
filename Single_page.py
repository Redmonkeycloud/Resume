import requests
from pathlib import Path
import streamlit as st 
from PIL import Image
from streamlit_lottie import st_lottie
 
# --- Path settimgs. --- 
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/ "styles" / "main.css"
resume_file = current_dir/ "assets"/"George_Plessias_-_Environmental_Engineer (2).pdf"
profile_pic = current_dir/"assets"/"profile-pic (1).png"

# --- General settings. --- 
PAGE_TITLE = "George Plessias | Resume"
PAGE_ICON =  "📃"
NAME = "George Plessias"
DESCRIPTION = """
Environmental Engineer with a passion for Machine Learning & Artificial Intelligence
"""
EMAIL = "plessiasgeorge@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn":"https://www.linkedin.com/in/george-plessias",
    "GitHub" : "https://github.com/Redmonkeycloud?tab=repositories",
    "Twitter": "https://twitter.com/GeorgePlessias"
}

st.set_page_config(page_title= PAGE_TITLE, page_icon= PAGE_ICON)

# --- Load CSS, PDF & Profile Picture --- 
with open(css_file) as f :
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file :
    PDF = pdf_file.read()

profile_pic = Image.open(profile_pic)

# --- Load Lottie --- 
def load_lottie_url(url):
            req = requests.get(url)
            if req.status_code != 200:
                return None
            return req.json()

lottie_coding = load_lottie_url("https://assets4.lottiefiles.com/packages/lf20_knvn3kk2.json")
lottie_coding_2 = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_xSuO9M.json")
lottie_coding_3 = load_lottie_url("https://assets3.lottiefiles.com/packages/lf20_6A6dPa5oOg.json")
lottie_coding_4 = load_lottie_url("https://assets4.lottiefiles.com/packages/lf20_Qy4K6awomF.json")
# --- Section no.1 --- 
col1, col2 = st.columns(2, gap="small")
with col1 :
    st.image(profile_pic, width= 250)
with col2 :
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data= PDF,
        file_name= resume_file.name,
        mime="application/octen-stream"
    )
    st.write('\n')
    st.write("✉️", EMAIL)

# --- Section no.2 --- 
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- Experience. --- 
with st.container():
    st.write("###")
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write('\n')
        st.subheader("Experience & Qualifications")
        st.write(
            """
        -  ✔️ 2 Years experience developing Machine Learning models.
        -  ✔️ Strong hands on Experience and knowledge in Python and Excel.
        -  ✔️ Good understanding of statistical principles and their respective applications.
        -  ✔️ Excellent team-player and displaying strong sense of initiative on tasks
        """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# --- Skills --- 
with st.container():
    st.write("###")
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st_lottie(lottie_coding_2, height=300, key="coding1")
    with right_column:
        st.subheader("Hard Skills")
        st.write(
            """
        -  Programming: Python (Scikit-learn, Tensorfolw, Pandas), MatLab
        -  Data Visulization: MS Excel, Plotly
        -  Modeling: Logistic Regression, Linear Regression, Decision trees
        """
        )

# --- Languages. --- 
with st.container():
    st.write("###")
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Languages")
        st.write(
            """
        -  ✔️ Greek (Mother Tongue)
        -  ✔️ English (C2)
        -  ✔️ German (B2)
        -  ✔️ French (B1)
        """
        )
    with right_column:
        st_lottie(lottie_coding_3, height=300, key="coding2")

# --- Professional History ---
st.subheader("Professional History")
st.write("---")

# JOB 1
st.write("**System Analyst | EMTech Space**")
st.write("02/2022 - 02/2023")
st.write(
    """
- ► Optimized use of Machine Learning Models to streamline forecasting & smart grids load allocation, 
resulting in cost savings of 15%.
- ► Advised on design of smart systems for buildings, increasing efficiency by 20% and customer comfort.
- ► Designed distributed micro-grid systems for residential applications with a 97% accuracy rate, reducing 
operational costs by 15%.
"""
)

# JOB 2
st.write('\n')
st.write("**Communications Departement | Greek Military**")
st.write("01/2021 - 10/2021")
st.write(
    """
- ► Mandatory Military Service, completed
"""
)

# JOB 3
st.write('\n')
st.write("**Researcher | National Technical University of Athens**")
st.write("03/2019 - 06/2020")
st.write(
    """
- ►  Developed neural networks algorithm to detect mathematical functions in Santorini frescoes, resulting in 
unseen insights with 95% accuracy.
- ► Implemented MATLAB scripts for data collection & analysis, leading to recognition of over 15 previously 
unknown patterns within the frescoes.
- ► Conducted research collaboration with 2 professors (Mr. Papaodysseus & Mr. Koukoutsis) of 
the Electrical Engineering department(NTUA), on stencils in ancient frescoes, demonstrating the techniques 
uncovered.
"""
)

# --- Cerificates. ---
st.subheader("Cerificates")
st.write("---")

st.write(
    """
- ►  Smarterials, Technical University of Crete | Mar, 2020 
- ► Zero-Energy Design: an approach to make your building sustainable, Edx/ Delft University |
Sept, 2021
- ► Python Basics for Data Science, Edx/IBM | Mar, 2022
- ► Deep Learning Fundamentals with Keras, Edx/IBM | Feb, 2022
- ► Computer Vision and Image Processing Fundamentals, Edx/ IBM | Mar, 2023
"""
)