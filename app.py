import streamlit as st
import yfinance as yf
import pandas as pd 
import plotly.graph_objects as go

#untuk reference streamlit buka di wwww.docs.streamlit.io/library/api-reference 

yf.Ticker('goto.jk').history(period='10d') #untuk tau ada apa saja dan penulisan nama kolomnya

st.title('Yahoo Finance! Dashboard')

#karena tidak enak dilihat, maka dibuat 2 columns tampilan:
col1, col2 = st.columns(2)
with col1:
    saham = st.text_input('Kode Saham') #liat di www.docs.streamlit.io/library/api-reference/chart
with col2:
    waktu = st.selectbox('Periode',['1d','5d','1mo','1y','5y','10y','ytd','max'],index=3) #index=3 adalah menentukan default(karena integer jadinya 0=1d, 1=5d dst.), jadi selalu dibelakang
#data = yf.Ticker('goto.jk').history(period='max').reset_index()
#data = yf.Ticker(saham).history(period='max').reset_index()
data = yf.Ticker(saham).history(period=waktu).reset_index()


if not data.empty: 
    #st.header('GOTO.JK')
    st.header(saham)
    fig = go.Figure(
        data=go.Candlestick(
            x=data['Date'],
            open=data['Open'],
            high=data['High'],
            low=data['Low'],
            close=data['Close']
        )
    )

#col1, col2 = st.columns(2) #buat 2 columns 
#with col1:
    #st.plotly_chart(fig, use_container_width=True)

#with col2:
    #st.plotly_chart(go.Figure(), use_container_width=True)

    st.plotly_chart(fig)
else:
    st.caption('Data saham tidak tersedia ...')
