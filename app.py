#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


# In[7]:


image = Image.open('search.jpg')
st.sidebar.image(image,width=120)


# In[8]:


st.sidebar.subheader("SELECT SIMILARITY SEARCH METHOD")
add_selectbox = st.sidebar.radio("  ",
    ("Artistic Style", "FAISS")
)


# In[12]:


if add_selectbox == 'Artistic Style' :
    st.title("Similar Products using Artistic Style Search")
    st.write("-------------------------------------------------------------------------------------------------")
    def get_data():
        return pd.read_csv('Artistic.csv')
    n=1
    df = get_data()
    images = df['0'].unique()
    #images1 = df['second']
    st.subheader("Select a Product :")
    pic = st.selectbox('Choices:', images)
    st.write("**You selected:**")
    st.image(pic,width=None)
    z = st.slider('Select Number of Similar Product:', 1, 10, 5)
    st.write("-------------------------------------------------------------------------------------------------")
    st.subheader("Output:")
    st.write('Similar Products: ')
    for index, row in df.iterrows():
        if row['0']==pic:
            while n < z+1:
            
                st.image(row[n], use_column_width=None, caption=row[n])
                n+=1

elif add_selectbox == 'FAISS':
    st.title("Similar Products using Faiss - Facebook AI Similarity Search")
    st.write("-------------------------------------------------------------------------------------------------")
    def get_data():
        return pd.read_csv('faiss.csv')
    n=1
    df = get_data()
    images = df['0'].unique()
    #images1 = df['second']
    st.subheader("Select a Image :")
    pic = st.selectbox('Choices:', images)
    st.write("**You selected:**")
    st.image(pic,width=None)


    z = st.slider('Select Number of Similar Products:', 1, 9, 5)
    st.write("-------------------------------------------------------------------------------------------------")
    st.subheader("Output:")
    st.write('**Similar Products:**')
    for index, row in df.iterrows():
        if row['0']==pic:
            while n < z+1:
            
                st.image(row[n], use_column_width=None, caption=row[n])
                n+=1


# In[ ]:




