from desFunctions.DESOperations import KeyGenOperations, Conversions

keyGenOperation = KeyGenOperations()
conversion = Conversions()

def keyGeneration(key):
    PC1 = keyGenOperation.permutationChoice1(key)

    C = PC1[ : 28]
    D = PC1[28 : ]

    roundKeys = []
    rotationSequence = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    roundCount = 0
    while roundCount < 16:
        Cs = keyGenOperation.leftCircularShift(C, rotationSequence[roundCount])
        Ds = keyGenOperation.leftCircularShift(D, rotationSequence[roundCount])

        PC2_key = keyGenOperation.permutationChoice2(Cs.join(Ds))

        roundKeys.append(PC2_key)
        
        C = Cs
        D = Ds

        roundCount += 1
    return roundKeys



