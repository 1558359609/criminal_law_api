# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ： start_api
@Author ：xiaowu
@Date   ：2022/10/19 14:33
@Desc   ：
=================================================='''
# import pandas as pd
from fastapi import FastAPI
# import nltk
import time
import criminal_law_cn as law

app=FastAPI()


@app.get('/')
def read_root():
    return {'code':200,'info':'hello world'}
@app.get('/getContentByArticleCode/')
def read_content_by_code(article_code:int,article_sub_code:int=None):
    start_time=time.time()
    res=law.getInfoByArticleCode(article_code,article_sub_code)
    res['response_time']=1000*(time.time()-start_time)
    return  res

@app.get('/getCodeByContent/')
def read_code_by_content(content:str,vague:bool):
    start_time=time.time()
    res=law.getInfoByContent(content,vague)
    res['response_time'] = (time.time() - start_time) * 1000
    return res






"""
'part_code':'编',
'chapter_code':'章',
'section_code':'节',
'article_code':'条',
'paragraph_code':'款',
'article_sub_code':'子条',
'part_name':'编名称',
'chapter_name':'章名称',
'section_name':'节名称',
'article_name':'条名称',
'article_content':'条内容(包括所有款)',
'paragraph_content':'款内容'
"""