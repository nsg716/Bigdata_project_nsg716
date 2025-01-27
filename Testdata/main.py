# -*- coding: utf-8 -*-
"""메인 메뉴.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1urCxg8hWh5z9vaNBz8eb_clg0ULrfbKd
"""

import streamlit as st
from streamlit_cloud_bigdata1 import run_streamlit_app1 as streamlit_cloud_bigdata1_app
from streamlit_cloud_bigdata3 import run_streamlit_app3 as streamlit_cloud_bigdata3_app

PAGES = {
    "소득분위별 순자산,부채,소득,소비" :  streamlit_cloud_bigdata1_app,
    "자산,소비에 따른 소득분위 예측": streamlit_cloud_bigdata3_app
}

st.sidebar.title('메뉴')
selection = st.sidebar.radio("페이지를 선택하세요:", list(PAGES.keys()))

page = PAGES[selection]
page()
