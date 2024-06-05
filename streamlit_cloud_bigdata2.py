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
    github_url = 'https://raw.githubusercontent.com/사용자명/저장소명/브랜치명/파일경로.csv'

    # 파일 다운로드
    csv_file_path = download_csv_from_github(github_url)
    
    # CSV 파일 읽기
    df1 = pd.read_csv(csv_file_path)
    
    # Streamlit 앱 시작
    st.title('깃허브 데이터 시각화')
    
    st.write('CSV 파일 데이터:')
    st.write(data)


    
    # 데이터 불러오기
    
    
    # 변수 설정
    years = ['2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']
    columns_of_interest = ['소득분위별(1)', '특성별(1)','특성별(2)'] + years
    income_levels = ['1분위', '2분위', '3분위', '4분위', '5분위']
    categories = ['성별', '연령별', '학력별', '종사자지위별']
    genders = ['남성','여성']
    ages = ['20대 이하', '30대', '40대', '50대', '60대 이상']
    educations = ['중졸이하','고교재학/고졸', '대재이상']
    employee_statuses = ['임금 근로자','일용 근로자','고용원이 없는 자영업자','고용원을 둔 사업주','무급가족 종사자','전업주부/학생/무직']
    
    # 데이터 필터링
    df1_filtered = df1[columns_of_interest]
    
    # 사용자 입력 받기
    st.title("가구원 비율 계산기")
    
    years_input = st.selectbox("연도별 (2007~2021):", years)
    income_level_input = st.selectbox("소득분위 (1-5):", income_levels) + "분위"
    gender_input = st.selectbox("성별:", genders)
    age_input = st.selectbox("연령별:", ages)
    education_input = st.selectbox("학력별:", educations)
    employee_status_input = st.selectbox("종사자지위별:", employee_statuses)
    
    # 데이터 추출 및 배열화
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
    
    # 결과 계산 및 출력
    cal = 1
    for value in data_dict.values():
        cal *= (value/100)
    
    
    cal = round(cal, 8)
    
    st.write(f"{years_input}년도에 가구원: 가구 내 작년 한해 동안 소득이 있거나 소득 활동을 한 가구원 중 \n소득{income_level_input}  \n성별 : {gender_input}\n연령대 :  {age_input}\n교육수준 : {education_input}\n종사자지위 : {employee_status_input} \n\n해당하는 비율")
    st.write("비율 :" + str(cal) + '%')


