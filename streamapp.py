import pandas
import streamlit as st
import os, os.path

for root, _, files in os.walk('datasets/daily1'):
    for f in files:
        fullpath = os.path.join(root, f)
        try:
            if os.path.getsize(fullpath) < 1 * 1024:   #set file size in kb
                os.remove(fullpath)
        except WindowsError:
            none
            
Consol = []
Break = []
def is_consolidating(df, percentage=2):
    recent_candlesticks = df[-10:]
    #print(percentage)
    max_close = recent_candlesticks['Close'].max()
    min_close = recent_candlesticks['Close'].min()

    threshold = 1 - (percentage / 100)
    if min_close > (max_close * threshold):
        return True        
    
    return False

def is_breaking_out(df, percentage=4):
    last_close = df[-1:]['Close'].values[0]

    if is_consolidating(df[:-1], percentage=percentage):
        recent_closes = df[-11:-1]

        if last_close > recent_closes['Close'].max():
            return True

    return False

for filename in os.listdir('datasets/daily1'):
    df = pandas.read_csv('datasets/daily1/{}'.format(filename))
    
    if is_consolidating(df, percentage=3.5):
        st.markdown(filename + " is consolidating")
    if is_breaking_out(df):
        st.markdown(filename + " is Breaking Out")
