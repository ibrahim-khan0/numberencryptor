import random
print("Welcome to the Number Encryptor!")
encrypt_decrypt = input("Would you like to encrypt or decrypt (encrypt, decrypt): ")
if (encrypt_decrypt == "encrypt"):
    number = input("Please enter the number you wish to encrypt:")
    Ukey = random.random()
    Rkey = float(Ukey) * 100
    encrypted_num = float(number) * float(Rkey)
    print("Your encrypted number is: " + str(encrypted_num))
    print("Your key is: " + str(Rkey))
if (encrypt_decrypt == "decrypt"):
    encrypted_numdc = input("Please enter your encrypted number: ")
    encrypted_numkeydc = input("And the key: ")
    normal_num = float(encrypted_numdc) / float(encrypted_numkeydc)
    print("Your number is " + str(normal_num) + ".")
