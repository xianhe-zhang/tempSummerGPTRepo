import streamlit as st
import datetime
from streamlit import session_state as state

st.title('Who you are.')

with st.form("my_form"):
    state.dob = st.date_input("DOB", datetime.date.today(), max_value=datetime.date.today(), min_value = datetime.date(1950,1,1))
    state.gender = st.radio("Gender", ('Male', 'Female', 'Other'))
    state.city = st.text_input('City')
    state.financial_knowledge = st.radio("How would you evaluate your financial knowledge?", 
                                        ('Very good', 'Good', 'Fair', 'Not good', 'Poor'))
    state.is_international = st.radio("Are you an international student?", ('Yes', 'No'))
    state.school = st.text_input('Which school are you expecting to enroll?')
    state.program = st.text_input('What program are you expecting to enroll?')
    state.major = st.text_input('What major are you expecting to enroll?')
    state.speciality = st.text_input('What specialty are you expecting to enroll?')
    state.term = st.selectbox('Which term are you expecting to enroll in?',('Fall', 'Spring', 'Winter'))
    state.year = st.text_input('Enrollment year')
    st.text("Which of the following topics do you need help with?")
    state.is_student_loan = st.checkbox("Student Loan")
    state.is_financial_aid = st.checkbox("Financial Aid")
    state.is_scholarship_grant = st.checkbox("Scolarship and Grant")
    state.is_financial_budget = st.checkbox("Financial Budget")
    state.is_bank_account = st.checkbox("Opening· a Bank Account")
    state.is_creditcard = st.checkbox("Credit Card Recommendation")
   # Every form must have a submit button.
    state.submitted = st.form_submit_button("Submit")
    if state.submitted:
        st.write("Information Saved Successfully at "+str(datetime.datetime.now().strftime('%Y-%m-%d, %H:%M')))


