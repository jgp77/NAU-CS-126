def timesincemidnight(str):
    ans=(int(str[0])*60*60)+(int(str[2:4])*60)+int(str[5:7])
    return ans
