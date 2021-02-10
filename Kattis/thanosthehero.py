def main():
    N = int(input())
    worlds = input()

    worldlist = list(map(int, worlds.split(' ')))
    kills = 0
    reversedlist = list(reversed(worldlist))

    for i in range(N-1):
        if reversedlist[i] <= reversedlist[i+1]:
            difference = reversedlist[i+1] - reversedlist[i] + 1
            reversedlist[i+1] -= difference
            kills += difference
            if reversedlist[i+1] < 0:
                return 1
    return kills


if __name__ == "__main__":
    print(main())
