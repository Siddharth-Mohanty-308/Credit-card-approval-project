import streamlit as st

col1, col2 = st.columns(2,3)

with col1:
  st.header("Column 1")
  st.write("Add image")
  st.markdown("[My LinkedIn id](https://www.linkedin.com/in/siddharth6791/)")
  st.markdown("[My email](siddharth6791@gmail.com)")

with col2:
  st.header("Column 2")
  st.markdown("### Siddharth Mohanty")
  st.write("Add info about me section")
  # st.image("my_image.png", caption="This is an example image", use_column_width=True)
