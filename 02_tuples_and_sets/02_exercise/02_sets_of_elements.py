n, m = input().split()

n_set = set([int(input()) for x in range(int(n))])
m_set = set([int(input()) for y in range(int(m))])

unique_elements = n_set & m_set

print(*unique_elements, sep="\n")