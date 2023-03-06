BAD = "VISIT THE DOCTOR"
GOOD = "NORMAL"

sex = input()
red = float(input())
white = float(input())
platelets = float(input())
hemoglobin = float(input())
hematocrit = float(input())

red_flag = False
white_flag = 4500 <= white <= 11000
platelets_flag = 150000 <= platelets <= 400000
hemoglobin_flag = False
hematocrit_flag = False

if sex == "Male":
    red_flag = 4.3 <= red <= 5.9
    hemoglobin_flag = 13.5 <= hemoglobin <= 17.5
    hematocrit_flag = 41 <= hematocrit <= 53
else:
    red_flag = 3.5 <= red <= 5.5
    hemoglobin_flag = 12.0 <= hemoglobin <= 16.0
    hematocrit_flag = 36 <= hematocrit <= 46

curr = GOOD if red_flag else BAD
print(f"Red blood cells: {curr}")
curr = GOOD if white_flag else BAD
print(f"White blood cells: {curr}")
curr = GOOD if platelets_flag else BAD
print(f"Platelets: {curr}")
curr = GOOD if hemoglobin_flag else BAD
print(f"Hemoglobin: {curr}")
curr = GOOD if hematocrit_flag else BAD
print(f"Hematocrit: {curr}")
