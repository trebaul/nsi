def compte(n):
    if n == 1:
        print(str(n) + '\nPartez !')
    else:
        print(n)
        compte(n-1)