import streamlit as st

image_url = 'https://raw.githubusercontent.com/Siddharth-Mohanty-308/Credit-card-approval-project/main/pages/my_image.png'
col1, col2 = st.columns([2, 3])

with col1:
  st.image(image_url, use_column_width=True)
  st.markdown("[My LinkedIn id](https://www.linkedin.com/in/siddharth6791/)")
  st.markdown("email: siddharth6791@gmail.com")

with col2:
  st.header("Siddharth Mohanty")
  st.write("I am a recent Computer Science graduate with strong programming skills in Python, specializing in data science and visualization have equipped me with practical expertise in machine learning, data analysis, and software development.") 
  st.write("I am passionate about leveraging my technical skills to solve complex problems and drive innovation.")
