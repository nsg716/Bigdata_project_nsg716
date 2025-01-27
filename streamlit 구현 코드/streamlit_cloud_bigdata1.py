# -*- coding: utf-8 -*-
"""streamlit_cloud_bigdata.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1g3dQFgftVT9qaDR8rijUybRQaX5ydl3_
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager
def run_streamlit_app1():
    # Nanum Gothic 폰트 설정
    font_path = "NanumGothic.ttf"
    font_prop = font_manager.FontProperties(fname=font_path)
    plt.rc('font', family=font_prop.get_name())
    

    
    
    # 사용자 입력
    st.title('가계 재무 데이터 비교')
    net_worth_input = st.number_input("모든 순자산을 입력하세요 (단위: 만 원): ", min_value=0)
    if net_worth_input == 0:
        net_worth_input = 1
    debt_input = st.number_input("모든 부채를 입력하세요 (단위: 만 원): ", min_value=0)
    if debt_input == 0:
        debt_input = 1
    total_income_data_input = st.number_input("모든 전체소득을 입력하세요 (단위: 만 원): ", min_value=0)
    if total_income_data_input == 0:
        total_income_data_input = 1
    labor_income_input = st.number_input("한 해 근로소득을 입력하세요 (단위: 만 원): ", min_value=0, value=1)
    if labor_income_input == 0:
        labor_income_input = 1
    consume_input = st.number_input("한 해 소비를 입력하세요 (단위: 만 원): ", min_value=0, value=1)
    if consume_input == 0:
        consume_input = 1
    if st.button('데이터 비교'):
        if net_worth_input == 0:
            net_worth_input = 1
        if debt_input == 0:
            debt_input = 1
        if total_income_data_input == 0:
            total_income_data_input = 1
        if labor_income_input == 0:
            labor_income_input = 1
        if consume_input == 0:
            consume_input = 1
        years = ['2007','2008','2009','2010','2011','2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
        x = years
        year_2021index = years.index('2021')  # 2021년에 해당하는 인덱스를 찾습니다.
        net_worth_data = {
            '순자산': [np.array([5747.7, 5294.9, 5245.5, 6488.7, 6169.4, 6314.5, 7654.8, 7736.1, 9925.3, 10092.5, 10966.8, 11073.2, 13078.6, 14410.8, 14897.2], dtype=float),
                      np.array([6599.3, 6932.6, 6599.3, 7573.9, 7912.8, 8293.8, 8967.5, 11029.7, 10236.4, 11480.3, 12470.1, 13653.4, 14931.7, 17484.3, 18726.2], dtype=float),
                      np.array([8170.3, 7653.2, 8596.2, 9458.9, 9826.7, 10847.5, 10747.6, 10164.5, 12470.4, 12597.7, 13074.4, 15030.0, 15583.1, 18632.5, 20284.7], dtype=float),
                      np.array([10521.1, 10737.3, 10984.1, 11540.5, 11174.8, 12376.3, 13024.7, 14605.6, 14308.5, 14376.2, 17056.6, 18001.8, 20859.2, 22519.2, 22989.6], dtype=float),
                      np.array([20275.0, 19735.9, 19580.9, 23210.8, 22546.0, 22137.1, 22919.1, 23206.2, 27076.2, 28804.4, 30539.3, 31307.3, 34303.2, 43489.2, 43927.8], dtype=float)],
        }
        
        debt_data = {
            '부채': [np.array([1017.1, 1125.7, 1021.8, 1108.2, 1064.8, 940.3, 953.3, 868.0, 860.7, 977.3, 1020.8, 1193.7, 885.4, 1286.4, 1248.5], dtype=float),
                    np.array([1387.6, 1334.0, 1115.2, 1291.1, 1243.1, 1479.7, 1417.6, 1394.9, 1246.3, 1089.0, 1894.7, 1498.6, 1453.1, 1495.1, 1700.3], dtype=float),
                    np.array([1369.8, 1601.9, 1488.6, 1850.3, 1655.6, 1617.4, 1724.8, 1874.7, 1821.7, 1941.1, 1693.7, 2208.9, 1994.6, 2315.3, 2193.7], dtype=float),
                    np.array([1939.9, 2206.3, 2003.6, 1937.3, 2443.0, 2342.2, 2535.8, 2773.2, 2515.4, 2791.8, 2811.7, 2906.6, 2875.3, 3187.6, 3133.9], dtype=float),
                    np.array([3866.1, 3655.3, 3674.5, 4612.9, 4564.8, 4638.9, 5362.1, 4647.5, 5201.0, 5167.6, 4833.6, 5280.4, 5278.4, 6304.4, 6995.1], dtype=float)],
        }
        
        total_income_data = {
            '전체소득': [np.array([424.2, 433.0, 455.1, 543.1, 548.8, 531.9, 547.6, 592.9, 652.9, 681.4, 717.0, 747.7, 832.5, 811.1, 868.5], dtype=float),
                        np.array([1031.1, 1022.9, 1096.8, 1206.5, 1247.0, 1198.1, 1263.5, 1337.8, 1430.3, 1508.9, 1577.1, 1666.7, 1876.2, 1780.4, 1877.6], dtype=float),
                        np.array([1576.7, 1589.2, 1693.9, 1822.9, 1910.7, 1905.4, 2013.4, 2078.3, 2222.2, 2300.1, 2399.1, 2555.9, 2720.8, 2719.6, 2841.3], dtype=float),
                        np.array([2262.7, 2296.4, 2411.5, 2603.4, 2673.6, 2763.9, 2893.7, 2994.2, 3185.5, 3317.4, 3420.4, 3642.7, 3677.8, 3755.4, 3952.5], dtype=float),
                        np.array([4173.8, 4179.1, 4315.5, 4750.1, 4889.3, 5150.6, 5228.7, 5418.6, 5795.8, 6214.6, 6102.4, 6549.0, 6311.6, 6485.3, 6959.8], dtype=float)],
        }
        
        income_data = {
            '근로소득': [np.array([301.1, 306.0, 316.5, 375.8, 384.5, 373.0, 392.7, 419.5, 458.6, 469.0, 496.6, 515.8, 574.2, 562.8, 611.6], dtype=float),
                        np.array([710.7, 689.3, 751.0, 841.7, 879.3, 839.8, 886.0, 938.4, 1008.0, 1056.8, 1110.1, 1171.1, 1334.6, 1270.5, 1361.8], dtype=float),
                        np.array([1023.5, 1014.5, 1075.4, 1177.1, 1250.1, 1240.7, 1323.5, 1351.9, 1465.8, 1518.0, 1581.3, 1687.1, 1814.4, 1776.8, 1854.1], dtype=float),
                        np.array([1387.7, 1393.3, 1459.1, 1580.2, 1646.8, 1721.1, 1811.2, 1856.6, 1971.8, 2047.1, 2126.1, 2260.2, 2286.4, 2304.4, 2395.3], dtype=float),
                        np.array([2397.5, 2367.7, 2437.1, 2723.8, 2781.4, 2902.0, 2925.4, 3031.0, 3258.0, 3495.1, 3457.4, 3665.1, 3456.6, 3511.2, 3781.3], dtype=float)]
        }
        consume_data = {
            '소비': [np.array([518,  694.9, 758.5, 760.6, 719.3, 768.8, 739.3, 772.3, 783.9, 830.8, 857.5, 894.1, 933.2, 859.6, 964.3], dtype=float),
                    np.array([ 824.6, 925.9 ,991.4, 1064.7, 1055.3, 1056.1, 1053.5, 1116.5, 1134.2, 1161.6, 1214.4, 1322.7, 1294.7, 1218.6, 1295.2], dtype=float),
                    np.array([1010.2, 1287.5,1333.1, 1385.3, 1347.6, 1380.2, 1436.8, 1432.3, 1465.7, 1479.8, 1559.2, 1571.2, 1650.9, 1552.2, 1616.4], dtype=float),
                    np.array([1223.8, 1501.9 ,1553.7, 1646.3, 1652.1, 1700.7, 1722.9, 1771.9, 1771.8, 1828.7, 1907.6, 1896.4, 1933.0, 1814.2, 1884.3], dtype=float),
                    np.array([1604.4, 1962.0, 1955.0, 2173.0, 2035.1, 2180.1, 2288.6, 2242.9, 2342.9, 2377.4, 2405.6, 2485.3, 2478.5, 2348.6, 2384.9], dtype=float)],
        }
    
        # 2021년 데이터 추출
        year_2021index = years.index('2021')
        net_worth_2021 = [arr[year_2021index] for arr in net_worth_data['순자산']]
        debt_2021 = [arr[year_2021index] for arr in debt_data['부채']]
        total_income_2021 = [arr[year_2021index] for arr in total_income_data['전체소득']]
        income_2021 = [arr[year_2021index] for arr in income_data['근로소득']]
        consume_2021 = [arr[year_2021index] for arr in consume_data['소비']]
        
        # 비율 계산
        net_worth_ratio = [round((net_worth_input / value)*100-100, 4) for value in net_worth_2021]
        debt_ratio = [round((debt_input / value)*100-100, 4) for value in debt_2021]
        total_income_ratio = [round((total_income_data_input / value)*100-100, 4) for value in total_income_2021]
        income_ratio = [round((labor_income_input / value)*100-100, 4) for value in income_2021]
        consume_ratio = [round((consume_input / value)*100-100, 4) for value in consume_2021]
        
        # 결과 출력
        
        
        # 그래프 그리기
        for i in range(5):
            fig, ax = plt.subplots(figsize=(10, 6))
        
            ax.plot(years, net_worth_data['순자산'][i], label='순자산', color='red')
            ax.plot(years, debt_data['부채'][i], label='부채', color='blue')
            ax.plot(years, total_income_data['전체소득'][i], label='전체소득', color='orange')
            ax.plot(years, income_data['근로소득'][i], label='근로소득', color='green')
            ax.plot(years, consume_data['소비'][i], label='소비', color='purple')
        
            ax.scatter(years[-1], net_worth_input, color='red', label='사용자 순자산', zorder=5)
            ax.scatter(years[-1], debt_input, color='blue', label='사용자 부채', zorder=5)
            ax.scatter(years[-1], total_income_data_input, color='orange', label='사용자 전체소득', zorder=5)
            ax.scatter(years[-1], labor_income_input, color='green', label='사용자 근로소득', zorder=5)
            ax.scatter(years[-1], consume_input, color='purple', label='사용자 소비', zorder=5)
        
            ax.set_title(f'소득 {i+1}분위별 순자산, 부채, 소득, 소비 현황', fontproperties=font_prop)
            ax.set_xlabel('시간', fontproperties=font_prop)
            ax.set_ylabel('금액', fontproperties=font_prop)
            ax.legend(prop=font_prop)
            ax.grid(True)
            st.pyplot(fig)
            
            st.write(f"소득 {i+1}분위")
            st.write("입력한 값과 순자산의 차이 비율 :\t\t", f"{net_worth_ratio[i]}%")
            st.write("입력한 값과 부채의 차이 비율 :\t\t", f"{debt_ratio[i]}%")
            st.write("입력한 값과 전체 소득의 차이 비율 :\t", f"{total_income_ratio[i]}%")
            st.write("입력한 값과 근로 소득의 차이 비율 :\t", f"{income_ratio[i]}%")
            st.write("입력한 값과 소비의 차이 비율 :\t", f"{consume_ratio[i]}%")
            st.write("-" * 50)
