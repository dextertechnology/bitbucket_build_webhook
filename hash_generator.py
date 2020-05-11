#!/usr/bin/env python3

import hashlib, binascii


PASSWORD = b"Welc0me t0 the T9em |f y0u can cr@ck th|5 p@$$w0rd"

def encode(password):
    dk = hashlib.pbkdf2_hmac('sha256', password, b'salt', 234273)

    print("================================================================")
    print(binascii.hexlify(dk).decode("utf-8"))
    print("================================================================")

encode(PASSWORD)
