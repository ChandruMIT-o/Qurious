import streamlit as st
import pandas as pd
import numpy as np

if 'key' not in st.session_state:
    st.session_state['key'] = -1

if 'question' not in st.session_state:
    st.session_state['question'] = 1

my_bar = st.progress(0, text=f"Progress: {st.session_state['question'] + 1} out of 5 questions")
my_bar.progress(st.session_state['question'] * 20, text=f"Progress: {st.session_state['question'] + 1} out of 5 questions")

# st.set_page_config(layout="wide")

def question_section(question, options, answer, description):

    cols = st.columns(4)
    with cols[0]:
        st.info(f"Question {st.session_state['question'] + 1}")

    st.code(question, language=None)

    col1, col2 = st.columns(2)

    with col1:
        if st.session_state['key'] == 0:
            cb1 = st.checkbox(options[0], True, key = options[0])
        else: 
            cb1 = st.checkbox(options[0], False, key = options[0])

        if cb1: 
            st.session_state['key'] = 0

        if st.session_state['key'] == 1:
            cb2 = st.checkbox(options[1], True, key = options[1])
        else: 
            cb2 = st.checkbox(options[1], False, key = options[1])

        if cb2: st.session_state['key'] = 1

    with col2:
        if st.session_state['key'] == 2:
            cb3 = st.checkbox(options[2], True, key = options[2])
        else: 
            cb3 = st.checkbox(options[2], False, key = options[2])

        if cb3: st.session_state['key'] = 2

        if st.session_state['key'] == 3:
            cb4 = st.checkbox(options[3], True, key = options[3])
        else: 
            cb4 = st.checkbox(options[3], False, key = options[3])

        if cb4: st.session_state['key'] = 3
    
    if not (cb1 or cb2 or cb3 or cb4): 
        st.session_state['key'] = -1
    
    if st.button("Verify answer", type="secondary", key = question):

        if st.session_state['key'] != -1:

            if options[st.session_state['key']] == answer:
                st.success(f"Correct answer ({answer})")

                with st.expander("Explanation"):
                    st.code(description)

                return True
            
            else:
                st.error("Incorrect! The right answer is "+answer)

                with st.expander("Explanation"):
                    st.code(description, language=None)
                return True
        else:
            st.error("Choose an option!")
            return False
    else: return False

df = pd.read_csv("data/data.csv")

description = """Elements are the basic substances that make up all matter, and they are defined by the number of protons in their atoms. Atoms can combine to form molecules, but when an atom is broken down further, it loses its elemental identity.

Scientists have been able to further break down atoms into subatomic particles, such as protons, neutrons and electrons, but these particles themselves don’t exhibit the same chemical properties as whole atoms.

While we can break down atoms into smaller particles, these particles  themselves are not considered elements and don’t retain the defining characteristics of the original atom."""

row = df.loc[st.session_state['question']]

temp = question_section(row['Question'], [row['Option 1'], row['Option 2'], row['Option 3'], row['Option 4']], row['Answer'], description)

cols = st.columns(3)

with cols[0]:
    if (st.session_state['question'] > 0):
        if st.button("Previous Question", type='primary'):
            st.session_state['question'] = st.session_state['question'] + 1
with cols[1]:
    if temp:
        if st.button("Next Question", type='primary'):
            st.session_state['question'] = st.session_state['question'] + 1


