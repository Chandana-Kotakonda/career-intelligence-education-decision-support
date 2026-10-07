import streamlit as st


st.set_page_config(
    page_title="Career Intelligence & Education Decision Support",
    page_icon="🧭",
    layout="wide"
)


st.title("🧭 Career Intelligence & Education Decision Support System")

st.write(
    "A data-driven system for career discovery, skill-gap analysis, "
    "job-market insights, education decisions, and career planning."
)


pages = [
    "🏠 Home",
    "👤 My Profile",
    "🧭 Career Discovery",
    "💼 Job Intelligence",
    "🎓 Education",
    "🔄 Career Transition",
    "⚖️ Compare Careers",
    "🔮 What-If",
    "🗺️ My Roadmap",
]


selected_page = st.sidebar.radio(
    "Navigation",
    pages
)


st.header(selected_page)

if selected_page == "🏠 Home":
    st.write("Welcome to the Career Intelligence & Education Decision Support System.")
    st.info("Project skeleton is working. Features will be added in later tasks.")

else:
    st.info(f"{selected_page} module will be developed in the upcoming tasks.")