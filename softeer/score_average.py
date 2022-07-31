import sys
n_stduent, k_segment = map(int, sys.stdin.readline().split())
if n_stduent == 1:
    print(int(input()))
else:
    scores = list(map(int, sys.stdin.readline().split()))

    for _ in range(k_segment):
        start, end = map(int, sys.stdin.readline().split())
        start = start-1
        segment = scores[start:end]
        print("{:.2f}".format(sum(segment)/len(segment)))