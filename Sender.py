
import socket
import sys
import threading
import colorama
colorama.init()

terminate = threading.Event()

class conn:
    def __init__(self) :
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ADDR = "0.0.0.0"
        PORT = 444
        self.sock.bind((ADDR,PORT))
        

    def send(self,file):
        print(f"Sending {file} to receiver")
        fil = open(file,"rb")
        chunk = fil.read(1024)
        try:
            while chunk:
                target.send(chunk)
                chunk = fil.read(1024)
            print(f"{colorama.Fore.GREEN}File successfully sent{colorama.Style.RESET_ALL}")
        except socket.error as e:
            print(f"{colorama.Fore.RED}Failed to send file {colorama.Style.RESET_ALL}")
            print(e)


    # def recv(self):
    #     f = open("recv","wb")
    #     while not terminate.is_set():
    #         try:
    #             chunk = target.recv(1024)
    #             while chunk:
    #                 f.write(chunk)
    #             print(termcolor.colored("Receive complete","green"))
    #             f.close()
    #         except socket.error:
    #             print(termcolor.colored("Receive Failed","red"))
            

    def main(self,file=None):
        # rec = threading.Thread(target=self.recv)
        # rec.start()
        if file:
            self.send(file)
            terminate.set()
        else:
            pass

try:
    file_transfer = conn()
    print(f"Listening for incoming connections ")
    file_transfer.sock.listen(5)
    target,ip = file_transfer.sock.accept()
    print(f"{colorama.Fore.GREEN}connected to {ip} {colorama.Style.RESET_ALL}")
    try:
        sys.argv[1]
        file_transfer.main(sys.argv[1])
    except IndexError:
        print("Select a proper file")
except socket.error as e:
    print(f"{colorama.Fore.RED}An unexpected error occured {colorama.Style.RESET_ALL}")
    print(f"{type(e).__name__},{e}")
# finally:
#     file_transfer.sock.close()
