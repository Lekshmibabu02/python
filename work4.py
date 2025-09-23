attendance = [18, 20, 19, 15, 21]

for x in attendance:
    if x >= 20:


        print("Full Attendance")
    else:
        print("Not Full")

def fullClassCount(attendance):
    a = 0
    for y in attendance:
        if y >= 20:
            a += 1
    return a

def totalattendance(attendance):
    total = 0
    for z in attendance:
        total += z
    return total

print("Full Day Count:", fullClassCount(attendance))
print("Total Attendance for all 5 days:", totalattendance(attendance))
