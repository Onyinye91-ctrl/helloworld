import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')
st.write('Hello, *World!* :sunglasses:')

st.write(1,2,3,4)

df = pd.DataFrame({
    'first_columns': [1, 2, 3, 4],
    'second column': [10, 20, 20, 10]
})
st.write(df)

st.write('Below is a Dataframe: ', df, 'Above is a Dataframe')

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a','b','c']
)
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b',size='c', tooltip=['a','b','c']
)
st.write(c)