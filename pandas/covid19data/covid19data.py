import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter,DayLocator
import pandas as pd

# CSVデータファイル
# https://www.mhlw.go.jp/stf/covid-19/open-data.html
data_pcr_positive_daily = './pandas/covid19data/pcr_positive_daily.csv'
data_pcr_tested_daily = './pandas/covid19data/pcr_tested_daily.csv'

# データファイルをpandasで読み込み
#  - 日々の陽性者数と、PCR検査実施数を連結
#  - また、陽性者数の移動平均、陽性率も計算
df_pcr_positive = pd.read_csv(data_pcr_positive_daily)
df_pcr_tested = pd.read_csv(data_pcr_tested_daily)
#print(df_pcr_positive)
#print(df_pcr_tested)
df = pd.merge(df_pcr_positive,df_pcr_tested,on='日付')
df['移動平均'] = df.iloc[:,1].rolling(7).mean()
df['陽性率'] = df.iloc[:,1] / df.iloc[:,2] * 100 # [%]
print(df)

# グラフ表示(pandasのplot())
#df_pcr_positive.plot()
#plt.show()

data_date = df.iloc[:,0].astype(np.datetime64)
#print(data_date)
data_pcr_positive = df.iloc[:,1]
#print(data_pcr_positive)
data_pcr_positive_ave = df.iloc[:,3]

# 陽性者数および移動平均をプロット
plt.bar(data_date,data_pcr_positive,label='PCR Positive')
plt.plot(data_date,data_pcr_positive_ave,label='moving_ave',color='r')
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(DayLocator(interval=14))
plt.gcf().autofmt_xdate()
plt.xlabel('Date')
plt.ylabel('PCR positive')
plt.grid(which='both')
plt.legend()
plt.show()

# 陽性率をプロット
#  - 陽性者数÷検査実施件数だと、単純にはできないみたい
plt.plot(data_date,df['陽性率'],label='Positive rate')
plt.xlabel('Date')
plt.ylabel('Positive rate[%]')
plt.ylim([0,100])
plt.grid(which='both')
plt.legend()
plt.show()
