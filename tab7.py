import streamlit as st
import get_keys as gk
import pandas as pd

def disp(cursor):
    with st.container():
        def submitted():
            st.session_state.submitted = True
        def reset():
            st.session_state.submitted = False
        def create_user_registration():
            with st.form("my_form"):
                st.text_input("Username",key="uname")
                st.text_input("Password",type='password',key='Pass')
                st.text_input("First Name",key='f_name')
                st.text_input("Middle Initials",key='minit')
                st.text_input("Last Name",key='l_name')
                st.selectbox("Authorization Level",['0','1','2'],index=2,key='auth_lvl')
                st.form_submit_button("Submit",on_click=submitted)
            st.button("Cancel",on_click=reset)
        if 'submitted' in st.session_state:
            # print("First Phase")
            if st.session_state.submitted == True:
                # print("Second Phase")
                uname = st.session_state.uname
                Pass = st.session_state.Pass
                f_name = st.session_state.f_name
                minit = st.session_state.minit
                l_name = st.session_state.l_name
                auth_lvl = st.session_state.auth_lvl
                # st.write(data_dict)
                gk.add_usr(uname,Pass,f_name,minit,l_name,auth_lvl)
                reset()
                st.success("New User added")
        if st.button("Register"):
            reset()
            create_user_registration()
        with st.container():
            user_input = st.text_area("Enter text here",placeholder='SELECT * FROM Airlines;')
            if st.button("Run Query"):
                cursor.execute(user_input)
            # del cols
            if cursor.description!=None:
                cols=[i[0] for i in cursor.description]
                rows=cursor.fetchall()
                st.dataframe(pd.DataFrame(rows,columns=cols))
                st.success("retrieved successfully")
                