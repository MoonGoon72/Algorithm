import sys
input = sys.stdin.readline
# 진실을 알고 있는 사람이 없고,
# 진실을 알고 있는 사람과 같은 파티에 참석한 적이 없는 사람들로만 구성된 파티가 과장 가능한 파티
n, m = map(int, input().split())
truthMans = list(map(int, input().split()))
truthMans = set(truthMans[1:]) # 진실을 알고있는 사람

parties = []

for _ in range(m):
    party = list(map(int, input().split()))
    parties.append(party)

for _ in range(m):
    for party in parties:
        for person in party[1:]:
            if person in truthMans:
                for man in party[1:]:
                    truthMans.add(man)
                break

result = 0

for party in parties:
    if not any(element in truthMans for element in party[1:]):
        result += 1

print(result)

'''
아래의 반례를 못찾았었음
5 4
1 5
2 1 2
2 2 3
2 3 4
2 4 5
파티 m번을 반복해야 위의 케이스가 해결이 된다.
'''
