import math

def solution(fees, records):
    default_time, default_fee, standard_time, standard_fee = fees
    
    in_out_dict = {}
    record_dict = {}
    fee_dict = {}
    
    def calc_time(hour, in_hour, minute, in_minute):
        total_time = (hour - in_hour) * 60 + minute - in_minute
            
        if car in record_dict.keys():
            record_dict[car] += total_time
        else:
            record_dict[car] = total_time
            
    
    def calc_fee(car, total_time):
        if total_time <= default_time:
            fee_dict[car] = default_fee
        else:
            total_fee = default_fee + math.ceil(( total_time - default_time ) / standard_time ) * standard_fee

            fee_dict[car] = total_fee

    
    for record in records:
        time, car, in_out = record.split()
        hour, minute = map(int, time.split(':'))
        
        if in_out == 'IN':
            in_out_dict[car] = [hour, minute]
        
        else:
            in_hour, in_minute = in_out_dict[car]
            
            calc_time(hour, in_hour, minute, in_minute)
            
            del in_out_dict[car]
            
            
    if in_out_dict.keys():
        for car in in_out_dict.keys():
            in_hour, in_minute = in_out_dict[car]
            
            calc_time(23, in_hour, 59, in_minute)
            
    for car in record_dict.keys():
        calc_fee(car, record_dict[car])
    
    answer = []
    for car in sorted(fee_dict.keys()):
        answer.append(fee_dict[car])
    
    return answer