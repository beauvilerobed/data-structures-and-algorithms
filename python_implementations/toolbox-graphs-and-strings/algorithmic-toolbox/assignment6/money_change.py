

def money_change(money):
    number_of_coins = 0
    while money > 0:
        if money >= 10:
            number_of_coins += (money - money % 10) / 10
            money = money % 10
        elif money >= 5:
            number_of_coins += (money - money % 5) / 5
            money = money % 5
        elif money >= 1:
            number_of_coins += money - money % 1
            money = money % 1
    
    return int(number_of_coins)


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))