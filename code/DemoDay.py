
N, M = (int(x) for x in raw_input().split())

maze = [[0] * M for i in range(N)]
for i in range(N):
    for j,c in enumerate(raw_input().strip()):
        if c == 'b':
            maze[i][j] = 1
max_val = N * M

dp = [[[max_val, max_val] for j in range(M + 1)] for i in range(N + 1)]
dp[1][1] = [0, max_val]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if i == 1 and j == 1:
            continue
        if maze[i-1][j-1] == 1:
            dp[i][j] = [1, 1]
        else:
            dp[i][j] = [0, 0]
        step = 0
        if i + 1 < N and maze[i][j-2] == 0:
            step = dp[i][j-1][1] + 1
        else:
            step = dp[i][j-1][1]
        dp[i][j][0] += min(step, dp[i][j-1][0])

        if j + 1 < M and maze[i-2][j] == 0:
            step = dp[i-1][j][0] + 1
        else:
            step = dp[i-1][j][0]
        dp[i][j][1] += min(step, dp[i-1][j][1])

print min(dp[N][M])
