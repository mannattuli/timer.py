import time
y = input("enter the minutes")
mins=int(y)
x = input("enter the seconds")
sec=int(x)
if sec>59:
    print("enter a real second value pls")

while mins>-1:
    print(mins)
    print(sec)
    print("--------")
    time.sleep(1)
    sec -= 1
    if sec == -1:
        sec = 59
        mins -= 1
    

if sec == 0:
    print("ur time is up")
