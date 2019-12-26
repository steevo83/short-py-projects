def sum_timestamps(times):
    seconds = 0
    minutes = 0
    hours = 0
    time_list = [t.split(":") for t in times]
    for s in time_list:
        seconds += int(s[-1])
    for m in time_list:
        minutes += int(m[-2])
    for h in time_list:
        try: 
            if h[-3]:
                hours += int(h[-3])
        except IndexError:
            continue
    sec_adj = divmod(seconds, 60)
    seconds = sec_adj[1]
    minutes += sec_adj[0]
    min_adj = divmod(minutes, 60)
    minutes = min_adj[1]
    hours += min_adj[0]
    secondstr = f'{seconds:02d}'
    if hours:
        minutestr = f'{minutes:02d}:'
    else:
        minutestr = f'{minutes}:'
    hourstr = f'{hours}:'
    return f'{hourstr if hours else ""}{minutestr}{secondstr}'
    #print(time_list)
    #print(f'{hourstr if hours else ""}{minutestr}{seconds}')