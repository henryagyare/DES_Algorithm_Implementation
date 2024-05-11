from desFunctions.DESOperations import DESOperations, Conversions
from keyGeneration import keyGeneration
import time

start_time = time.time()
desOperations = DESOperations()
conversion = Conversions()


plainText = input("Enter Plain Text: ")
plainText = conversion.textTo64bit(plainText)

inputKey = input("Enter Encryption Key: ")
inputKey = conversion.textTo64bit(inputKey)

initialPerm = desOperations.initialPermutation(plainText)

Lo = initialPerm[:32]
Ro = initialPerm[32:]

roundKeys = keyGeneration(inputKey)
# print(f"roundKeys = {roundKeys}")
roundNumber = 0
L, R = Lo, Ro

while roundNumber < 16: 
    expandR = desOperations.expansion(R)
    keyXorR = conversion.xor(roundKeys[roundNumber], expandR)
    # keyXorR = int(roundKeys[roundNumber]) ^ int(expandR)
    # print(f"keyXor = {keyXorR}")
    # print(f"expandR = {expandR}")

    subRto32 = desOperations.substitution(keyXorR)
    # print(f"subRto32 = {subRto32}")

    permR = desOperations.permutation(subRto32)

    # LXorR = L ^ permR
    LXorR = conversion.xor(L, permR)
    L = R
    R = LXorR
    roundNumber += 1

# swap operation
L = R
R = LXorR

preCipherText = [0 for _ in range(64)] 
# preCipherText = []
preCipherText[:32] = L
preCipherText[32:] = R

cipherText = desOperations.invPermutation(preCipherText)


PT = conversion.binary_to_text(plainText)
CT = conversion.binary_to_text(cipherText)

print(f"plaintext = {PT}")
print(f"ciphertext = {CT}")
# print(cipherText)

end_time = time.time()

execution_time = end_time - start_time
print("Execution time = end_time - start_time")
print(f"Execution time = {end_time} - {start_time}")
print("Execution time:", execution_time, "seconds")


