#encoding=utf-8

import jieba

jieba.load_userdict("dict/dict.txt")

path_in='testing.txt'
path_out='dict.txt'
f_in=open(path_in,encoding='utf-8')
f_out=open(path_out,'w',encoding='utf-8')

for i in f_in.readlines():

  seg_list = jieba.cut(i, cut_all=False)

  for n in seg_list:
    f_out.write(n)
    f_out.write("\n")

f_in.close()
f_out.close()
