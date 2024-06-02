# -*- coding: utf-8 -*-
"""메인 메뉴.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1urCxg8hWh5z9vaNBz8eb_clg0ULrfbKd
"""

import streamlit as st
import streamlit_cloud_bigdata3


consumption_data = {
    '소득분위별': ['1분위', '2분위', '3분위', '4분위', '5분위'],
    '2012': [768.8, 1056.1, 1380.2, 1700.7, 2180.1],
    '2013': [739.3, 1053.5, 1436.8, 1722.9, 2288.6],
    '2014': [772.3, 1116.5, 1432.3, 1771.9, 2242.9],
    '2015': [783.9, 1134.2, 1465.7, 1771.8, 2342.9],
    '2016': [830.8, 1161.6, 1479.8, 1828.7, 2377.4],
    '2017': [857.5, 1214.4, 1559.2, 1907.6, 2405.6],
    '2018': [894.1, 1322.7, 1571.2, 1896.4, 2485.3],
    '2019': [933.2, 1294.7, 1650.9, 1933.0, 2478.5],
    '2020': [859.6, 1218.6, 1552.2, 1814.2, 2348.6],
    '2021': [964.3, 1295.2, 1616.4, 1884.3, 2384.9]
}

asset_data = {
    '소득5분위': ['소득1분위', '소득2분위', '소득3분위', '소득4분위', '소득5분위'],
    '2012': [9840, 16894, 23556, 34775, 76545],
    '2013': [10034, 18056, 24422, 35758, 75153],
    '2014': [10951, 19122, 25294, 36735, 75573],
    '2015': [11908, 19561, 26944, 37927, 77073],
    '2016': [11954, 20228, 28608, 40466, 81917],
    '2017': [12420, 21994, 31735, 44109, 83094],
    '2018': [13522, 23629, 34849, 46668, 91492],
    '2019': [13146, 23780, 35464, 48891, 94663],
    '2020': [13629, 25523, 36076, 49422, 98054],
    '2021': [16500, 28682, 39673, 56447, 109952]
}

income_data = {
    '소득5분위': ['소득1분위', '소득2분위', '소득3분위', '소득4분위', '소득5분위'],
    '2012': [683, 1705, 2805, 4173, 8014],
    '2013': [713, 1814, 2975, 4406, 8343],
    '2014': [721, 1951, 3160, 4630, 8632],
    '2015': [765, 1999, 3262, 4778, 8826],
    '2016': [796, 2064, 3347, 4929, 8969],
    '2017': [867, 2183, 3650, 5560, 10339],
    '2018': [918, 2275, 3760, 5709, 10692],
    '2019': [958, 2316, 3850, 5792, 10728],
    '2020': [1009, 2369, 3942, 5916, 10855],
    '2021': [1170, 2582, 4174, 6166, 11194]
}
def main() :
    st.title('선택화면')
    menu = ['소득 분위 및 조건을 통한 경제적 위치 확인', '소득분위별 순자산,부채,소득,소비', '자산,소비에 따른 소득분위 예측']
    choice = st.sidebar.selectbox('메뉴', menu)



    if choice == menu[2] :
        streamlit_cloud_bigdata3.analyze_income_asset_consumption(consumption_data,asset_data,income_data,font_path="NanumGothic.ttf")