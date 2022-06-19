if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    for i in range(n):
        if arr[i] > arr[i + 1]:
            print(arr[i])
