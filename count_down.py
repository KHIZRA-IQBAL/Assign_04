import time

# Ask for total time in seconds
total_seconds = int(input("⏱️ Enter countdown time in seconds: "))

while total_seconds:
    mins, secs = divmod(total_seconds, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(f"\r⏳ {timer}", end="")
    time.sleep(1)
    total_seconds -= 1

print("\n⏰ Time's up!")

