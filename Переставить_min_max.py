s1 = input().split()
s = []
for i in s1[:]:
    s.append(int(i))
if len(s) == 1:
    print(*s)
else:
    l_index = s.index(max(s))
    m_index = s.index(min(s))
    l = s[l_index]
    m = s[m_index]
    s[l_index] = 0
    s[m_index] = 0
    s[l_index] = m
    s[m_index] = l
    print(*s)
