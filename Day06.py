from functools import reduce

Time_list = [35, 69, 68, 87]
Distance_list = [213, 1168, 1086, 1248]


array_result = []

n = 0

for n in range(0, 4):
    time = int(Time_list[n])
    temp_array = []
    time_holding_button = 0
    while time_holding_button < time:
        time_holding_button = time_holding_button + 1
        Distance = (time - time_holding_button) * time_holding_button
        if Distance > Distance_list[n] and Distance != 0:
            temp_array.append(Distance)
    array_result.append(len(temp_array))
result = reduce(lambda x, y: x * y, array_result)
print(result)
