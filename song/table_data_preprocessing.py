import pandas as pd
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

# 전처리 결과를 Database에 넣는다.
class PreprocessTable:
    def __init__(self):
        # self.accommodation_data = pd.read_csv("./data/accommodation_data.csv", encoding='cp949')
        # self.accommodation_id_data = None
        # self.restaurant_data = pd.read_csv("./data/restaurant_data.csv", encoding='cp949')
        # self.restaurant_id_data = None
        # print(self.restaurant_data)
        # self.tourist_attractions_data = pd.read_csv("./data/tourist_attractions_data.csv", encoding="cp949")
        # self.tourist_attractions_id_data = None
        # print(self.tourist_attractions_data)

        # a1 ....
        # r1 ....
        # t1 ....
        # 에 해당되는 id값을 넣을 예정
        # 이미지 경로 추가

        # 숙박업 id 넣기
        # number_list = list()
        # for i in range(len(self.accommodation_data)):
        #     number_list.append(f"a{i + 1}")
        # self.accommodation_id_data = pd.DataFrame(number_list, columns=["id"])
        # self.accommodation_data = pd.concat([self.accommodation_id_data, self.accommodation_data], axis=1)
        # self.accommodation_data.to_csv("./data/accommodation_data.csv", index=False)
        #
        # 음식점 id 넣기
        # number_list = list()
        # for i in range(len(self.restaurant_data)):
        #     number_list.append(f"r{i + 1}")
        # self.restaurant_id_data = pd.DataFrame(number_list, columns=["id"])
        # self.restaurant_data = pd.concat([self.restaurant_id_data, self.restaurant_data], axis=1)
        # self.restaurant_data.to_csv("./data/restaurant_data.csv", index=False)
        # print(self.restaurant_data)
        #
        # 관광지 id 넣기
        # number_list = list()
        # for i in range(len(self.tourist_attractions_data)):
        #     number_list.append(f"t{i + 1}")
        # self.tourist_attractions_id_data = pd.DataFrame(number_list, columns=["id"])
        # self.tourist_attractions_data = pd.concat([self.tourist_attractions_id_data, self.tourist_attractions_data], axis=1)
        # self.tourist_attractions_data.to_csv("./data/tourist_attractions_data.csv", index=False)
        # print(self.tourist_attractions_data)

        # ====================================================================================================================

        # 이미지 주소 값 넣기
        # accommodation_file_location = "C:/Users/KDT02/Desktop/new_team_project_1/image/accommodation_data_image/"
        # self.accommodation_data = pd.read_csv("./data/accommodation_data.csv")
        # restaurant_file_location = "C:/Users/KDT02/Desktop/new_team_project_1/image/restaurant_data_image/"
        # self.restaurant_data = pd.read_csv("./data/restaurant_data.csv")
        # tourist_attractions_location = "C:/Users/KDT02/Desktop/new_team_project_1/image/tourist_attractions_data_image/"
        # self.tourist_attractions_data = pd.read_csv("./data/tourist_attractions_data.csv")
        #
        # # 숙박업 이미지 주소값 넣기
        # image_address_list = list()
        # for i in range(len(self.accommodation_data)):
        #     image_address_list.append(f"{accommodation_file_location}{self.accommodation_data.loc[i, '업체명']}.png")
        # self.image_address_data = pd.DataFrame(image_address_list, columns=["image_address"])
        # self.accommodation_data = pd.concat([self.accommodation_data, self.image_address_data], axis=1)
        # self.accommodation_data.to_csv("./data/accommodation_data.csv", index=False)
        #
        # # 음식점 이미지 주소값 넣기
        # image_address_list = list()
        # for i in range(len(self.restaurant_data)):
        #     image_address_list.append(f"{restaurant_file_location}{self.restaurant_data.loc[i, '콘텐츠명']}.png")
        # self.image_address_data = pd.DataFrame(image_address_list, columns=["image_address"])
        # self.restaurant_data = pd.concat([self.restaurant_data, self.image_address_data], axis=1)
        # self.restaurant_data.to_csv("./data/restaurant_data.csv", index=False)
        #
        # 음식점 이미지 주소값 넣기
        # image_address_list = list()
        # for i in range(len(self.tourist_attractions_data)):
        #     image_address_list.append(f"{tourist_attractions_location}{self.tourist_attractions_data.loc[i, '여행지']}.png")
        # self.image_address_data = pd.DataFrame(image_address_list, columns=["image_address"])
        # self.tourist_attractions_data = pd.concat([self.tourist_attractions_data, self.image_address_data], axis=1)
        # self.tourist_attractions_data.to_csv("./data/tourist_attractions_data.csv", index=False)

        # ====================================================================================================================
        # ERD에 맞춰서 컬럼 명 조정하기
        # same_columns_name_list = ['id', 'brought', 'name', 'address', 'latitude', 'longitude', 'contact_number', 'detail', 'image_address']
        #
        # self.accommodation_data = pd.read_csv("./data/accommodation_data.csv")
        # self.accommodation_data.columns = same_columns_name_list
        # self.accommodation_data.to_csv("./data/accommodation_data.csv", index=False)
        #
        # self.restaurant_data = pd.read_csv("./data/restaurant_data.csv")
        # self.restaurant_data.columns = same_columns_name_list
        # self.restaurant_data.to_csv("./data/restaurant_data.csv", index=False)
        #
        #
        # self.tourist_attractions_data = pd.read_csv("./data/tourist_attractions_data.csv")
        # self.tourist_attractions_data.columns = same_columns_name_list
        # self.tourist_attractions_data.to_csv("./data/tourist_attractions_data.csv", index=False)

        # ====================================================================================================================
        # ERD에 맞춰서 데이터프레임 분할하기.
        # self.accommodation_data = pd.read_csv("./data/accommodation_data.csv")
        # self.restaurant_data = pd.read_csv("./data/restaurant_data.csv")
        # self.tourist_attractions_data = pd.read_csv("./data/tourist_attractions_data.csv")
        #
        # common_columns_list = ['id', 'brought', 'name', 'address', 'latitude', 'longitude', 'contact_number']
        # self.accommodation_common_data = self.accommodation_data[common_columns_list]
        # self.restaurant_common_data = self.restaurant_data[common_columns_list]
        # self.tourist_attractions_data = self.tourist_attractions_data[common_columns_list]
        #
        # self.common_data = pd.concat([self.accommodation_common_data, self.restaurant_common_data, self.tourist_attractions_data], ignore_index=True)
        # self.common_data.to_csv("./data/common_data.csv", index=False)
        #
        # ====================================================================================================================
        # ERD에 맞춰서 데이터프레임 분할하기.
        # self.accommodation_data = pd.read_csv("./data/accommodation_data.csv")
        # self.restaurant_data = pd.read_csv("./data/restaurant_data.csv")
        # self.tourist_attractions_data = pd.read_csv("./data/tourist_attractions_data.csv")
        #
        # common_columns_list = ['id', 'detail', 'image_address']
        # # trip_place_sub_data
        # # restaurant_sub_data
        # # accommodation_sub_data
        # self.accommodation_sub_data = self.accommodation_data[common_columns_list]
        # self.accommodation_sub_data.to_csv("./data/accommodation_sub_data.csv", index=False)
        #
        # self.restaurant_sub_data = self.restaurant_data[common_columns_list]
        # self.restaurant_sub_data.to_csv("./data/restaurant_sub_data.csv", index=False)
        #
        # self.trip_place_sub_data = self.tourist_attractions_data[common_columns_list]
        # self.trip_place_sub_data.to_csv("./data/trip_place_sub_data.csv", index=False)


        # ====================================================================================================================
        # 이미지 주소 값 변경
        # new_address = "C:/Users/kdt111/Desktop/work/TeamProject44/park/image_/accommodation_data_image/"
        # self.accommodation_data = pd.read_csv("./data/accommodation_data.csv")
        # self.accommodation_sub_data = pd.read_csv("./data/accommodation_sub_data.csv")
        # accommodation_name_list = list(self.accommodation_data["name"].values)
        # new_image_address_list = list()
        # for name in accommodation_name_list:
        #     new_image_address_list.append(f"{new_address}{name}.png")
        #
        # temp = pd.DataFrame(new_image_address_list, columns=["image_address"])
        # self.accommodation_sub_data.drop("image_address", axis=1, inplace=True)
        # self.accommodation_sub_data = pd.concat([self.accommodation_sub_data, temp], axis=1)
        # self.accommodation_sub_data.to_csv("./data/accommodation_sub_data.csv", index=False)
        #
        #
        # self.restaurant_sub_data = pd.read_csv("./data/restaurant_sub_data.csv")
        # new_address = "C:/Users/kdt111/Desktop/work/TeamProject44/park/image_/restaurant_data_image/"
        # self.restaurant_data = pd.read_csv("./data/restaurant_data.csv")
        # self.restaurant_sub_data = pd.read_csv("./data/restaurant_sub_data.csv")
        # restaurant_name_list = list(self.restaurant_data["name"].values)
        # new_image_address_list = list()
        # for name in restaurant_name_list:
        #     new_image_address_list.append(f"{new_address}{name}.png")
        #
        # temp = pd.DataFrame(new_image_address_list, columns=["image_address"])
        # self.restaurant_sub_data.drop("image_address", axis=1, inplace=True)
        # self.restaurant_sub_data = pd.concat([self.restaurant_sub_data, temp], axis=1)
        # self.restaurant_sub_data.to_csv("./data/restaurant_sub_data.csv", index=False)
        #
        #
        # self.trip_place_sub_data = pd.read_csv("./data/trip_place_sub_data.csv")
        # new_address = "C:/Users/kdt111/Desktop/work/TeamProject44/park/image_/tourist_attraction_data_image/"
        # self.tourist_attractions_data = pd.read_csv("./data/tourist_attractions_data.csv")
        # self.trip_place_sub_data = pd.read_csv("./data/trip_place_sub_data.csv")
        # trip_place_name_list = list(self.tourist_attractions_data["name"].values)
        # new_image_address_list = list()
        # for name in trip_place_name_list:
        #     new_image_address_list.append(f"{new_address}{name}.png")
        #
        # temp = pd.DataFrame(new_image_address_list, columns=["image_address"])
        # self.trip_place_sub_data.drop("image_address", axis=1, inplace=True)
        # self.trip_place_sub_data = pd.concat([self.trip_place_sub_data, temp], axis=1)
        # self.trip_place_sub_data.to_csv("./data/trip_place_sub_data.csv", index=False)
        pass






if __name__ == '__main__':
    preprocess_table_object = PreprocessTable()