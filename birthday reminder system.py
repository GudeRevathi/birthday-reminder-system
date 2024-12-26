from datetime import datetime


birthdays = {
    "Alice": "19-12",
    "Bob": "15-03",
    "Charlie": "19-12"
}


today = datetime.now().strftime("%d-%m")


for name, date in birthdays.items():
    if date == today:
        print(f"🎉 Happy Birthday, {name}!")
        break
else:
    print("No birthdays today.")