import streamlit as st
import datetime
from streamlit import session_state as state


if not state.submitted:
    st.write("No information available, we cannot help you")
else:
    
    st.write("TODO: May need more questions to this specific topic -> Generate Template based on information -> Send to ChatGPT -> Generate graphs/charts for visualization.")