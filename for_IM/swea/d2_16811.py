T = int(input())

for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))
    carrot.sort()
    k = N//2
    carrot_list = {}
    check = True
    sum_carrot_list = []
    result = N

    for i in carrot:
        if i in carrot_list:
            carrot_list[i] += 1
        else:
            carrot_list[i] = 1

    n = len(carrot_list)
    if n < 3:
        print(f'#{tc} -1')
    else:
        for i in carrot_list.values():
            sum_carrot_list.append(i)
            if i > k:
                print(f'#{tc} -1')
                check = False
                break
        
        if check:
            for i in range(1, n):
                sum_carrot_list[i] += sum_carrot_list[i-1]
            for i in range(n-2):
                for j in range(i+1, n-1):
                    so = sum_carrot_list[i]
                    jung = sum_carrot_list[j] - sum_carrot_list[i]
                    dae = sum_carrot_list[n-1] - sum_carrot_list[j]
                    if so > k or  jung > k or dae > k:
                        continue
                    else:
                        if result > max(abs(so-jung), abs(jung-dae), abs(dae-so)):
                            result = max(abs(so-jung), abs(jung-dae), abs(dae-so))

            print(f'#{tc} {result}')

