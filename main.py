import streamlit as st
from streamlit_elements import elements, mui, html

st.set_page_config(layout="wide")
st.image("assets/headerimg.png")
st.title("Qurious")
st.subheader("An AI Powered Quiz Application")

subjects = ['Mathematics', 'Botany', 'Zoology', 'Commerce', 'Computer Science', 'Physics', 'Chemistry', 'Literature']

subject = False

topics = {
    'Mathematics' : ['Algebra', 'Calculus', 'Probability', 'Arithmetic'],
    'Botany' : ['asd', 'dfg', 'we', 'ad']
}

url = {
    'Mathematics' : 'assets/image 2.png', 
    'Botany' : 'assets/image 3.png', 
    'Zoology' : 'assets/image 4.png', 
    'Commerce' : 'assets/image 5.png', 
    'Computer Science' : 'assets/image 6.png', 
    'Physics' : 'assets/image 7.png', 
    'Chemistry' : 'assets/image 8.png', 
    'Literature' : 'assets/image 1.png'
}

cols = st.columns(4)
i = 1
for x in subjects:
    with cols[i%4]:
        st.image(url[x])
        option = st.checkbox(x, key=x)
        if option:
            subject = x
    i+=1

if subject:
    # subject = st.selectbox("Select a Subject: ", subjects, index=0)

    topic = st.multiselect("Select a topic under "+subject, topics[subject], default=topics[subject][:2])

    st.write(subject)
    st.button("Start Quiz!", type='primary')