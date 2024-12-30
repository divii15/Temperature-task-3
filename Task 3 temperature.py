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

