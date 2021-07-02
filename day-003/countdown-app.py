print("------------------------------------------")
print("             count down app".upper())
print("------------------------------------------")

# implement tkinter to show the countdown app

print("Count down to important dates and deadlines")

new_count_down = input("Name: ")
date_count_down = input("Date: ")

include_time = input("Do you want to in include a time? yes or no").strip().lower()
if include_time.startswith("y"):
    time_count_down = input("Time: ")

if new_count_down != "" and date_count_down != "":
    print(f"Your {new_count_down}")
