import EC_Points_Multiply as ECPtsMult


def KeyGen(key, pointSet):
    order = len(pointSet)
    if key > order:
        key = key % order

        if key == 0: return pointSet[str(order) + "P"]  # if the modulo is zero return the last element in list

        key = pointSet[str(key) + "P"]  # User Public Key
    else:
        key = pointSet[str(key) + "P"]  # User Public Key

    return key


print("ECDH Key Exchnage Protocol")
print("Elliptic Curve: y^2 = x^3 + a*x + b (mod p)")
a = int(input("Enter the coefficient a: ").strip())
b = int(input("Enter the coefficient b: ").strip())
p = int(input("Enter the p mod value: ").strip())

print("Elliptic Curve: y^2 = x^3 + " + str(a) + "*x + " + str(b) + " (mod" + str(p) + ")")

gx = int(input("Enter generator x value: ").strip())
gy = int(input("Enter generator y value: ").strip())

generator = (gx, gy)

Xa = int(input("User A enter private keyA: ").strip())  # User A Private Key
Xb = int(input("User B enter private keyB: ").strip())  # User B Private Key

publicKeyA = KeyGen(Xa, ECPtsMult.scale_point_set(a, b, p, generator))
print("User A public KeyA Ya:", publicKeyA)

publicKeyB = KeyGen(Xb, ECPtsMult.scale_point_set(a, b, p, generator))
print("User B public KeyB Yb:", publicKeyB, end="\n\n")

kP_set_sharedKeyA = KeyGen(Xa, ECPtsMult.scale_point_set(a, b, p, publicKeyB))
print("User A shared key", kP_set_sharedKeyA)

kP_set_sharedKeyB = KeyGen(Xb, ECPtsMult.scale_point_set(a, b, p, publicKeyA))
print("User B shared key", kP_set_sharedKeyB, end="\n\n")

if kP_set_sharedKeyA == kP_set_sharedKeyB:
    print("Success!!! UserA and UserB have the same key")
