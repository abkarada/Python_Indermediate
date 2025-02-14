import threading

# Konsol çıktısı için bir kilit oluşturuyoruz
print_lock = threading.Lock()

def func1():
    for x in range(10):
        with print_lock:  # Kilidi al
            print("ONE")

def func2():
    for x in range(10):
        with print_lock:  # Kilidi al
            print("TWO")

t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

t1.start()
t2.start()

t1.join()
t2.join()