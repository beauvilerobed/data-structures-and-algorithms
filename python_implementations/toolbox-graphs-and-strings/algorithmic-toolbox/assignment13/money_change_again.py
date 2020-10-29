

def change(money):
    coins = [1, 3, 4]
    len_coins = len(coins)
    min_num_coins = [0 for _ in range(money + 1)]
    for m in range(1, len(min_num_coins)):
        min_num_coins[m] = float('inf')
        for i in range(len_coins):
            if m >= coins[i]:
                num_coins = min_num_coins[m - coins[i]] + 1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins

    return min_num_coins[money]


def main():
    amount = int(input())
    print(change(amount))


if __name__ == '__main__':
    main()
