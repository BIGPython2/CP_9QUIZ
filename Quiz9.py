settings = int(input("크리스마스 트리의 높이를 설정하세요:"))
for a in range(settings):
    for b in range(settings - a - 1):
        print(" ", end="")
    for c in range(2 * a + 1):
        print("*", end="")
    print()
