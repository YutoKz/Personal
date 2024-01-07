import paho.mqtt.client as mqtt
import pymysql
import json 

# MQTT設定
MQTT_BROKER = "localhost"
MQTT_TOPIC = "sensor_data"

# MariaDB設定
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "k2002y1417"
DB_NAME = "envdata"

def on_message(
        client: mqtt.Client, 
        userdata, # type: ignore
        msg: mqtt.MQTTMessage
    ):
    data = json.loads(msg.payload)
    temperature = data.get("temperature")
    co2_level = data.get("co2_level")

    # MariaDBにデータを格納
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO sensor_data (temperature, co2_level) VALUES (%s, %s)", (temperature, co2_level))
            #cursor.execute("INSERT INTO temp_only (temperature) VALUES (%s)", (temperature))
        conn.commit()
        conn.close()
        print("Data inserted into MariaDB.")
    except pymysql.Error as e:
        print(f"Error inserting data into MariaDB: {e}")

def main():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(MQTT_BROKER, 1883, 60)
    client.subscribe(MQTT_TOPIC)
    client.loop_forever()

if __name__ == "__main__":
    main()
