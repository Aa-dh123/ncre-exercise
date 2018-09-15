# 题目：
# 请编写程序，生成随机密码。具体要求如下：
#
# （1）使用 random 库，采用 0x1010 作为随机数种子。
#
# （2）密码 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&* 中的字符组成。
#
# （3）每个密码长度固定为 10 个字符。
#
# （4）程序运行每次产生 10 个密码，每个密码一行。
#
# （5）每次产生的 10 个密码首字符不能一样。
#
# （6）程序运行后产生的密码保存在“随机密码.txt”文件中。
#

import random
f = open('随机密码.txt','w+')

random.seed(0x1010)

key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'

password = []
pw = ''
a = ''
while len(password)<10:
    for i in range(10):
            pw += key[random.randint(0,69)]
    if pw[0] not in a:
        password.append(pw)
        a += pw[0]
        pw = ''

f.write('\n'.join(password))
f.close()