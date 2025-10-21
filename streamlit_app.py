import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Data Analytics AI",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Session state for role
if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "PC", "Professor", "Team"]

# Login section
def login():
    st.markdown("## User Login")
    role = st.selectbox("Select your role", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()

# Logout section
def logout():
    st.markdown("## Logout")
    if st.button("Log out"):
        st.session_state.role = None
        st.rerun()

# Define pages with updated titles
role = st.session_state.role

logout_page = st.Page(logout, title="Sign Out")
settings = st.Page("settings.py", title="Settings")

visualization = st.Page(
    "Visualization/visualization.py",
    title="Data Dashboard",
    default=(role == "Requester"),
)
maps = st.Page(
    "Visualization/maps.py",
    title="Maps",
    default=(role == "Requester"),
)
maps2 = st.Page(
    "Visualization/maps2.py",
    title="Additional Maps",
    default=(role == "Requester"),
)

ml = st.Page(
    "ml/ml_analysis.py",
    title="Machine Learning",
    default=(role == "Responder"),
)
eda = st.Page(
    "EDA/eda.py",
    title="Exploratory Data Analysis",
    default=(role == "Admin"),
)

# Group pages into sections
account_pages = [logout_page, settings]
visualization_pages = [visualization, maps, maps2]
ml_pages = [ml]
eda_pages = [eda]

# App header and branding
st.markdown(
    """
    <style>
        .main {background-color: #f5f7fa;}
        h1 {color: #2c3e50;}
        .stButton>button {background-color: #1f77b4; color: white;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Data Analytics AI")
st.logo("images/horizontal_blue.png", icon_image="images/icon_blue.png")

# Navigation logic
page_dict = {}

if role in ["Professor", "Team"]:
    page_dict["Exploratory Analysis"] = eda_pages
if role in ["Professor", "Team", "PC"]:
    page_dict["Visualization"] = visualization_pages
if role in ["Professor", "Team"]:
    page_dict["Machine Learning"] = ml_pages

if page_dict:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])


if role:
    st.markdown("### Welcome!")
    st.write("Here’s a quick overview of the available sections based on your role:")

    with st.expander("Visualization"):
        st.write("Explore dashboards and interactive maps to understand key metrics and spatial data.")

    if role in ["Professor", "Team"]:
        with st.expander("Exploratory Analysis"):
            st.write("Dive into datasets to uncover patterns, distributions, and insights using EDA tools.")

        with st.expander("Machine Learning"):
            st.write("Build and evaluate predictive models using machine learning techniques.")

    with st.expander("Account"):
        st.write("Manage your preferences or sign out of the application.")

pg.run()