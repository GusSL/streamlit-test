from cProfile import label
import pandas as pd
import streamlit as st

st.title('Welcome to my pandas basic tutorial 📊')

st.image("pandas.gif")

st.markdown("Here we will be discussing about pandas DataFrame Operations.")

st.markdown("Our example dataset will be:")

df = pd.DataFrame({
      'A': [1, 2, 3, 4],
      'B': [5, 6, 7, 8]
    })

st.write(df)

st.markdown("Let's take a look at a line plot using this DF:")

st.line_chart(df)

st.markdown('First we can use common aritmethic operators between columns:')

st.code("df['A'] + df['B']")
st.write(df['A'] + df['B'])

st.code("df['A'] - df['B']")
st.write(df['A'] - df['B'])

st.code("df['A'] * df['B']")
st.write(df['A'] * df['B'])

st.code("df['A'] / df['B']")
st.write(df['A'] / df['B'])

st.markdown('You can also use those aritmethic operators with constant variables:')

value = st.slider('Pick a number', 0, 10)

st.code("df['A'] + {}".format(value))
st.write(df['A'] + value)

st.code("df['A'] - {}".format(value))
st.write(df['A'] - value)

st.code("df['A'] * {}".format(value))
st.write(df['A'] * value)

st.code("df['A'] / {}".format(value))
st.write(df['A'] / value)

st.header("You have made it to the end! Click here to celebrate!")

def celeb():
  st.success("You did it!")
  st.balloons()

st.button(label="Activate celebration!", on_click=celeb)