import pickle
import streamlit as st

model1 = pickle.load(open('model.pkl', 'rb'))

def myf1():
  open = st.number_input('Enter the opening price of Tesla stock on the given day.')
  high = st.number_input('Enter the highest price of Tesla stock during the trading day.')
  low = st.number_input('Enter the lowest price of Tesla stock on the given day.')
  close = st.number_input('Enter the closing price of Tesla stock on the given day.')
  adj_close = st.number_input('Enter the cadjusted closing price of Tesla stock.')
  pred = st.button('predict')

  if(pred):
    op = model1.predict([[open, high, low, close, adj_close]])
    st.write('The trading volume of Tesla stock on the given day is: ', op)

myf1()
