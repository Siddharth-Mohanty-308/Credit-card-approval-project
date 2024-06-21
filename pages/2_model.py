import streamlit as st
import joblib
from sklearn import tree

model = joblib.load('decision_tree_model.joblib')
image_url="https://raw.githubusercontent.com/Siddharth-Mohanty-308/Credit-card-approval-project/main/readme_assets/conf_matrix_final.png"

st.markdown("### Model metrics")
st.caption("Confusion Matrix")
st.image(image_url)
st.markdown("### Model diagram")

dot_data=tree.export_graphviz(
    model,
    out_file=None
)

st.graphviz_chart(dot_data)
