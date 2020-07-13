def de_bruijn(k, n):
    try:
        _ = int(k)
        alphabet = list(map(str, range(k)))
 
    except (ValueError, TypeError):
        alphabet = k
        k = len(k)
 
    a = [0] * k * n
    sequence = []
 
    def db(t, p):
        if t > n:
            if n % p == 0:
                sequence.extend(a[1:p + 1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)
    db(1, 1)
    return "".join(alphabet[i] for i in sequence)
 
n = int(input())
print(de_bruijn(2, n), end='')
for i in range(1, n):
    print(0, end='')