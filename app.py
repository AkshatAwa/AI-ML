import streamlit as st

st.set_page_config(
    page_title="Just a Demo for AI/ML projects CaC",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("Welcome to the demo!")
st.write("👈 Select a bot from the sidebar to interact with it.")

st.markdown(
    """
    This is a demonstration of a multi-page Streamlit application.
    Each bot page in the sidebar represents a separate module
    where you can implement different functionalities or AI models.

    **How to use:**
    - Navigate using the sidebar on the left.
    - Each page (`Bot 1` to `Bot 4`) has its own functionality.
    - You can add more bots by creating new Python files in the `pages` directory.
    """
)
st.info("This is the main landing page. Explore the different bots!")

st.markdown("just a footer for the demo app")