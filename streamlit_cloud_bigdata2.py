# -*- coding: utf-8 -*-
"""streamlit_cloud_bigdata2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1E7fsPezSpTx4l68FrDKz_Qhnf42_bA9j
"""

def run_streamlit_app2():
    
    import streamlit as st
    import pandas as pd
    import os
    
    # 파일 저장 경로 설정
    github_url = 'https://raw.githubusercontent.com/nsg716/test_streamlit_cloud/master/test.csv'
    
    # CSV 파일 읽기
    df1 = pd.read_csv(github_url)
        
    years = ['2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']
    columns_of_interest = ['소득분위별(1)', '특성별(1)','특성별(2)'] + years
    income_levels = ['1분위', '2분위', '3분위', '4분위', '5분위']
    categories = ['성별', '연령별', '학력별', '종사자지위별']
    genders = ['남성','여성']
    ages = ['20대 이하', '30대', '40대', '50대', '60대 이상']
    educations = ['중졸이하','고교재학/고졸', '대재이상']
    employee_statuses = ['임금 근로자','일용 근로자','고용원이 없는 자영업자','고용원을 둔 사업주','무급가족 종사자','전업주부/학생/무직']
    
    df1_filtered = df1[columns_of_interest]
    
    st.title("데이터 추출 및 배열화")
    
    # 사용자 입력 받기
    years_input = st.text_input("연도를 입력하세요 (2007~2021)")
    income_level_input = st.text_input("소득분위를 입력하세요 (1-5)")
    gender_input = st.text_input("성별을 입력하세요")
    age_input = st.text_input("연령을 입력하세요")
    education_input = st.text_input("학력을 입력하세요")
    employee_status_input = st.text_input("종사자지위를 입력하세요")
    data_dict = {}
    
    for income_level in income_levels:
        if income_level == income_level_input:
            for category in categories:
                for gender in genders:
                    if gender == gender_input:
                        key = f"{category}_{income_level}_{gender}"
                        data = df1_filtered[
                            (df1_filtered['소득분위별(1)'] == income_level) &
                            (df1_filtered['특성별(1)'] == category) &
                            (df1_filtered['특성별(2)'] == gender)
                        ]
                        if not data.empty:
                            data_dict[key] = data[years_input].values.flatten()
    
                for age in ages:
                    if age == age_input:
                        key = f"{category}_{income_level}_{age}"
                        data = df1_filtered[
                            (df1_filtered['소득분위별(1)'] == income_level) &
                            (df1_filtered['특성별(1)'] == category) &
                            (df1_filtered['특성별(2)'] == age)
                        ]
                        if not data.empty:
                            data_dict[key] = data[years_input].values.flatten()
    
                for education in educations:
                    if education == education_input:
                        key = f"{category}_{income_level}_{education}"
                        data = df1_filtered[
                            (df1_filtered['소득분위별(1)'] == income_level) &
                            (df1_filtered['특성별(1)'] == category) &
                            (df1_filtered['특성별(2)'] == education)
                        ]
                        if not data.empty:
                            data_dict[key] = data[years_input].values.flatten()
    
                for employee_status in employee_statuses:
                    if employee_status == employee_status_input:
                        key = f"{category}_{income_level}_{employee_status}"
                        data = df1_filtered[
                            (df1_filtered['소득분위별(1)'] == income_level) &
                            (df1_filtered['특성별(1)'] == category) &
                            (df1_filtered['특성별(2)'] == employee_status)
                        ]
                        if not data.empty:
                            data_dict[key] = data[years_input].values.flatten()
    
    st.write("추출된 데이터:")
    for key, value in data_dict.items():
        st.write(f"{key}: {value}")
    
    # 결과 계산 및 출력
    cal = 1
    for value in data_dict.values():
        cal *= (value/100)
    cal = cal[0]
    
    cal = round(cal, 8)
    
    st.write(f"{years_input}년도에 가구원: 가구 내 작년 한해 동안 소득이 있거나 소득 활동을 한 가구원 중 \n소득{income_level_input}  \n성별 : {gender_input}\n연령대 :  {age_input}\n교육수준 : {education_input}\n종사자지위 : {employee_status_input} \n\n해당하는 비율")
    st.write("비율 :" + str(cal) + '%')



