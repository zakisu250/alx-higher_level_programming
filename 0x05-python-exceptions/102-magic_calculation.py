def magic_calculation(a, b):
    ans = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                ans += (a ** b) / i
        except:
            ans = a + b
            break
    return (ans)
