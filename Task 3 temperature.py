#TASK 3
#7)Get the Temparature from user.
#if tem greater than or equal to 0 and less than 10, output will be Very cold weather.
#if tem greater than or equal to 10 and less than 20, output will be cold weather.
#if tem greater than or equal to 20 and less than 30, output will be Normal Weather.
#if tem greater than or equal to 30 and less than 40, output will be Hot.
#otherwise Very hot.




term = int(input("Enter the temperature :"))
if term>=0 and term< 10:
    print("Very cold weather")
elif term>=10 and term < 20:
    print("Cold weather")
elif term>=20 and term < 30:
    print("Normal weather")
elif term>=30 and term< 40:
    print("Hot")
else:
    print("Very hot")

