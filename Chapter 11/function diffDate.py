def diffDate(x):
    # x dalam bentuk ('yyyy-mm-dd')
    import datetime
    now = datetime.datetime.now()
    tgl_now = datetime.datetime(now.year, now.month, now.day)
    x_split = x.split('-')
    y = [int(i) for i in x_split]
    tgl_input = datetime.datetime(y[0], y[1], y[2])
    if tgl_now < tgl_input:
        selisih = tgl_input - tgl_now
    elif tgl_now > tgl_input:
        selisih = tgl_now - tgl_input
    return selisih.days 
