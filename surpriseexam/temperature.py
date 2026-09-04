
#ONE  - WAY
# seven_days = []


# for i in range(1, 8):
#     temp = int(input(f"Ingrese la temperatura del día {i}: "))
#     seven_days.append(temp)

# print(f"La temperatura máxima es {max(seven_days)}°C")

# print(f"La temperatura mínima es {min(seven_days)}°C")

# average_temp = sum(seven_days) / len(seven_days)
# print(f"La temperatura promedio es {average_temp:.2f}°C")

#SECOND  - WAY
seven_days = []


for i in range(1, 8):
    temp = int(input(f"Ingrese la temperatura del día {i}: "))
    seven_days.append(temp)

max_temp = 0
min_temp = seven_days[0]


for j in seven_days:
    if j > max_temp:
        max_temp = j
    if j < min_temp:
        min_temp = j

print(f"La temperatura máxima es {max_temp}°C")
print(f"La temperatura mínima es {min_temp}°C")
average_temp = sum(seven_days) / len(seven_days)
print(f"La temperatura promedio es {average_temp:.2f}°C")
