import time

print("=== Typing Speed Test ===")
print("Ye sentence type karo:")

sentence = "Aadarsh is learning Python"
print(sentence)
print("")

input("Start karne ke liye Enter dabao...")
start = time.time()

typed = input("Ab type karo: ")
end = time.time()

time_taken = end - start
words = len(typed.split())
speed = (words / time_taken) * 60

print("")
print(f"Tumne {words} words likhe")
print(f"Time laga: {round(time_taken, 2)} second")
print(f"Tumhari speed: {round(speed)} WPM")

if speed > 30:
    print("Wah! Data Entry ke liye perfect speed hai")
else:
    print("Practice karo, speed badh jayegi")
