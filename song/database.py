import pandas as pd
import sqlite3
pd.set_option("display.max_columns", None)

class DataBase:
    def __init__(self):
        # 데이터 불러오기

        self.common_data = pd.read_csv("./data/common_data.csv")
        self.accommodation_sub_data = pd.read_csv("./data/accommodation_sub_data.csv")
        self.restaurant_sub_data = pd.read_csv("./data/restaurant_sub_data.csv")
        self.trip_place_sub_data = pd.read_csv("./data/trip_place_sub_data.csv")

        self.conn = sqlite3.connect("main_db")
        self.cur = self.conn.cursor()
        self.conn.execute('CREATE TABLE IF NOT EXISTS common'
                          '(id varchar(255) PRIMARY KEY,'
                          'brought varchar(255), '
                          'name varchar(255), '
                          'address varchar(255),'
                          'latitude float, '
                          'longitude float, '
                          'contact_number varchar(255))')

        self.conn.execute('CREATE TABLE IF NOT EXISTS trip_place_sub'
                          '(id varchar(255), '
                          'detail text,'
                          'image_address text, '
                          'FOREIGN KEY (id) REFERENCES common (id))')

        self.conn.execute('CREATE TABLE IF NOT EXISTS restaurant_sub'
                          '(id varchar(255), '
                          'detail text,'
                          'image_address text, '
                          'FOREIGN KEY (id) REFERENCES common (id))')

        self.conn.execute('CREATE TABLE IF NOT EXISTS accommodation_sub'
                          '(id varchar(255), '
                          'detail text,'
                          'image_address text, '
                          'FOREIGN KEY (id) REFERENCES common (id))')

        self.conn.execute('CREATE TABLE IF NOT EXISTS recommend'
                          '(id varchar(255), '
                          'name text, '
                          'ten integer, '
                          'twenty integer, '
                          'thirty integer, '
                          'fourty integer, '
                          'fifty integer, '
                          'sixty integer, '
                          'FOREIGN KEY (id) REFERENCES common (id))')

        # 'gangwon integer, '
        # 'gyeonggi integer, '
        # 'geongnam integer, '
        # 'geongbuk integer, '
        # 'daegu integer, '
        # 'seoul integer, '
        # 'sejong integer, '
        # 'ulsan integer, '
        # 'incheon integer, '
        # 'jeonnam integer, '
        # 'jeonbuk integer, '
        # 'jeju integer, '
        # 'chungnam integer, '
        # 'chungbuk integer, '

        self.conn.execute('CREATE TABLE IF NOT EXISTS member'
                          '(user_id varchar(255) PRIMARY KEY,'
                          'password varchar(255), '
                          'name varchar(255), '
                          'age integer)')

        self.conn.execute('CREATE TABLE IF NOT EXISTS schedule'
                          '(user_id varchar(255), '
                          'order_number integer, '
                          'contents_id varchar(255), '
                          'contents_name varchar(255), '
                          'contents_latitude float, '
                          'contents_longitude float, '
                          'image_address text, '
                          'FOREIGN KEY (user_id) REFERENCES member (user_id), '
                          'FOREIGN KEY (contents_id) REFERENCES common (id))')

        self.conn.execute('CREATE TABLE IF NOT EXISTS metrolocation'
                          '(station_name varchar(255), '
                          'station_latitude float, '
                          'station_longitude float)')

        self.conn.execute('CREATE TABLE IF NOT EXISTS metro'
                          '(first_station varchar(255), '
                          'second_station varchar(255), '
                          'distance integer)')

        # self.conn.execute('CREATE TABLE IF NOT EXISTS metro'
        #                   '(station_id varchar(255) PRIMARY KEY, '
        #                   'line_number varchar(255), '
        #                   'station_name varchar(255), '
        #                   'station_address varchar(255), '
        #                   'station_latitude float, '
        #                   'station_longitude float, '
        #                   'between_distance float, '
        #                   'between_time float)')

        # 데이터 넣기.
        self.conn = sqlite3.connect("main_db")
        self.cur = self.conn.cursor()

        self.common_data = pd.read_csv("./data/common_data.csv")
        for index, row in self.common_data.iterrows():
            insert_data = list(row.values)
            self.cur.execute('INSERT INTO common(id, brought, name, address, latitude, longitude, contact_number) VALUES(?, ?, ?, ?, ?, ?, ?)', insert_data)

        self.accommodation_sub_data = pd.read_csv("./data/accommodation_sub_data.csv")
        for index, row in self.accommodation_sub_data.iterrows():
            insert_data = list(row.values)
            self.cur.execute(
                'INSERT INTO accommodation_sub(id, detail, image_address) VALUES(?, ?, ?)', insert_data)

        self.restaurant_sub_data = pd.read_csv("./data/restaurant_sub_data.csv")
        for index, row in self.restaurant_sub_data.iterrows():
            insert_data = list(row.values)
            self.cur.execute(
                'INSERT INTO restaurant_sub(id, detail, image_address) VALUES(?, ?, ?)', insert_data)

        self.trip_place_sub_data = pd.read_csv("./data/trip_place_sub_data.csv")
        for index, row in self.trip_place_sub_data.iterrows():
            insert_data = list(row.values)
            self.cur.execute(
                'INSERT INTO trip_place_sub(id, detail, image_address) VALUES(?, ?, ?)', insert_data)

        self.recommend_data = pd.read_csv("./data/recommend_data.csv")
        for index, row in self.recommend_data.iterrows():
            insert_data = list(row.values)
            self.cur.execute('INSERT INTO recommend(id, name, ten, twenty, thirty, fourty, fifty, sixty) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', insert_data)

        self.metro_data = pd.read_csv("./metro/subway.csv")
        for index, row in self.metro_data.iterrows():
            insert_data = list(row.values)
            self.cur.execute('INSERT INTO metro(first_station, second_station, distance) VALUES(?, ?, ?)', insert_data)

        self.metrolocation_data = pd.read_csv("./metro/subwayLocation.csv")
        for index, row in self.metrolocation_data.iterrows():
            insert_data = list(row.values)
            self.cur.execute('INSERT INTO metrolocation(station_name, station_latitude, station_longitude) VALUES(?, ?, ?)', insert_data)

        self.conn.commit()
        self.conn.close()


        """
        # 로드 테스트
        self.conn = sqlite3.connect("main_db")
        self.conn.execute('PRAGMA foreign_keys = on')
        self.cur = self.conn.cursor()
        self.total_trip_data = pd.read_sql('SELECT * from common inner join trip_place_sub on common.id == trip_place_sub.id', self.conn)
        print(self.total_trip_data)

        # 화면 출력
        # self.cur.execute('SELECT * from common inner join trip_place_sub on common.id == trip_place_sub.id')
        # rows = self.cur.fetchall()
        # for row in rows:
        #     print(row)

        # 데이터 프레임으로 main_db의 테이블 저장
        self.common_table = pd.read_sql('SELECT * from common', self.conn)
        self.trip_place_sub_table = pd.read_sql('SELECT * from trip_place_sub', self.conn)
        self.restaurant_sub_table = pd.read_sql('SELECT * from restaurant_sub', self.conn)
        self.accommodation_sub_table = pd.read_sql('SELECT * from accommodation_sub', self.conn)
        self.recommend_table = pd.read_sql('SELECT * from recommend', self.conn)
        self.member_table = pd.read_sql('SELECT * from member', self.conn)
        self.schedule_table = pd.read_sql('SELECT * from schedule', self.conn)
        self.metro_table = pd.read_sql('SELECT * from metro', self.conn)

        self.conn.close()
        """

if __name__ == "__main__":
    data_base_object = DataBase()