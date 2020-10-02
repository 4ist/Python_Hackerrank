'''
Source: https://www.hackerrank.com/challenges/python-mutations/problem
'''

n=input()
m=input().split()
l=list(n)
l[int(m[1])].replace(m[1])
print(''.join(l))
