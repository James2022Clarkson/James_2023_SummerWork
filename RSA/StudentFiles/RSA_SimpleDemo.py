from RSA_Class import *

# This File is a demonstration of RSA Encryption in practice, for the logic behind the decisions made, see
# ### ADD POWERPOINT ####


if __name__ == "__main__":
    p = 47
    q = 73
    key_pair = KeyGeneration(p, q)
    Alice_private_key = key_pair.getPrivateKey()
    Alice_public_key = key_pair.getPublicKey()

    print("The private key holder sees:", Alice_private_key)
    print("The Public can see:", Alice_public_key, "\n")

    message = 13
    print("message to be sent:", message)

    ciphered_message = RSA_Method(message, Alice_public_key)
    print("ciphered message:", ciphered_message)

    # this ciphered message is then transferred over a secure, but not necessarily private, connection

    deciphered_message_int = RSA_Method(ciphered_message, Alice_private_key)
    print("message deciphered:", deciphered_message_int)
