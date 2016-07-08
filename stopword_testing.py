#encoding=utf-8

import jieba
import jieba.analyse

path_in='testing.txt'
path_out='dict.txt'
f_in=open(path_in,encoding='utf-8')
#f_out=open(path_out,'w')

#for i in f_in.readlines():
#  f_out.write(i)

test_line = f_in.readline()

jieba.analyse.set_stop_words("stopwords.txt")
tags = jieba.analyse.extract_tags(test_line,20)
print(",".join(tags))

##seg_list = jieba.cut(test_line, cut_all=False)
##
### 默认模式
###print("Default Mode: " + "/ ".join(seg_list))
##
##for n in seg_list:
##  print(n)

f_in.close()
#f_out.close()
