#encoding=utf-8

import jieba

path_in='testing.txt'
path_out='dict2.txt'
f_in=open(path_in,encoding='utf-8')
f_out=open(path_out,'w',encoding='utf-8')

com_list=[]

for i in f_in.readlines():
  seg_list = jieba.lcut(i, cut_all=False)
  com_list.extend(seg_list)


com_list=list(set(com_list))

for j in com_list:
  f_out.write(j)
  f_out.write("\n")

f_in.close()
f_out.close()
