s = input()
compare_alpha = 'АВЕКМНОРСТУХ'

if len(s) >= 9 and s[0] in compare_alpha and '0' <= s[1] <= '9' and '0' <= s[2] <= '9' and '0' <= s[3] <= '9' and s[
    4] in compare_alpha and s[5] in compare_alpha and s[6] == '_' and '0' <= s[7] <= '9' and '0' <= s[8] <= '9':
    if len(s) == 10 and '0' <= s[9] <= '9':
        print('YES')
    elif len(s) == 9:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
