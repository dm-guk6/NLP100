def ngram(n, s, m):
    gram = []
    if m == "moji":
        s = "".join(s)
    for i in range(len(s) - (n - 1)):
        t = ""
        for j in range(n):
            t += s[i + j]
        gram.append(t)
    return (gram)

number = int(input())
string = input().split(" ")
mode = input()
print(ngram(number, string, mode))