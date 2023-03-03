import sys
input = sys.stdin.readline

while True:
    word = input().rstrip()
    if word == 'end':
        break
    word = list(word)
    arr = [[0]*3 for _ in range(3)]
    arr_t = [[0]*3 for _ in range(3)]
    result = 'invalid'
    valid = False
    ans = True

    for i in range(3):
        if not ans:
            break
        for j in range(3):
            char = word.pop(0)
            if valid:
                if char == '.':
                    continue
                else:
                    result = 'invalid'
                    ans = False
                    break
            arr[i][j] = char
            arr_t[j][i] = char
            if i == 2:
                if arr_t[j].count('O') == 3 or arr_t.count('X') == 3:
                    result = 'valid'
                    valid = True
                if j == 0:
                    if arr[j][i] != '.' and arr[j][i] == arr[j+1][i-1] == arr[j+2][i-2]:
                        result = 'valid'
                        valid = True
                elif j == 2:
                    if arr[j-2][j-2] != '.' and arr[j-2][j-2] == arr[j-1][j-1] == arr[j][j]:
                        result = 'valid'
                        valid = True
        if arr[i].count('O') == 3 or arr[i].count('X') == 3:
            result = 'valid'
            valid = True
        
    print(result)


    