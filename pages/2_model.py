import streamlit as st
import joblib
import scikit-learn 

model = joblib.load('decision_tree_model.joblib')
st.markdown("### Model metrics")
# st.image()
st.markdown("### Model diagram")

dot_data=tree.export_graphviz(
    model,
    out_file=None
)

st.graphviz_chart(dot_data)
