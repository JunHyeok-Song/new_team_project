import metro_final_final_final
from haversine import haversine
"""
test data
a53,금정구,니즈호텔,부산광역시 금정구 청룡동 12175,               35.2744981,129.0899731
a54,기장군,바다애펜션,부산광역시 기장군 기장읍 시랑리 540-5,       35.18604169,129.2133248
"""
class ExtractAndCalculate:
    def __init__(self):
        # 노선 최적결과 계산 객체 생성
        self.obj = metro_final_final_final.MainClass()
        distance_optimization_object = metro_final_final_final.MainClass()
        self.metro_location_data_list = self.obj.getTotalLocation()
        self.metro_name_data_list = self.obj.getTotalName()
        self.metro_term_data = self.obj.getGraph()
        self.calculate_result_about_distance = list()
        self.short_distance_station_data = None
        self.want_station_name_data = None
        self.want_station_location_data = None
        self.accumulate_time_data = None
        self.line_number_list = None
        self.transfer_station_name_list = None

    def run(self):
        input_data = self.getTwoLocationDataTest()
        calculate_result = self.distanceCompare(input_data[0], input_data[1], self.metro_location_data_list)
        self.short_distance_station_data = calculate_result  # 가까운 역 데이터
        fix_result = self.fixStationName(calculate_result)

        # set
        self.obj.setInformation(fix_result[0], fix_result[1])
        # get
        self.obj.programRun()
        # run
        want_data = self.obj.getInformation()
        self.want_station_name_data = want_data[0]
        self.want_station_location_data = want_data[1]

        self.accumulate_time_data = self.timeCalculate()
        self.line_number_list = self.checkLineNumber()
        self.transfer_station_name_list = self.checkTransferStation()

    def fixStationName(self, calculate_result):
        fix_station1 = None
        fix_station2 = None
        temp_station1 = calculate_result[0][0]
        temp_station2 = calculate_result[1][0]
        for station_name in self.metro_name_data_list:
            if temp_station1 in station_name:
                fix_station1 = station_name
        for station_name in self.metro_name_data_list:
            if temp_station2 in station_name:
                fix_station2 = station_name
        return [fix_station1, fix_station2]

    def distanceCompare(self, user_input_data1, user_input_data2, metro_data_list_):
        temp_list = list()
        calculate_result_about_distance = list()
        for metro_data in metro_data_list_:
            metro_location_data = (float(metro_data[1]), float(metro_data[2]))
            calculate_result = haversine(user_input_data1, metro_location_data, unit='km')
            temp_list.append([metro_data[0], calculate_result, float(metro_data[1]), float(metro_data[2])])
        temp_list.sort(key=lambda x: x[1])
        calculate_result_about_distance.append(temp_list[0])

        temp_list.clear()

        for metro_data in metro_data_list_:
            metro_location_data = (float(metro_data[1]), float(metro_data[2]))
            calculate_result = haversine(user_input_data2, metro_location_data, unit='km')
            temp_list.append([metro_data[0], calculate_result, float(metro_data[1]), float(metro_data[2])])
        temp_list.sort(key=lambda x: x[1])
        calculate_result_about_distance.append(temp_list[0])

        return calculate_result_about_distance

    def timeCalculate(self):
        accumulate_time_list = list()
        for i in range(len(self.want_station_name_data) - 1):
            for row in self.metro_term_data:
                if ((self.want_station_name_data[i] in row[0]) and (self.want_station_name_data[i+1] in row[1])) or \
                        ((self.want_station_name_data[i] in row[1]) and (self.want_station_name_data[i+1] in row[0])):
                    accumulate_time_list.append(row[2])
        accumulate_time_data = sum(accumulate_time_list)
        return accumulate_time_data

    def checkLineNumber(self):
        temp_list = list()
        for name in self.want_station_name_data:
            temp_list.append(name[-2])
        neat_list = list(dict.fromkeys(temp_list))
        return neat_list

    def checkTransferStation(self):
        temp_list = list()
        temp_name_list = list()
        for name in self.want_station_name_data:
            temp_list.append(name[-2])
        for i in range(len(temp_list)-1):
            if temp_list[i] != temp_list[i+1]:
                temp_name_list.append(self.want_station_name_data[i][:-3])
        return temp_name_list

    def getTwoLocationDataTest(self):
        user_input_location_data1_latitude = float(input("입력 : "))
        user_input_location_data1_longitude = float(input("입력 : "))
        user_input_location_data2_latitude = float(input("입력 : "))
        user_input_location_data2_longitude = float(input("입력 : "))
        result_list = [[user_input_location_data1_latitude, user_input_location_data1_longitude], [user_input_location_data2_latitude, user_input_location_data2_longitude]]
        return result_list

    def getTwoLocationData(self, loc1, loc2):
        self.user_input_location_data1 = loc1  # input("입력 : ")
        self.user_input_location_data2 = loc2  # input("입력 : ")

    def getShortDistanceStationData(self):
        return self.want_station_name_data

    def getWantStationLacationData(self):
        return self.want_station_location_data

    def getWantStationNameData(self):
        return self.short_distance_station_data

    def getAccumulateTimeResult(self):
        return self.accumulate_time_data

    def getPassedLineNumberList(self):
        return self.line_number_list

    def getTransferStationNameList(self):
        return self.transfer_station_name_list

if __name__ == "__main__":
    obj = ExtractAndCalculate()
    obj.run()
    print("경로 명")
    print(obj.getShortDistanceStationData())
    print("경로 위치")
    print(obj.getWantStationLacationData())
    print("가까운 역(출발역, 도착역)")
    print(obj.getWantStationNameData())
    print("시간 확인")
    print(obj.getAccumulateTimeResult())
    print("호선 확인(순서O)")
    print(obj.getPassedLineNumberList())
    print("환승역 확인")
    print(obj.getTransferStationNameList())


"""
GUI로 돌아가는 형태여서 클래스로 만든  파트가 동작이 종료되고, 삭제되면서 그 아래 함수를 수행해도 데이터가 없는 것.
"""