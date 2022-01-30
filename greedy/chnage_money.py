LIST_CHANGE_MONEY = [500, 100, 50, 10]

def change_money(money):
    temp_money = money
    return_coins=[0, 0, 0, 0]
    for idx, coin in enumerate(LIST_CHANGE_MONEY):
        return_coins[idx] = temp_money // coin
        temp_money %=  coin

    return return_coins

if __name__ == '__main__':
    input_moeny = int(input("Input money : "))
    result = change_money(input_moeny)
    print(sum(result))