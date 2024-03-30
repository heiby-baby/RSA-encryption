def extended_euclidean_algorithm(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_euclidean_algorithm(b % a, a)
        return (gcd, y - (b // a) * x, x)

def modular_inverse(e, phi_n):
    gcd, x, y = extended_euclidean_algorithm(e, phi_n)
    if gcd != 1:
        raise Exception("Обратный элемент не существует.")
    else:
        return x % phi_n

def Eulerfunction(p, q):
    return (p - 1) * (q - 1)

def encrypt(text, e, n):
    encrypted_text = [pow(ord(char), e, n) for char in text]
    return encrypted_text

def decrypt(enc_t, d, n):
    decrypted_text = ''.join([chr(pow(char, d, n)) for char in enc_t])
    return decrypted_text



if __name__ == "__main__":
    p, q = 909_091, 99_990_001
    n = q * p
    eulerNum = Eulerfunction(p, q)
    e = 65537
    d = modular_inverse(e, eulerNum)  # Приватная экспонента
    text = "hello world"
    encrypted_text = encrypt(text, e, n)
    decrypted_text = decrypt(encrypted_text, d, n)
    print("Original text:", text)
    print("Encrypted text:", *encrypted_text, sep="")
    print("Decrypted text:", decrypted_text)
