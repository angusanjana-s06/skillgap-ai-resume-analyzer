import streamlit as st
skill_db = [
    "python",
    "sql",
    "canva",
    "excel",
    "java",
    "power bi",
    "javascript",
    "html",
    "c++",
    "tableau",
    "streamlit"
]

st.title("SkillGap AI")

st.header("Welcome to SkillGap AI")

st.subheader("Resume Reader and Analyzer")

name = st.text_input("Enter your name")

if name:
    st.write(f"Hello {name}, Welcome!!")

st.write("Resume Reader and Analyzer")

uploaded = st.file_uploader(
    "Attach your resume",
    type=["txt"]
)

found_skill = []
text = ""

if uploaded is not None:

    st.write("Uploaded successfully")
    st.write("File name:", uploaded.name)

    text = uploaded.read().decode("utf-8")

    st.write("Skills Found:")

    for skill in skill_db:
        if skill.lower() in text.lower():
            found_skill.append(skill)
            st.write(skill)

else:
    st.write("Upload a valid file (TXT only)")

role = st.selectbox(
    "Select target role",
    ["Python Developer", "Data Analyst", "Web Developer"]
)

Python_dev = ["python", "git", "streamlit", "sql"]

data_anal = ["sql", "python", "excel", "git", "power bi"]

web_dev = ["python", "sql", "excel", "git", "streamlit", "javascript", "html", "tableau"]

if role == "Python Developer":
    require_skill = Python_dev

elif role == "Data Analyst":
    require_skill = data_anal

else:
    require_skill = web_dev


st.write("Required skills:", require_skill)

miss_skill = []

for skill in require_skill:

    if skill.lower() not in [x.lower() for x in found_skill]:
        miss_skill.append(skill)


st.write("Missing Skills:")

for skill in miss_skill:
    st.write(skill)

score = (len(require_skill) - len(miss_skill)) / len(require_skill) * 100

st.write("Score:", score)

st.progress(score / 100)

if score == 100:
    st.write("Excellent! You have all the required skills.")

elif score >= 85:
    st.write("Almost there! Just learn a few more skills.")

elif score >= 60:
    st.write("Good progress. You need to learn:")
    st.write(miss_skill)

elif score >= 45:
    st.write("You need more practice and skill development.")

else:
    st.write("You need to improve your skills for this role.")