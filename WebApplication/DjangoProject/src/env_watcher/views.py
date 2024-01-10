from django.shortcuts import render

# Create your views here.

import pymysql
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Create your views here.
def index(request):

    DB_HOST = "192.168.3.6"
    DB_USER = "django"
    DB_PASSWORD = "k2002y1417"
    DB_NAME = "envdata"

    try:
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 120")
            data = cursor.fetchall()
            conn.close()

            # データを解析し、日時をdatetimeオブジェクトに変換
            timestamps = [row[1] for row in data]
            temperature_values = [row[2] for row in data]
            co2_level_values = [row[3] for row in data]

            # 折れ線グラフ
            fig, ax1 = plt.subplots(figsize=(10, 6)) # type: ignore
            ## 温度のプロット
            ax1.plot(timestamps, temperature_values, label='Temperature', marker='o', color='red')
            #ax1.set_xlabel('Time')
            ax1.set_ylabel('Temperature (°C)', color='red')
            plt.xticks(rotation=45)# type: ignore
            ax1.tick_params('y', colors='red')
            ax1.set_ylim(0, 35)
            ## CO2レベルのプロット
            ax2 = ax1.twinx()
            ax2.plot(timestamps, co2_level_values, label='CO2 Level (ppm)', marker='o', color='blue')
            ax2.set_ylabel('CO2 Level', color='blue')
            ax2.tick_params('y', colors='blue')
            ax2.set_ylim(400, 2500)
            ## グラフのフォーマット設定
            plt.xticks(rotation=45)# type: ignore
            ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
            plt.tight_layout()
            plt.savefig("/static/images/data.png")# type: ignore

    except pymysql.Error as e:
        return f"Error retrieving data from MariaDB: {e}"

    # ビューで渡すデータを作成
    context = {
            'data': data[:15],
    }

    # テンプレートをレンダリングしてレスポンスを返す
    return render(request, 'env_watcher/index.html', context)

