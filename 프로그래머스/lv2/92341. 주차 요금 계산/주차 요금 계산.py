import math

def solution(fees, records):
    default_time = fees[0]
    default_price = fees[1]
    unit_time = fees[2]
    unit_price = fees[3]
    
    # 입차/출차 내역 저장
    history_dict = {}
    for record in records:
        timestamp = int(record[:2]) * 60 + int(record[3:5])
        number = record[6:10]
        signal = record[11:]
        
        if number not in history_dict:
            new_dict = {"IN":[], "OUT":[], "TOTAL_TIME":0 , "TOTAL_PRICE":0}
            history_dict[number] = new_dict
        
        if signal == "IN":
            history_dict[number]["IN"].append(timestamp)
        else:
            history_dict[number]["OUT"].append(timestamp)
    
    # 총 이용 시간 연산
    for number in history_dict:
        # 최종 출차 시간이 없는 경우 대입
        if len(history_dict[number]["IN"]) is not len(history_dict[number]["OUT"]):
            history_dict[number]["OUT"].append(23 * 60 + 59)
        
        for i in range(len(history_dict[number]["IN"])):
            timestamp_in = history_dict[number]["IN"][i]
            timestamp_out = history_dict[number]["OUT"][i]
            
            history_dict[number]["TOTAL_TIME"] += (timestamp_out - timestamp_in)
    
    # 금액 연산
    for number in history_dict:
        extra_time = history_dict[number]["TOTAL_TIME"] - default_time
        if extra_time <= 0:
            extra_price = 0
        else:
            extra_price = math.ceil(extra_time / unit_time) * unit_price
        
        history_dict[number]["TOTAL_PRICE"] = default_price + extra_price
            
    # list로 변환
    history_list = []
    for number in history_dict:
        history_list.append([number, history_dict[number]["TOTAL_PRICE"]])
    
    # 이름순으로 정렬
    history_list.sort(key=lambda x:x[0])

    
    return [x[1] for x in history_list]
    