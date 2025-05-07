S1 = "paraparaparadise"
S2 = "paragraph"
X = set()
Y = set()

for i in range(len(S1)):
    X.add(S1[i:i+2]) # スライスはインデックスエラーにならない
for i in range(len(S2)):
    Y.add(S2[i:i+2])


X_or_Y = X.copy()
X_and_Y = set()
X_dif_Y = X.copy()

for i in Y:
    if i in X:
        X_dif_Y.remove(i)
        X_and_Y.add(i)
    else:
        X_or_Y.add(i)

print(X_or_Y, X_and_Y, X_dif_Y)

print(f'se in X : {'se' in X}')
print(f'se in X : {'se' in Y}')