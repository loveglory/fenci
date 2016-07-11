#encoding=utf-8

import jieba

jieba.load_userdict("dict/dict.txt")

path_in='D:/My Documents/GitHub/material/testing_2.txt'
path_out='dict2.txt'
f_in=open(path_in,encoding='utf-8')
f_out=open(path_out,'w',encoding='utf-8')

com_list=[]

for i in f_in.readlines():
  seg_list = jieba.lcut(i, cut_all=False)
  com_list.extend(seg_list)


countw = []
com_list2=set(com_list)
for k in com_list2:
  f_out.write(k)
  f_out.write(" ")
  f_out.write(str(com_list.count(k)))
  f_out.write("\n")


f_in.close()
f_out.close()
