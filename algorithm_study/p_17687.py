def number_convert(number, convert_number):
    res = []
    
    while number // convert_number != 0:
        res_n = number % convert_number
        res.append(res_s[res_n])
        number //= convert_number
    
    res.append(res_s[number])
    
    return res[::-1]

def solution(n, t, m, p):
    global res_s
    res_s = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    
    for i in range(0, 10):
        res_s [i] = str(i)
    
    res = []
    target = 0
    
    while len(res) < t * m:
        res += number_convert(target, n)
        target += 1
    

    turn = 1
    answer = ''
    for i in range(len(res)):
        if i % m == p - 1:
            answer += res[i]
        if len(answer) == t:
            break
            
    return answer