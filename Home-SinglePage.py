import streamlit as st
import datetime

def main():
    # 用户选择功能
    option = st.selectbox('选择功能', ['主页', '设置', '帮助'])

    # 根据用户选择展示不同的内容
    if option == '主页':
        show_home_page()
    elif option == '设置':
        show_settings_page()
    elif option == '帮助':
        show_help_page()

def show_home_page():
    st.title('欢迎来到主页')
    # 在主页上展示相关内容

    if st.button('跳转到设置页'):
        show_settings_page()

def show_settings_page():
    st.title('设置')
    # 在设置页面上展示相关内容
    

    if st.button('跳转到主页'):
        st.session_state.page = '主页'  # 更新状态变量
    with st.form("my_form"):
        dob = st.date_input("DOB", datetime.date.today(), max_value=datetime.date.today(), min_value = datetime.date(1950,1,1))
        gender = st.radio("Gender", ('Male', 'Female', 'Other'))
        city = st.text_input('City')
        financial_knowledge = st.radio("How would you evaluate your financial knowledge?", 
                                            ('Very good', 'Good', 'Fair', 'Not good', 'Poor'))
        is_international = st.radio("Are you an international student?", ('Yes', 'No'))
        school = st.text_input('Which school are you expecting to enroll?')
        program = st.text_input('What program are you expecting to enroll?')
        major = st.text_input('What major are you expecting to enroll?')

def show_help_page():
    st.title('帮助')
    # 在帮助页面上展示相关内容

    if st.button('跳转到主页'):
        st.session_state.page = '主页'  # 更新状态变量

if __name__ == '__main__':
    if 'page' not in st.session_state:
        st.session_state.page = '主页'  # 初始化状态变量

    main()