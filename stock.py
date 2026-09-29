import yfinance as yf
import streamlit as st
import datetime



st.title("Building Stock market app")
st.header("Learn stock market using streamlit", divider='gray')

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Please enter starting date", datetime.date(2019, 1, 1))

with col2:
    end_date = st.date_input("Please enter starting date", datetime.date.today())

ticket_name = st.text_input("Enter the ticker of stock",'MSFT', key='placeholder')



if st.button('Apply'):
    msyf = yf.Ticker(ticket_name)
    hist = msyf.history(start= start_date, end = end_date)
    st.dataframe(hist)

    st.write('Closing price')
    st.line_chart(hist.Close)

    st.write(f'Volume of {ticket_name} stock')
    st.line_chart(hist.Volume)