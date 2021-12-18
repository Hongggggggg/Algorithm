def test_1_wei_bag_problem():
    weight = [1, 3, 4]
    value = [15, 20, 30]

    bag_weight = 4
    dp = [0] * (bag_weight + 1)

    #先遍历物品，再遍历背包容量
    for i in range(len(weight)):
        for j in range(bag_weight, weight[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    print(dp)

test_1_wei_bag_problem()