
#ONE  - WAY
# seven_days = []


# for i in range(1, 8):
#     temp = int(input(f"Ingrese la temperatura del día {i}: "))
#     seven_days.append(temp)

# seven_days.sort()


# print(f"La temperatura máxima es {max(seven_days)}°C")

# print(f"La temperatura mínima es {min(seven_days)}°C")

# print(f"La temperatura promedio es {sum(seven_days) / len(seven_days)}°C")

#SECOND  - WAY
seven_days = []


for i in range(1, 8):
    temp = int(input(f"Ingrese la temperatura del día {i}: "))
    seven_days.append(temp)

seven_days.sort()

max_temp = 0
min_temp = 100


for j in seven_days:
    if j > max_temp:
        max_temp = j
    if j < min_temp:
        min_temp = j   

print(f"La temperatura máxima es {max_temp}°C")
print(f"La temperatura mínima es {min_temp}°C")
print(f"La temperatura promedio es {sum(seven_days) / len(seven_days)}°C")
