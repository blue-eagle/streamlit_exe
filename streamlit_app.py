## making streamlit app
import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

## making if else statement with streamlit showing different messages depending on if the button was pressed or not
st.header('st.write')

# example1
st.write('Hello, *World!* :sunglasses:')

# example2
st.write(1234)

# esample3
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

# example4
st.write('This is a dataframe:', df, 'above is a dataframe')

# example5

df2 = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
)

st.write(c)