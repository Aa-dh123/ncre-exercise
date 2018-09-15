
fname = '天龙八部-网络版.txt'
f = open(fname,'r',encoding='utf-8')
txt = f.read()
txt = txt.replace('\n','').replace(' ','')
count = {}
for i in txt:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

fw = open('天龙八部-汉字统计.csv','w+',encoding = 'utf-8')
for i in count:
    fw.write('{}:{}, '.format(i,count[i]))


f.close()
fw.close()