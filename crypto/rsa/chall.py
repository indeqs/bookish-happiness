from Crypto.PublicKey import RSA

flag = int.from_bytes(
    open("flag.txt", "r").read().strip().encode(), byteorder="big"
)
print(f"flag is {flag}")

key = RSA.generate(1024)
print(f"Key components: n={key.n}, e={key.e}, d={key.d}, p={key.p}, q={key.q}")

print(f"n = {key.n}")

print(f"c = {pow(flag, key.e, key.n)}")

phi = (key.p - 1) * (key.q - 1)
print(f"phi is {phi}")

print(f"strange = {pow(phi, 2, key.n)}", end="\n\n\n")
