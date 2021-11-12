import random
import hashlib

users = ["shb8aon98H9", "mw4e75nas", "Bwenf3245n", "nb4q32aY", "fbnhah5452sb"]
owner = "azgbhnu141sdba"



def getkey(o1, sp1):
  generated = input("Please enter the origin string: ")
  generated = hashlib.sha256(o1.encode()).hexdigest()
  generated = hashlib.sha256(sp1.encode()).hexdigest()
  print(generated)
  return generated

  #owner, input string and randomly chosen user are being useed to generate a hashed private key for the owner to sign transactions with
  #the hashing process is replicable only if origin input, owners name and the seed provider are known

def getseed():
    seed1 = random.choice(users)
    getkey(owner, seed1)

getseed()


