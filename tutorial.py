import streamlit as st
st.set_page_config(page_title='My Streamlit')
mymenu=st.sidebar.selectbox('My Menu',('Home','Fillform','Download'))
st.image('https://onleitechnologies.com/wp-content/uploads/2021/12/cropped-Untitled_design__6_-removebg-preview-1.png')
st.title('Onlei Technologies')
st.header('By Rahul Khanchandani')
st.text('This a tutorial of streamlit')
if(mymenu=='Home'):
    st.markdown('<centre><h1>WELCOME</h1></scentre>',unsafe_allow_html=True)
    st.video('https://www.youtube.com/watch?v=88K_kvi-IRM')
elif(mymenu=='Fillform'):
    with st.form('My Form'):
        name=st.text_input('Enter your Name')
        dob=st.date_input('choose date of birth')
        marks=st.slider('Choose Marks')
        k=st.form_submit_button('Submit Form')
        if k:
            st.write('Name:',name,'DOB:',dob,'Marks:',marks)
elif(mymenu=='Download'):
    st.header('Download')
    st.download_button('Download Now','hello this a download data','onlei.txt')
