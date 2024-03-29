import streamlit as st
import pathlib, sys
module_dir = pathlib.Path(__file__).parent.parent
sys.path.append(str(module_dir))
import backend.get_keys as gk
import pandas as pd

def disp(cursor):
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
    with st.container():
        def submitted():
            st.session_state.submitted = True
        def reset():
            st.session_state.submitted = False
        def create_user_registration():
            with st.expander("Register New User Here:"):
                with st.form("my_form",clear_on_submit=True):
                    st.text_input("Username",key="uname")
                    st.text_input("Password",type='password',key='Pass')
                    st.text_input("First Name",key='f_name')
                    st.text_input("Middle Initials",key='minit')
                    st.text_input("Last Name",key='l_name')
                    st.selectbox("Authorization Level",['0','1','2'],index=2,key='auth_lvl')
                    st.form_submit_button("Submit",on_click=submitted)
        if 'submitted' in st.session_state:
            if st.session_state.submitted == True:
                uname = st.session_state.uname
                Pass = st.session_state.Pass
                f_name = st.session_state.f_name
                minit = st.session_state.minit
                l_name = st.session_state.l_name
                auth_lvl = st.session_state.auth_lvl
                gk.add_usr(uname,Pass,f_name,minit,l_name,auth_lvl)
                st.success("New User added")
                reset()
        reset()
        create_user_registration()
                