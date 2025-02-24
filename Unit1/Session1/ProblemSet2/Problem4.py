def sleep_assesment(hours):
    if hours < 8:
        print("Oof, go back to bed!")
    elif hours >= 8 and hours < 10:
        print("ou got a good night's rest!")
    elif hours >= 10:
        print("You are a sleep prodidgy!")

hour_input = input("Hi, enter how many hours you slept last night: ")
hours =int(hour_input)
sleep_assesment(hours)
    