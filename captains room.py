'''
Source: https://www.hackerrank.com/challenges/py-the-captains-room/problem
'''
K = int(input())
room_numbers = map(int, input().split())
rooms = set(room_numbers)

print( (sum(rooms) * K - sum(room_numbers)) // (K - 1))
