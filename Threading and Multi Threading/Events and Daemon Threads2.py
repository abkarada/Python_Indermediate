import threading
import time

path = "text.txt"
text = ""

def readFile():
    global path, text
    while True:
        with open(path, "r") as f:
            text = f.read()
        time.sleep(3)

def printLoop():
    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printLoop)

t1.start()
t2.start()

t2.join()  
