n = int(input())

for i in range(1, n+1):
    cnt = 0
    clap = ''

    cnt += str(i).count('3')
    cnt += str(i).count('6')
    cnt += str(i).count('9')

    if cnt > 0:
        for j in range(cnt):
            clap += '-'
        print(clap, end=' ')
    else: print(i, end=' ')