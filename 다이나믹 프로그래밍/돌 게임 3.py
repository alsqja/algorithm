# 만약 남은 돌이 1,3,4이고 내 차례라면 무조건 이긴다. 남은 돌이 2개라면 무조건 진다.
# 그 말은 내가 선 플레이어일 때 1개, 3개, 4개인 경우는 무조건 Win이고, 2개일때는 무조건Lose라는 것이다.
# 그럼 돌이 5개일 때는 어떨까?
# 직관적으로는 5개에서 3개를 가져가면 2개를 상대에게 남겨서 패배시킬 수 있다.
# 즉, N개의 돌이 남았을때, N-1, N-3, N-4 중에 Lose값이 있으면 승리할 수 있고, 나머지는 패배한다.

N = int(input())
# dp[i] = i개의 돌을 가지고 게임을 시작 할 때 승/패 여부(단, 선공자 기준)
# dp의 의미: 내가 시작할 때 그 자리에 있으면 패배 -> 5번째부터는 1, 3, 4개의 돌을 집어서 Lose로 보낼 수 있으면 Win, 그럴 수 없으면 Lose
dp = [0, "Win", "Lose", "Win", "Win"] + [0] * (N - 4)  # ['Win', 'Win', 'Lose'... ]


if N <= 4:
    pass
else:
    for i in range(5, N + 1):
        if "Lose" in [dp[i - 1], dp[i - 3], dp[i - 4]]:
            dp[i] = "Win"
        else:
            dp[i] = "Lose"
if dp[N] == "Win":
    print("SK")
else:
    print("CY")
