import streamlit as st
import sympy as sym
import time


col1 = st.columns([1,1,1])

with col1[0]:
    param_button1 = st.button("+1する")
with col1[1]:
    param_button2 = st.button("リセットする")

with col1[2]:
    param_button3 = st.button("更新ボタン")

if 'num' not in st.session_state :
    st.session_state['num'] = 0
    st.write(f"{st.session_state['num']}になりました．")

if param_button1 :
    st.session_state['num'] += 1
    st.write(f"{st.session_state['num']}になりました．")


if param_button2 :
    st.session_state['num'] =0
    st.write(f"{st.session_state['num']}になりました．")

col2 = st.columns([1,1,1])
with col2[0]:
    param_button3 = st.button("start")
with col2[1]:
    param_button4 = st.button("stop")
with col2[2]:
    param_button5 = st.button("reset")

num = int(st.text_input("itelation","100"))
# with st.empty():
#     num_inital = st.session_state['num']
#     if param_button3 :
#         for i in range(num_inital,num,1):
#             st.metric("Count","Number = %s"%(i+1))
#             if i < 10 :
#                 time.sleep(1)
#             elif 10 <= i < 25:
#                 time.sleep(0.5)
#             else :
#                 time.sleep(0.25)
#             st.session_state['num']=i+1
#     if param_button4 :
#         st.stop()
#     if param_button5 :
#         st.session_state['num'] = 0

with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")