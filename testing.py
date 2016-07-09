#encoding=utf-8

import jieba

jieba.load_userdict("dict/dict.txt")

i="我们爱vivoxshot"

seg_list = jieba.cut(i, cut_all=False, HMM=False)

print(" / ".join(seg_list))
