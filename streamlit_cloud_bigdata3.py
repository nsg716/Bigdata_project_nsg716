# -*- coding: utf-8 -*-
"""streamlit_cloud_bigdata3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Iyq5rHYSMcBNsDVZ5u58URtY3bVJuD40
"""

from matplotlib import font_manager
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score




def run_streamlit_app3():
    import streamlit as st
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    
    # Nanum Gothic 폰트 설정
    font_path = "NanumGothic.ttf"
    font_prop = font_manager.FontProperties(fname=font_path)
    plt.rc('font', family=font_prop.get_name())
    
    
    # 주어진 데이터
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
    
    # DataFrame으로 변환
    consumption_df = pd.DataFrame(consumption_data)
    asset_df = pd.DataFrame(asset_data)
    income_df = pd.DataFrame(income_data)
    
    # 데이터 병합
    merged_df = pd.DataFrame()
    
    for year in range(2012, 2022):
        temp_df = pd.DataFrame({
            '소득분위별': consumption_df['소득분위별'],
            '연도': year,
            '소비': consumption_df[str(year)],
            '자산': asset_df[str(year)],
            '소득': income_df[str(year)]
        })
        merged_df = pd.concat([merged_df, temp_df])
    
    # Streamlit 앱 시작
    st.title("소득, 자산, 소비 데이터 분석")
    
    
    # 독립 변수와 종속 변수 선택
    X = merged_df[['자산', '소비']]
    y = merged_df['소득']
    
    # 데이터 분할 (학습 데이터와 테스트 데이터)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 선형 회귀 모델 생성
    model = LinearRegression()
    
    # 모델 훈련
    model.fit(X_train, y_train)
    
    # 예측
    y_pred = model.predict(X_test)
    
    # R² 점수 계산
    r2 = r2_score(y_test, y_pred)
    st.write(f'R² 점수: {r2}')
    
    # 모델 평가 (평균 제곱 오차)
    mse = mean_squared_error(y_test, y_pred)
    st.write("Mean Squared Error:", mse)
    
    # 회귀 계수 확인
    st.write("Intercept (절편):", model.intercept_)
    
    # 모델의 계수 가져오기
    asset_coef, consume_coef = model.coef_
    
    # 계수를 설명과 함께 출력
    st.write(f"Coefficients (계수):")
    st.write(f"  자산: {asset_coef:.4f}")
    st.write(f"  소비: {consume_coef:.4f}")
    import streamlit as st
    import matplotlib.pyplot as plt
    import numpy as np  # NumPy 추가
    
    # 가정: model.predict 함수가 이미 정의되어 있고 사용 가능하다.
    # 예를 들어, 미리 학습된 모델을 불러오는 코드가 필요할 수 있습니다.
    
    # Streamlit 앱의 제목 설정
    st.write('연도별 소득 분위 및 예상 소득 비교')
    
    # 사용자 입력 받기
    asset = st.number_input("현재 (혹은 예상)자산을 입력하세요 (단위 만 원):", min_value=0, value=0, step=100)
    consumption = st.number_input("현재 (혹은 예상) 1년당 소비를 입력하세요 (단위 만 원):", min_value=0, value=0, step=100)
    
    # 데이터 준비
    data_input = [[asset, consumption]]
    predicted_income_data = model.predict(data_input)
    
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
    
    # 연도별로 데이터 정리
    years = [year for year in income_data.keys() if year.isnumeric()]
    income_values = [income_data[year] for year in years]
    predicted_incomes = [predicted_income_data for _ in years]
    
    # 그래프 그리기
    fig, ax = plt.subplots(figsize=(10, 6))
    for i in range(5):  # 5개의 소득 분위
        ax.plot(years, [income[i] for income in income_values], label=income_data['소득5분위'][i])
    ax.plot(years, predicted_incomes, label='예측 소득', linestyle='--', color='red')
    ax.set_xlabel('연도', fontproperties=font_prop)
    ax.set_ylabel('소득', fontproperties=font_prop)
    ax.set_title('연도별 소득 분위' ,fontproperties=font_prop)
    ax.legend(prop=font_prop)
    plt.xticks(rotation=45)  # x축 레이블 회전
    plt.grid(True)
    plt.tight_layout()  # 그래프 레이아웃 조정
    
    # Streamlit을 사용하여 그래프 표시
    st.pyplot(fig)
    
    st.write(f"1년 예상 소득 (만 원): {str(*predicted_income_data)}")
    
    # 각 연도별로 소득 분위와 예측 소득 사이의 차이를 백분율로 계산 및 표시
    for year, incomes, predicted_income in zip(years, income_values, predicted_incomes):
        st.write(f"{year}년도 소득 분위별 차이 (%):")
        for i, income in enumerate(incomes):
            # 예측 소득과 실제 소득 사이의 차이를 백분율로 계산
            difference_percentage = ((predicted_income[0] - income) / income) * 100
            st.write(f"  소득 {i+1}분위: {difference_percentage:.2f}%")
        st.write("")

    
    
    
    # Train the linear regression models
    years = [year for year in income_data.keys() if year.isnumeric()]
    income_values = [income_data[year] for year in years]
    
    X = np.array([int(year) for year in years]).reshape(-1, 1)
    models = []
    
    for i in range(5):
        y = np.array([income[i] for income in income_values])
        model = LinearRegression()
        model.fit(X, y)
        models.append(model)
    
    # Generate predicted data from 2022 to 2026
    future_years = list(range(2022, 2027))
    future_incomes = []
    
    for i in range(5):
        future_income = []
        for year in future_years:
            income = models[i].predict([[year]])
            future_income.append(income[0])
        future_incomes.append(future_income)
    
    # Display the results
    st.title("소득 분위별 예측 결과")
    
    for i in range(5):
        st.subheader(f"소득 {i+1}분위 예측 결과:")
        for j, year in enumerate(future_years):
            st.write(f"{year}년도 예상 소득: {future_incomes[i][j]:.2f} 만 원")
        st.write()
    
    # Create the chart
    st.subheader("소득 분위별 예측 결과 차트")
    predicted_incomes = [predicted_income_data for _ in future_years]
    
    fig, ax = plt.subplots(figsize=(12, 6))
    for i in range(5):
        ax.plot(future_years, future_incomes[i], label=income_data['소득5분위'][i])
    ax.plot(future_years, predicted_incomes, label='예측 소득', linestyle='--', color='red')
    ax.set_xlabel('년도',fontproperties=font_prop)
    ax.set_ylabel('소득 (만 원)',fontproperties=font_prop)
    ax.set_title('소득 분위별 예측 결과',fontproperties=font_prop)
    ax.legend(prop=font_prop)
    st.pyplot(fig)
    
    # Calculate the percentage difference between predicted and actual incomes
    for year, incomes, predicted_income in zip(future_years, income_values, predicted_incomes):
        min_difference = float('inf')
        min_difference_percentage = 0
        print(f"{year}년도 소득 분위별 차이 (%):")
        for i, income in enumerate(incomes):
             # 예측 소득과 실제 소득 사이의 차이를 백분율로 계산
             difference_percentage = ((predicted_income[0] - income) / income) * 100
             print(f"  소득 {i+1}분위: {difference_percentage:.2f}%")
             # 0에 가장 가까운 차이 값 찾기
             if abs(difference_percentage) < abs(min_difference):
                    min_difference = difference_percentage
                    min_difference_percentage = difference_percentage
        print(f"  이 년도 중 가장 가까운 차이: {min_difference_percentage:.2f}%")
        print()


