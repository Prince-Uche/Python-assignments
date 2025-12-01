def convert_minutes(minutes):
    return minutes // 60

minutes = int(input("Enter minutes: "))
if minutes < 60:
        print("Please input hours: ")
else: 
        print(convert_minutes(minutes), "hour(s)", minutes % 60, "minutes")


