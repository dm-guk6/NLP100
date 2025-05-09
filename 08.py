def cipher(s):
    angou = []
    for az in s:
        if 'a' <= az <= 'z':
            angou.append(chr(219 - ord(az)))
        else:
            angou.append(az)

    angou = "".join(angou)
    return angou

print(cipher("zkkovAPPLE"))
