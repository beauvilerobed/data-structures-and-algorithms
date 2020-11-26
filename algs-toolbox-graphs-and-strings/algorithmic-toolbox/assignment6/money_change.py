def money_change(money):
    count = 0
    denom = [10, 5, 1]

    # greedy chioce will be the largest denomination
    while money > 0:
        for val in denom:
            if money >= val:
                number = (money - money % val) // val
                count += number
                money = money - number * val
                break

    return count


def main():
    input_money = int(input())
    print(money_change(input_money))

if __name__ == '__main__':
    main()
