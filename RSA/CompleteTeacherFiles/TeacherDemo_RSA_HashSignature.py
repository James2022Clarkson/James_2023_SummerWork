from Teacher_RSAClass_HashSignatureFunctions import *


# This File is a demonstration of RSA Encryption in practice, for the logic behind the decisions made, see
# ### POWERPOINT ####


if __name__ == "__main__":
    # assigning two keys to two users, so they can communicate both ways.
    if 1 == 1:  # disable to use random primes(random primes occasionally generate numbers small enough to trip error protection code)
        p = 6590931022536165685431242563274435929755514340432152012489163885084375099810784640703665344188416779504170626555278438541106140219
        q = 5852861251882460148610485097553792365770268149930588402747925106057304945295566283313067044848790434855431308587244988999412858607
        r = 4171870264810250979476660047579817246040723809999034234737866919847666269980254724961466287977894940471399296882488171958471731469
        s = 12082024508935335613176023863034702501411331831980658583076442323545258876848399486196085141563671091559410501265390525234830668419
    else:
        p, q, r, s = 0, 0, 0, 0
    key_pair1 = KeyGeneration(p, q)
    key_pair2 = KeyGeneration(r, s)

    Alice_private_key = key_pair1.getPrivateKey()
    Alices_public_key = key_pair1.getPublicKey()

    Bob_private_key = key_pair2.getPrivateKey()
    Bobs_public_key = key_pair2.getPublicKey()

    print(f"\nThe first private key holder sees Private key = {Alice_private_key}")
    print(f"the Public can see: {Alices_public_key}\n")
    print(f"The second private key holder sees their Private key: {Bob_private_key}")
    print(f"the Public can see: {Bobs_public_key}\n")

    # now, let's send this message.
    message = "A secret is no fun if everyone knows it."
    # the first thing to do is to pad it, to keep regularities in messages from becoming weaknesses.
    # this part isn't focused on, but it is a common practice for most encryption techniques
    padded_message = SimplePadding(message)
    print("Our padded message: ", padded_message)

    # then, we need to turn our string into an integer, which we can work with.
    # the RSA_Encrypt function can do this for us, but we can also do it ourselves.
    message_as_an_int = TextToInt(padded_message)
    print("Our message as an integer", message_as_an_int)
    # now, let's have Alice send make this into a ciphered value she can send to Bob, using Bob's public key
    ciphered_message = RSA_Encrypt(message_as_an_int, Bobs_public_key)

    # this message is then sent, secure in the fact that interception won't be an issue.
    print("ciphered message:", ciphered_message)
    #

    # then, on the other end, Bob uses his private key to decipher the message, a key only he has access to.
    deciphered_message_int = RSA_Decrypt_Integer(ciphered_message, Bob_private_key)

    # he then receives the int form of the message, before turning it back into a string
    print("message received:", deciphered_message_int)

    # then, we turn that integer back into a string.
    secret_string = IntToText(deciphered_message_int)

    print("On the Other end, we end up with:", secret_string)
    print("if we inverse the padding process, it's clear we have the same message we sent\n")

    ###
    # now, for a demonstration of Hashing as a Digital Signature.
    ###

    # the sender('signee'), Alice, will generate a hashing value of their message first.
    message = "I'm Alice, and I can prove it!"
    h = Hashing(message)
    # you can think of h as a scrambled version of the message where we can't actually go from h to the original message
    # it's a one way process.

    # h is our hashed value. It has several useful properties which make it difficult to forge or decipher
    # we don't need to worry about how, only know it works.

    # if you remember, e and d are inverses, and which one is the public and which is the private are only conveniences
    # this means we can encrypt with e, and then only d can decrypt, the inverse of the normal method
    message_Signature = RSA_Encrypt(h, Alice_private_key)
    print("The message is:", message)
    print("This particular message's signature from Alice is", message_Signature)

    # as an example, let's examine Bob's signature on the exact same message
    print("Bob's signature on the exact same message would be :", RSA_Encrypt(h, Bob_private_key))

    print("\n")  # to space out the output for readability

    # each message has a new, unpredictable signature, based on the sender's private key
    # so using that signature, the reader will know the sender is in possession of Alice's key, only Alice has her key.

    # then, we'd send our message like normal, only we're also sending something else,
    # our hash value signature, which has been made by Alice's private key, is then encrypted again using a second key

    ciphered_message = RSA_Encrypt(message, Bobs_public_key)  # Alice is sending to Bob
    ciphered_message_signature = RSA_Encrypt(message_Signature, Bobs_public_key)

    # We'd then send that composite message over to Bob, uncaring if it's intercepted

    # Bob then follows standard procedure to decipher the messages
    deciphered_message = RSA_Decrypt(ciphered_message, Bob_private_key)
    partly_deciphered_message_signature = RSA_Decrypt_Integer(ciphered_message_signature, Bob_private_key)

    # we can print the deciphered message immediately, but the signature is still one step away.
    print("Bob's Deciphered Message reads: ", deciphered_message)
    print("Bob Received this Deciphered Signature: ", partly_deciphered_message_signature)
    # Alice's Signature can be checked using a simple fact, it's an encrypted form of a Hash, having used Alice's private key
    # At some point, Alice and Bob would have agreed to use a particular hash(which was also a  CHF), and even if someone knows this,
    # they don't know Bob's Private Key, which he used to decipher the ciphered text into Alice's Private Key encrypted Hash Signature.
    # They'd still be stuck at decrypting the message into Alice's encrypted Hash Signature, and wouldn't be able to see the signature at all.

    # We can confirm Alice's key was used by 'finishing' the decryption of the Signature, and comparing it to the result we get normally
    # ('normally' as in hashing the message that was signed using the agreed upon hash table)

    comparable_message_signature = RSA_Decrypt_Integer(partly_deciphered_message_signature, Alices_public_key)
    # the first method is to undo the encryption of Alice's key pair, using 'e'(the public key) in this case
    normal_hash = Hashing(deciphered_message)
    # the second is to hash the message ourselves, to see what we'd have gotten normally

    print("\nWhat hashes do we get from those two methods?")
    print("the one we received   :", comparable_message_signature)
    print("the one we calculated :", normal_hash)

    if comparable_message_signature == normal_hash:
        print("As you can see, they're the same, and since we used the 'e' of alice's pair to decrypt,\n"
              "we know she must have used her private 'd' to encrypt, since the pair invert each other")
