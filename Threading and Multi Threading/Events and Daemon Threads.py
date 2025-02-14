import threading

event = threading.Event()

def myfunction():
    print("Waiting for event to trigger... \n")
    event.wait()
    print("Performing action XYZ now \n")

t1 = threading.Thread(target=myfunction)
t1.start()

x = input("Do you wanna trigger the event? (y/n) \n")

if x == 'y':
    event.set()



