def date_autumn(dates):
    autumn_dates = []
    for i in dates:
        clear_date = list(map(int, i.split('-')))
        if 9 <= clear_date[0] <= 11:
            autumn_dates.append(clear_date)
    autumn_dates = sorted(autumn_dates)
    return '-'.join(map(str, autumn_dates[-1]))


if __name__ == '__main__':
    dates = {"11-27-2006",
             "12-01-2009",
             "08-31-2010",
             "11-28-2008",
             "11-28-2009"}
    print(date_autumn(dates))
