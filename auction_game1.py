import random

array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]   #点数拍卖顺序
m1 = 12000   #1号玩家金钱数
m2 = 12000
p1 = 0   #1号玩家点数和
p2 = 0
players = [p1,p2]
money = [m1,m2]
plist = [1,2]

print("欢迎来到拍卖游戏!游戏规则如下:")
print(open("rules.txt",encoding="utf-8").read())
print("\n\n")

start = random.choice(plist)   #随机选择玩家作为第1轮开始
plist.remove(start)
after = plist[0]   #另一名玩家
print("第1轮由"+str(start)+"号玩家开始报价\n\n")

for i in array:   #拍卖进行的轮数
    plist = [1,2]
    print("!!第"+str(i)+"轮拍卖开始\n")
    print("1号玩家   点数:"+str(players[0])+";   余额:"+str(money[0]))
    print("2号玩家   点数:"+str(players[1])+";   余额:"+str(money[1])+"\n")

    print("********************"+str(start)+"号玩家回合********************\n")
    #输入并检验报价是否正确
    s = int(input(str(start)+"号玩家报价为:   "))
    while s % 10 != 0:
        print("报价仅允许为10的倍数,请重新报价！")
        s = int(input(str(start)+"号玩家报价为:   "))

    while True:
        print("********************"+str(after)+"号玩家回合********************\n")
        is_compete = input(str(after)+"号玩家是否竞拍?   (y/n)")
        while is_compete != "y" and is_compete != "n":
            print("输入有误!请输入y或n")
            is_compete = input(str(after)+"号玩家是否竞拍?   (y/n)")

        if is_compete == "n":   #此轮结束，进入下一轮
            players[start-1] = players[start-1] + i
            money[start-1] = money[start-1] - s
            print(str(start)+"号玩家获得"+str(i)+"点,消耗"+str(s)+"元\n")
            break

        elif is_compete == "y":
            a = int(input(str(after)+"号玩家报价为:   "))
            while a % 10 != 0:
                print("报价仅允许为10的倍数,请重新报价！")
                a = int(input(str(after)+"号玩家报价为:   "))

            print("********************"+str(start)+"号玩家回合********************\n")
            is_compete = input(str(start)+"号玩家是否竞拍?   (y/n)")
            while is_compete != "y" and is_compete != "n":
                print("输入有误!请输入y或n")
                is_compete = input(str(start)+"号玩家是否竞拍?   (y/n)")

            if is_compete == "n":   #此轮结束，进入下一轮
                players[after-1] = players[after-1] + i
                money[after-1] = money[after-1] - a
                print(str(after)+"号玩家获得"+str(i)+"点,消耗"+str(a)+"元\n")
                
                start = after
                plist.remove(after)
                after = plist[0]

                break

            elif is_compete == "y":
                s = int(input(str(start)+"号玩家报价为:   "))
                while s % 10 != 0:
                    print("报价仅允许为10的倍数,请重新报价！")
                    s = int(input(str(start)+"号玩家报价为:   "))
    continue

#所有拍卖结束，结算最终点数
print("1号玩家点数:"+str(players[0]))
print("2号玩家点数:"+str(players[1]))