def sheeps(day1, day2, count):
    all_days = day1 + day2
    summ = 0
    for i in range(len(all_days)):
        summ += all_days[i]
    return count - summ

print(sheeps([0], [4, 15], 31))


  

