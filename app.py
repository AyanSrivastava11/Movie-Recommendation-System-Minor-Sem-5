import streamlit as st
import page1
import about_us

# Set the page configuration
st.set_page_config(
    page_title='Movie Recommendation App',
    page_icon='🎬',
    layout='wide'
)

# Sidebar navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Home', 'Movie Recommendation', 'About Us'])

# Display the selected page
if page == 'Home':
    st.title('Home Page')
    st.write("Welcome to the Movie Recommendation App!")
elif page == 'Movie Recommendation':
    page1.show()
elif page == 'About Us':
    about_us.show()
