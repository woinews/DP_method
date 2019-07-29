# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 15:33:07 2019

@author: chenzx
"""

import pandas as pd
import jieba
import jieba.analyse
from gensim import corpora,models,similarities

top500 = pd.read_excel('2018年财富世界500强.xlsx')

company_list = top500['公司名称(中英文)'].tolist()

# 设置停止词
stoplist=['集团', '公司', '有限公司', ' ', '（', '）',"",'油公司','集团公司']

# 加载用户自定义词典
jieba.load_userdict('dict_world.txt')

all_company_list = []

# jieba cut参数cat_all=True代表全模式，默认为False精确模式
for doc in company_list:
    doc_list = [word for word in jieba.cut(doc,cut_all=True)]
    doc_list = [word for word in doc_list if word not in stoplist]
    all_company_list.append(doc_list)

# 用dictionary方法获取词袋
dictionary = corpora.Dictionary(all_company_list)
# 词袋中用数字对所有词进行了编号 
# dictionary.token2id

# 使用doc2bow制作语料库，利用词袋模型中的字典将其映射到向量空间
corpus = [dictionary.doc2bow(doc) for doc in all_company_list]

print('输入匹配文字:')
name_test = str(input()) #'飞利浦'

name_test_list = [word for word in jieba.cut(name_test,cut_all=True)]
name_test_list = [word for word in name_test_list if word not in stoplist]

# 对匹配文档也进行制作语料库，利用词袋模型中的字典将其映射到向量空间
name_test_vec = dictionary.doc2bow(name_test_list )

# 使用TF-IDF模型对语料库建模，获文档中，每个词的TF-IDF值 tfidf[corpus]
tfidf = models.TfidfModel(corpus)

# 对每个目标文档，分析测试文档的相似度
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
sim = index[tfidf[name_test_vec]]

# 输出匹配前五的公司名称，并舍弃匹配度为0的值
find_5 = sorted(enumerate(sim), key=lambda item: -item[1])[0:5]
find_5 = [_ for _ in find_5 if _[1] >0 ]

print('\n匹配结果:\n')
for i in find_5:
    print(top500.iloc[i[0]]['公司名称(中英文)'], '  匹配度%.2f%%' %(i[1]*100))
