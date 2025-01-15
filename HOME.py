import numpy as np
import streamlit as st
import pandas as pd


st.title("Welcome to the Simulation Project (HBL BANK)")
st.subheader("Group Members:")
st.write("1. Hassan Ahmed Khan - B21110006041")
st.write("2. Osama Ahmed - B21110006104")
st.write("3. Sheraz Azghar - B21110006122")
st.write("4. Saad Sami Khan B2110006108")
st.write(" ")
st.title("1-Data")

df = pd.read_excel("./data/Goodness Of Fit Test(ChiSquare).xlsx", sheet_name="Sheet1")
df = df.astype(str)
data = df[:94]
# df.fillna("-", inplace=True)
st.dataframe(data,hide_index=True)

st.title("2-Chi square test")
st.subheader("i)GOODNESS OF FITNESS INTER-ARRIVAL")
header = df.iloc[94]  # This is the row you want to set as the header


# Create a new DataFrame with the row as the column names
IA_chiSquare = df.iloc[95:104].fillna("-")  # Data starting from row 95 to 104
IA_chiSquare.columns = header  # Set the extracted row as column names

# Display the updated DataFrame
# st.dataframe(IA_chiSquare)
st.dataframe(IA_chiSquare, hide_index=True)
st.markdown('<p style="color:green;">Ho is accepted: Inter arrival time for this data is in poisson distribution</p>', unsafe_allow_html=True)

st.subheader("ii)GOODNESS OF FITNESS SERVICE")
Sheader = df.iloc[106]  # This is the row you want to set as the header

# Create a new DataFrame with the row as the column names
S_chiSquare = df.iloc[107:120].fillna(" ")  # Data starting from row 95 to 104
S_chiSquare.columns = header  # Set the extracted row as column names

# Display the updated DataFrame
st.dataframe(S_chiSquare,hide_index=True)

st.markdown('<p style="color:green;">Ho is accepted:Service time for this data is in exponential distribution</p>', unsafe_allow_html=True)









