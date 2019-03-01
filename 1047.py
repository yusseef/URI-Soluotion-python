first_hour, first_minute, end_hour, end_minute = map(int, input().split())
if end_hour == first_hour == first_minute == end_minute:
    houres, minutes = 24, 0
else:
    if end_minute >= first_minute:
        minutes = end_minute - first_minute
    else:
        minutes = 60 - abs(end_minute - first_minute)
        end_hour -= 1
    if end_hour >= first_hour:
        houres = end_hour - first_hour
    else:
        houres = 24 - abs(end_hour - first_hour)
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(houres, minutes))
