import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])


st.line_chart(chart_data)


st.header('Line chart using randint function')
chart_data2 = pd.DataFrame(
     np.random.randint(5, size=(10, 3)),
    columns=['Day1', 'Day2', 'Day3']
     )
st.line_chart(chart_data2)


st.header('Line chart using rand function')
chart_data3 = pd.DataFrame(
     np.random.rand(10, 4),
    columns=['Day1', 'Day2', 'Day3', 'Day4']
     )
st.line_chart(chart_data3)