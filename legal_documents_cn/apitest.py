# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ： apitest
@Author ：xiaowu
@Date   ：2022/10/19 14:46
@Desc   ：
=================================================='''
import requests
# url='http://127.0.0.1:8000/getContentByArticleCode/?article_code=17&article_sub_code=1'
# content='被告人彭某某有坦白情节'
# # content='交通肇事'
# url=f'http://127.0.0.1:8000/getCodeByContent/?content={content}&vague=True'
# res=requests.get(url)
# print(res.text)
import criminal_law_cn
criminal_law_cn.getContentByArticle(73,6)
