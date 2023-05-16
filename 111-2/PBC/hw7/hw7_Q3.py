# Hw6 for PBC
# Created on 20230422 by Tsai,C,Y
# Q3----------------------------------------------------------
# read input
time_num = input()

zh_year = ['零','一','二','三','四','五','六','七','八','九','十']
zh_month = ['一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月','十二月']
zh_h = ['零','一','兩','三','四','五','六','七','八','九','十','十一','十二']

def num2z_h (hour):
    '''
    recieve a int for hour
    '''
    hour = int(hour)
    # HH
    if hour >= 12:
        if hour - 12 == 0:
            h = str('下午十二點')
        else:
            h = str('下午'+ zh_h[hour-12]+ '點')
    else:
        h = str('上午'+ zh_h[hour]+ '點')
    
    return h

def num2z_m (minutes):
    '''
    recieve a int for minute
    '''
    # MM
    m_ten = int(str(minutes[0]))
    m_one = int(str(minutes[1]))
    mm = int(minutes)
    
    if mm == 0:
        m_out = '零'
    elif 0 < mm and mm < 10 and mm != 2:
        m_out = zh_year[mm]
    elif mm == 2:
        m_out = '兩'
    else:
        if m_ten >= 2:
            m = str(zh_year[m_ten]+ '十')
        elif m_ten == 1:
            m = '十'
        else:
            m = ''

        if m_one > 0:
            m_0 = str(zh_year[m_one])
        else:
            m_0 = ''
        
        m_out = m + m_0
    
    return m_out+'分'

def num2z_s (second):
    '''
    recieve a int for minute
    '''
    # MM
    m_ten = int(str(second[0]))
    m_one = int(str(second[1]))
    mm = int(second)
    
    if mm == 0:
        m_out = '零'
    elif 0 < mm and mm < 10 and mm != 2:
        m_out = zh_year[mm]
    elif mm == 2:
        m_out = '兩'
    else:
        if m_ten >= 2:
            m = str(zh_year[m_ten]+ '十')
        elif m_ten == 1:
            m = '十'
        else:
            m = ''

        if m_one > 0:
            m_0 = str(zh_year[m_one])
        else:
            m_0 = ''
        
        m_out = m + m_0
    
    return m_out+'秒'

def num2z_date(date):

    year = date[0:4]
    mon = date[5:7]
    day = date[8:10]

    # YYYY
    
    y1 = zh_year[int(year[0])]
    y2 = (zh_year[int(year[1])])
    y3 = (zh_year[int(year[2])])
    y4 = (zh_year[int(year[3])])

    y = '西元'+y1+y2+y3+y4+'年'

    # DD
    m_ten = int(str(day[0]))
    m_one = int(str(day[1]))
    mm = int(day)
    
    if mm == 0:
        m_out = '零'
    elif 0 < mm and mm < 10:
        m_out = zh_year[mm]
    else:
        if m_ten >= 2:
            m = str(zh_year[m_ten]+ '十')
        elif m_ten == 1:
            m = '十'
        else:
            m = ''

        if m_one > 0:
            m_0 = str(zh_year[m_one])
        else:
            m_0 = ''
        
        m_out = m + m_0
    
    d = m_out+'日'

    # MM
    m = zh_month[int(mon)-1]

    # YMD
    ymd = y+m+d

    return ymd

if len(time_num) == 3:
    # HH
    hour = int(time_num[1:])
    h = num2z_h(hour)
    print(h)

elif len(time_num) == 6:
    # HH
    hour = int(time_num[1:3])
    h = num2z_h(hour)
    # MM
    min = time_num[4:6]
    m = num2z_m(min)
    print(h+m)

elif len(time_num) == 9:
    # HH
    hour = int(time_num[1:3])
    h = num2z_h(hour)
    # MM
    min = time_num[4:6]
    m = num2z_m(min)
    # SS
    sec = time_num[7:9]
    s = num2z_s(sec)
    print(h+m+s)

elif len(time_num) == 10:
    ymd = num2z_date(time_num)
    print(ymd)

elif len(time_num) == 13:
    ymd = num2z_date(time_num[:10])
    h = num2z_h(time_num[11:13])
    print(ymd+h)

elif len(time_num) == 16:
    ymd = num2z_date(time_num[:10])
    h = num2z_h(time_num[11:13])
    m = num2z_m(time_num[14:16])
    print(ymd+h+m)

elif len(time_num) == 19:
    ymd = num2z_date(time_num[:10])
    h = num2z_h(time_num[11:13])
    m = num2z_m(time_num[14:16])
    s = num2z_s(time_num[17:19])
    print(ymd+h+m+s)