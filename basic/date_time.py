import datetime

def datetime_getshortstring():
    now = datetime.datetime.now()
    return now.strftime('%Y%m%d_%H%M%S')

def datetime_getlongstring():
    now = datetime.datetime.now()
    return now.strftime('%Y/%m/%d %H:%M:%S')

def datetime_getshortdatestring():
    now = datetime.datetime.now()
    return now.strftime('%Y%m%d')

def datetime_getlongdatestring():
    now = datetime.datetime.now()
    return now.strftime('%Y/%m/%d')

def datetime_getshorttimestring():
    now = datetime.datetime.now()
    return now.strftime('%H%M%S')

def datetime_getlongtimestring():
    now = datetime.datetime.now()
    return now.strftime('%H:%M:%S')


print('現在日時(Short) : ',datetime_getshortstring())
print('現在日時(Long) : ',datetime_getlongstring())
print('日付(Short) : ',datetime_getshortdatestring())
print('日付(Long) : ',datetime_getlongdatestring())
print('時刻(Short) : ',datetime_getshorttimestring())
print('時刻(Long) : ',datetime_getlongtimestring())
