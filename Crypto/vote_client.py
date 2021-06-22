# Client to implement simplified 'secure' electronic voting algorithm
# and send votes to a server. The client says hello to the server and indicates
# which cryptographic algorithms it can support. The server picks one
# asymmetric key and one symmetric key algorithm and then responds to the
# client with its public key and a nonce. The client generates a symmetric
# key to send to the server, encrypts the symmetric key with the public key,
# and then encrypts the nonce with the symmetric key.
# If the nonce is verified, then the server will send the "107 Polls Open"
# message.

import socket
import math
import random
import sys
import simplified_AES
import NumTheory

# Author: 
# Last modified: 2020-11-13
# Version: 0.1
#!/usr/bin/python3

class RSAClient:
    def __init__(self, address, port):
        self.address = address
        self.port = int(port)
        self.socket = socket.socket()
        self.lastRcvdMsg = None
        self.sessionKey = None		#For storing the symmetric key
        self.modulus = None		#For storing the server's n in the public key
        self.serverExponent = None	#For storing the server's e in the public key

    def send(self, message):
        self.socket.connect((self.address, self.port))
        self.socket.send(bytes(message,'utf-8'))

    def read(self):
        try:
            data = self.socket.recv(4096).decode('utf-8')
        except BlockingIOError:
            pass
        else:
            if data:
                self.lastRcvdMsg = data
            else:
                raise RuntimeError("Server is unavailable")

    def close(self):
        print("closing connection to", self.address)
        try:
            self.socket.close()
        except OSError as e:
            print(
                "error: socket.close() exception for",
                f"{self.address}: {repr(e)}",
            )
        finally:
            # Delete reference to socket object for garbage collection
            self.socket = None

    def RSAencrypt(self, msg):
        """Encryption side of RSA"""
        pass

    def computeSessionKey(self):
        """Computes this node's session key"""
        self.sessionKey = random.randint(1, 65536)

    def AESencrypt(self, plaintext):
        """Computes the simplified AES encryption of some plaintext"""
        simplified_AES.keyExp(self.sessionKey) # Generating round keys for AES.
        ciphertext = simplified_AES.encrypt(plaintext) # Running simplified AES.
        return ciphertext

    def serverHello(self):
        status = "101 Hello 3DES, AES, RSA16, DH16"
        return status

    def sessionKeyMsg(nonce):
        """Function to generate response string to server's hello"""
        pass

    def start(self):
        """Main sending and receiving loop for the client"""
        self.send(self.serverHello())
        self.read()
        print(self.lastRcvdMsg)
        self.close()
        #pass


def main():
    """Driver function for the project"""
    args = sys.argv
    if len(args) != 3:
        print ("Please supply a server address and port.")
        sys.exit()
    serverHost = str(args[1])       # The remote host
    serverPort = int(args[2])       # The same port as used by the server

    client = RSAClient(serverHost, serverPort)
    try:
        client.start()
    except (KeyboardInterrupt, SystemExit):
        exit()

if __name__ == "__main__":
    main()
