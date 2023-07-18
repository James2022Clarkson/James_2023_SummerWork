# those functions are created in the previous labs, and as such aren't included in the student files

def EEA(a, b, prin):
    """r = GCD, a*d + b*t = GCD(a,b) \n
    d/t are our Bezout coefficents \n
    a * d + t * b = r \n
    returns in order 'r(GCD), d, t'\n
    prin = False for no printed values, prin = True for detailed follow along"""
    ###
    # THIS FUNCTION DEMONSTRATES ONE PROCESS FOR CALCULATING MODULAR INVERSES, IT IS NOT USED IN THE CODE
    # you would restructure a modular equation of 'a*d ≡ 1 (mod b)' into 'a*d + t*b = 1', then solve using this algorythm.
    # Instead, the 'pow' function is used, following the structure pow(a, -1, mod=b), to get the modular inverse of a mod b
    ###

    # above, d is used, but the function internally uses 's' following the example of:
    # https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    # it doesn't change the formulas used, but the change is noted here.

    # variables renamed to make the recursive aspect clearer
    r0 = a
    r1 = b
    s0, s1, t0, t1 = 1, 0, 0, 1  # assigning base values for the recursion to come

    i = 0  # recursion level counter for clearer formatting when printing
    if prin:
        # Print our current status (quotient is set to "NA" since it doesn't make sense yet
        print(f"q{i} = %s r{i} = %d s{i} = %d t{i} = %d" % ("NA", r0, s0, t0))
        i += 1
        print(f"q{i} = %s r{i} = %d s{i} = %d t{i} = %d" % ("NA", r1, s1, t1))

    # this is a separate loop because we need to pass the s & t values into it.
    if prin:
        print("here we enter the loop")

    # both 'i' and 'prin' are for readability, and don't impact the function at all
    send_out_r, send_out_s, send_out_t = EEALoop(r0, r1, s0, s1, t0, t1, i, prin)

    # here means we've exited out of the recursion part, back to the user

    # This code flips any negative integers(though they're still modular multiplicative inverses), for cleaner use later
    send_out_t, send_out_s = send_out_t % a, send_out_s % b
    if prin:
        print(f"d works, see that the two terms cancel leaving only 1:\n"
              f"d*a mod(b) =  {(send_out_s*r0) % r1}")
    return send_out_r, send_out_s, send_out_t


def EEALoop(old_r, r, old_s, s, old_t, t, i, prin):
    i += 1  # unused if 'prin' is disabled

    if r == 0:  # r_current is zero, marking the end of the loop, our important stuff is 1 step back, in the old values
        # old_r is r-1, marking the greatest common divisor(if r0 = a & r1 = b initially)
        # old_s & old_t then must mark Bezout coefficients, such that old_r = a*old_s + b*old_t (we've found r = a*s + b*t)
        if prin:
            print("internal send-back, we're now returning from recursion, sending our values back")
        return old_r, old_s, old_t
    else:
        # old_r marks the previous for this step(which is overwritten during it), 'r' marks the 'present' step.
        quotient = old_r // r  # defined in terms of r and old_r , which are the step's divisors

        temp_r, temp_s, temp_t = r, s, t  # saving the current 'present' step since they're going to be overwritten
        # new values for r,s,&t, following Euclid's Extended Algorithm's formula
        r = old_r - quotient * r
        s = old_s - quotient * s
        t = old_t - quotient * t
        # the 'present step' we saved earlier, becomes the 'past' step next loop
        old_r, old_s, old_t = temp_r, temp_s, temp_t

        if prin:
            # we print out our values at this layer
            print(f"q{i} = %d r{i} = %d s{i} = %d t{i} = %d" % (quotient, r, s, t))

        # Updated values, time to do some recursion again.
        send_out_r, send_out_s, send_out_t = EEALoop(old_r, r, old_s, s, old_t, t, i, prin)
        # once we're here, we're leaving the loop with our found values
        return send_out_r, send_out_s, send_out_t


# EEA is used for calculating 'd', while the other functions are quality of life, abstracting some of the process of RSA

# the other functions here are used later on, when we're Encrypting and Decrypting, rather than calculating our values

def SimplePadding(Unpadded_message):
    """Returns the message with a simple padding on the ends"""
    # Particular padding isn't important, as this aspect isn't focused on while discussing the RSA Encryption technique
    return "0000" + Unpadded_message + "0000"


def TextToInt(message):
    """Input a string, Returns an integer\n
    not designed for characters with bit equivalents greater than 0xFF, which will return an error message,\n
    ASCII will always work, UNICODE is not guaranteed to work"""
    message_int = 0
    for char in range(len(message)):
        if ord(message[char]) > 0xFF:  # an exception check for if our character is more than 8 bits, which would require a different system
            raise BaseException(f"'{message[char]}' is not usable with this method, please use something else")
        message_int = (message_int << 8) | ord(message[char])
        # This can be read as:
        # slide our current message over 8 bits
        # and add the next character where those newly empty 8 bits are(since ord() turns a character into an int)
        # this makes more sense in hex, since each character is 4 bits
    return message_int


def IntToText(message_int):
    """Input an integer, Returns a string"""
    message_text = ''  # empty string to initialize to.
    hex_m = hex(message_int)  # turns our integer into a hex value, where each 2 characters is an utf-8 value for 'chr' to use
    hex_m = hex_m[2:]  # cuts off the '\x' of the hex value string so the decoder can read it properly.
    for bit in range(0, len(hex_m), 2):  # every 2 hex values are read together.
        char = hex_m[bit:bit+2]  # every two digits make a character in hex to utf-8.
        message_text += chr(int(char, 16))  # decodes hex character using chr (chr needs an integer instead of a hex, so we convert first)
    return message_text
