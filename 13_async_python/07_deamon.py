import threading
import time

def monitor_tea_temorature():
    while True:
        print(f"Monitoring tea temprature")
        time.sleep(2)

t = threading.Thread(target=monitor_tea_temorature, daemon=True)
t.start()

print("Main program done")