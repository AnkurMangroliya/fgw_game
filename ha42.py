import time
initial = time.time()
k=0
while(k<45):
    print("ankur")
    time.sleep(2)
    k+=1
print("while time", time.time() - initial, "seconds")
initial2 = time.time()
for i in range(45):
    print("ankur")
print("for time", time.time() - initial2,"seconds")
localtime =time.asctime(time.localtime(time.time()))
print(localtime)
