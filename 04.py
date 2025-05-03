S = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split(" ")
n = {1, 5, 6, 7, 8, 9, 15, 16, 19}
dictionary = dict()

for i in range(len(S)):
    if i + 1 in n:
        dictionary[S[i][:2]] = i + 1
    else:
        dictionary[S[i][0]] = i + 1

print(dictionary)