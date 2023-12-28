## making streamlit app
import streamlit as st

## making if else statement with streamlit showing different messages depending on if the button was pressed or not
st.header('st.button')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')