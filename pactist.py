import threading
import time

 def time():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logging in for",count"seconds")

x = threading.Thread(target=timer, daemon=True)
x.start()

answer = input("do yiu want to exit")