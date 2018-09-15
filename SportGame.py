
from random import random

def PrintIntro():      #输出程序的介绍信息
    print('这个程序可以模拟体育竞赛，输出比赛结果')
    print('程序需要手动输入竞技球员的能力值')

def GetInput():
    proA = eval(input('请输入球员A的能力值（0~1）:'))
    proB = eval(input('请输入球员B的能力值（0~1）:'))
    n = eval(input('请输入模拟比赛的次数:'))

    return proA,proB,n

def GameOver(scoreA,scoreB):
    return scoreA == 15 or scoreB == 15


def PlayoneGame(proA,proB):
    scoreA,scoreB = 0,0
    startgame = "A"
    a= random()
    print(a,proA)
    while not GameOver(scoreA,scoreB):
        if startgame == "A":
            if a < proA:

                scoreA = scoreA + 1
            else:
                startgame = "B"
        else:
            if a < proB:
                socreB = scoreB + 1
            else:
                startgame = "A"
    print(scoreA,scoreB)
    return scoreA,scoreB


def PlaynGame(proA,proB,n):
    winA,winB = 0,0
    scoreA,scoreB = 0,0
    for i in range(n):
        scoreA, scoreB = PlayoneGame(proA, proB)
        if scoreA > scoreB:
            winA = winA + 1
        else:
            winB = winB + 1
    return winA,winB


def PrintOutput(winA,winB):
    n = winA + winB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winA,winA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winB,winB/n))


def main():
    PrintIntro()
    proA,proB,n = GetInput()
    winA,winB = PlaynGame(proA,proB,n)
    PrintOutput(winA,winB)

main()

