import socket
import colorama
import sys
import threading
colorama.init()

terminate = threading.Event()

class conn:
    def __init__(self,host) :
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ADDR = host
        self.PORT = 444
        

    # def send(self,file):
    #     print(f"Sending {file} to receiver")
    #     fil = open(file,"rb")
    #     chunk = fil.read(1024)
    #     try:
    #         while chunk:
    #             self.sock.send(chunk)
    #             chunk = fil.read(1024)
    #         print(termcolor.colored("File successfully sent","green"))
    #     except socket.error as e:
    #         print(termcolor.colored("Failed to send file ","red"))
    #         print(e)


    def recv(self,file):
        f = open(file,"wb")
        try:
            while not terminate.is_set():
                chunk = self.sock.recv(1024)
                if not chunk:
                    break
                f.write(chunk)
            print(f"{colorama.Fore.GREEN}Receive complete {colorama.Style.RESET_ALL}")
            f.close()
        except socket.error:
            print(f"{colorama.Fore.RED}Receive Failed{colorama.Style.RESET_ALL}")
    

    def main(self,file=None):
        # rec = threading.Thread(self.sock=self.recv)
        # rec.start()
        self.recv(file)

try:
    hst = input("Enter the ip address of the host ")
    file_transfer = conn(hst)
    file_transfer.sock.connect((file_transfer.ADDR,file_transfer.PORT))
    print(f"{colorama.Fore.GREEN}connected to host{colorama.Style.RESET_ALL}")
    try:
        sys.argv[1]
        file_transfer.main(sys.argv[1])
    except IndexError:
        print("Input a file")
except socket.error as e:
    print(f"{colorama.Fore.RED}An unexpected error occured{colorama.Style.RESET_ALL}")
    print(f"{type(e).__name__},{e}")
finally:
     file_transfer.sock.close()
