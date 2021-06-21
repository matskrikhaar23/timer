import time

start = time.time()

for i in range(10):
    print i 

time.sleep(1)

end = time.time()

print(f"runtime of program is {end - start}")