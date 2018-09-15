import jieba

sign = ['！','？','｡','＂','＃',' ','＄','％','＆','＇','（','）','＊','＋','，','－','／','：','；','＜','＝','\\','＞','＠','［','＼','］','＾','＿','｀','｛','｜','｝','～','｟','｠','｢','｣',',''、','〃','》',',','「','」','『','』','【','】','〔','〕','〖','〗','〘','〙','〚','〛','〜','〝','〞','〟','〰','〾','–—','‘','’','‛''“','”','„','‟','…','‧','﹏','.']

f = open('天龙八部-网络版.txt','r',encoding = 'utf-8')
f.read()
for i in sign:
    if i in f:
        f.replace(i,'')
count_word = {}
txt = jieba.lcut(f)
for i in txt:
    if i not in count_word:
        count_word[i] = 1
    else:
        count_word += 1
fw = open('天龙八部-词语统计.txt','w+',encoding = 'utf-8')
for i in count_word:
    fw.write('{}:{}, '.format(i,count_word[i]))
f.close()
fw.close()