"""test tb"""

import sqlite3
import pandas as pd
pd.set_option("display.max_column", None)
pd.set_option("display.max_row", None)







class DataBaseClass:
    conn = sqlite3.connect("main_db")
    conn.execute('PRAGMA foreign_keys = on')
    cur = conn.cursor()

    # common_table = pd.read_sql('SELECT * from common', conn)
    # trip_place_sub_table = pd.read_sql('SELECT * from trip_place_sub', conn)
    # accommodation_sub_table = pd.read_sql('SELECT * from accommodation_sub', conn)
    # restaurant_sub_table = pd.read_sql('SELECT * from restaurant_sub', conn)
    # recommend_table = pd.read_sql('SELECT * from recommend', conn)
    # member_table = pd.read_sql('SELECT * from member', conn)
    # schedule_table = pd.read_sql('SELECT * from schedule', conn)
    # metro_table = pd.read_sql('SELECT * from metro', conn)
    def main_db(self, switch_, a):
        if switch_ == 0:
            return self.trip_db(a)
        elif switch_ == 1:
            return self.restaurant_db(a)
        elif switch_ == 2:
            return self.accommodation_db(a)


    def trip_db(self, a):
        total_trip_data = pd.read_sql(
            'SELECT * from common inner join trip_place_sub on common.id == trip_place_sub.id', self.conn)
        print(total_trip_data.keys())

        if a == "전체":
            num_list = total_trip_data[
                ['image_address', 'name', 'address', 'brought', 'contact_number', 'latitude', 'longitude', 'id']]

        else:
            df_1_pd = total_trip_data[total_trip_data['brought'] == f"{a}"]
            df_1_pd.reset_index(inplace=True)
            num_list = df_1_pd[
                ['image_address', 'name', 'address', 'brought', 'contact_number', 'latitude', 'longitude', 'id']]
        list_column = ["이미지", "업체명", "주소", "시군구명", "전화번호", "위도", "경도", "아이디"]
        dict_value = {}
        dict_num = {}
        cnt_ = 0
        for i in num_list.values:
            for value in zip(list_column, i):
                dict_value[value[0]] = value[1]
                db_copy = dict_value.copy()
                dict_num[f"{cnt_}"] = db_copy
            cnt_ += 1
        return dict_num

    def restaurant_db(self, a):
        total_restaurant_data = pd.read_sql(
            'SELECT * from common inner join restaurant_sub on common.id == restaurant_sub.id', self.conn)
        if a == "전체":
            num_list = total_restaurant_data[
                ['image_address', 'name', 'address', 'brought', 'contact_number', 'latitude', 'longitude', 'id']]
        else:
            df_1_pd = total_restaurant_data[total_restaurant_data['brought'] == f"{a}"]
            df_1_pd.reset_index(inplace=True)
            num_list = df_1_pd[
                ['image_address', 'name', 'address', 'brought', 'contact_number', 'latitude', 'longitude', 'id']]
        list_column = ["이미지", "업체명", "주소", "시군구명", "전화번호", "위도", "경도", "아이디"]
        dict_value = {}
        dict_num = {}
        cnt_ = 0
        for i in num_list.values:
            for value in zip(list_column, i):
                dict_value[value[0]] = value[1]
                db_copy = dict_value.copy()
                dict_num[f"{cnt_}"] = db_copy
            cnt_ += 1
        return dict_num

    def accommodation_db(self, a):
        total_accommodation_data = pd.read_sql(
            'SELECT * from common inner join accommodation_sub on common.id == accommodation_sub.id', self.conn)
        if a == "전체":
            num_list = total_accommodation_data[
                ['image_address', 'name', 'address', 'brought', 'contact_number', 'latitude', 'longitude', 'id']]
        else:
            df_1_pd = total_accommodation_data[total_accommodation_data['brought'] == f"{a}"]
            df_1_pd.reset_index(inplace=True)
            num_list = df_1_pd[
                ['image_address', 'name', 'address', 'brought', 'contact_number', 'latitude', 'longitude', 'id']]
        list_column = ["이미지", "업체명", "주소", "시군구명", "전화번호", "위도", "경도", "아이디"]
        dict_value = {}
        dict_num = {}
        cnt_ = 0
        for i in num_list.values:
            for value in zip(list_column, i):
                dict_value[value[0]] = value[1]
                db_copy = dict_value.copy()
                dict_num[f"{cnt_}"] = db_copy
            cnt_ += 1
        return dict_num

if __name__ == '__main__':
    a = DataBaseClass()
    test = a.main_db(0, "전체")
    for i in range(len(test)):
        print(test[f'{i}'])

