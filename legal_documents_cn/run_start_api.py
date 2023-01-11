# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ： start_api
@Author ：xiaowu
@Date   ：2022/10/19 14:33
@Desc   ：
=================================================='''
import pandas as pd
from fastapi import FastAPI
import nltk
import time
import uvicorn

app=FastAPI()
description="""
中华人民共和国刑法
颁布日期：2020-12-26
执行日期：2021-3-1
时 效 性：现行有效
刑法是规定犯罪、刑事责任和刑罚的法律，是掌握政权的统治阶级为了维护本阶级政治上的统治和各阶级经济上的利益，根据自己的意志，规定哪些行为是犯罪并且应当负何种刑事责任 ，并给予犯罪嫌疑人何种刑事处罚的法律规范的总称。
2020年12月26日，第十三届全国人民代表大会常务委员会第二十四次会议通过刑法修正案(十一)。修改后的刑法自2021年3月1日开始施行。这也是继1997年全面修订刑法后通过的第十一个刑法修正案。
(1979年7月1日第五届全国人民代表大会第二次会议通过，1997年3月14日第八届全国人民代表大会第五次会议修订。根据1999年12月25日中华人民共和国刑法修正案，2001年8月31日中华人民共和国刑法修正案(二)，2001年12月29日中华人民共和国刑法修正案(三)，2002年12 月28日中华人民共和国刑法修正案(四)，2005年2月28日中华人民共和国刑法修正案(五)，2006年6月29日中华人民共和国刑法修正案(六)，2009年2月28日中华人民共和国刑法修正案(七)修正，根据2009年8月27日《全国人民代表大会常务委员会关于修改部分法律的决定》修正，根据2011年2月25日中华人民共和国刑法修正案(八)修正，根据2015年8月29日第十二届全国人民代表大会常务委员会第十六次会议通过的《刑法修正案(九)》修正，根据2017年11月4日第十二届全国人民代表大会常务委员会第三十次会议通过的《刑法修正案（十）》修正，根据2020年12月26日第十三届全国人民代表大会常务委员会第二十四次会议通过的《刑法修正案（十一）》修正。)
"""

feature_map={'part_code':'编','chapter_code':'章','section_code':'节','article_code':'条','paragraph_code':'款','article_sub_code':'子条',
             'part_name':'编名称','chapter_name':'章名称','section_name':'节名称','article_name':'条名称','article_content':'条内容(包括所有款)','paragraph_content':'款内容'}

df=pd.read_csv('criminal_law.csv')
df=df.fillna('')
@app.get('/')
def read_root():
    return {'code':200,'info':'hello world'}
@app.get('/getContentByArticleCode/')
def read_content_by_code(article_code:int,article_sub_code:int=None):
    start_time=time.time()
    res=getContentByArticleCode(article_code,article_sub_code)
    res['response_time']=1000*(time.time()-start_time)
    return  res

@app.get('/getCodeByContent/')
def read_code_by_content(content:str,vague:bool):
    start_time=time.time()
    res=getArticleCodeByContent(content,vague)
    res['response_time'] = (time.time() - start_time) * 1000
    return res

def getContentByArticleCode(article_code:int,article_sub_code:int=None):
    '''
    根据条款的标号获取条款的内容
    :param article_code:
    :return:

    '''

    df_by_article=df[df['article_code']==article_code]
    if article_sub_code!=None:
        df_by_article=df_by_article[df['article_sub_code']==article_sub_code]
    if len(df_by_article)==0:
        return {'code':200,'error':f'未查询到该条款{article_code}之{df_by_article}'}
    return get_info_dict_by_df(df_by_article)
    # return {'code':200,'description':"description"}


def get_info_dict_by_df(df_one_item):
    '''
    通过df的一行数据处理成返回的dict
    :param df_one_item:只有一行数据的df
    :return:dict
    '''
    def convert2int(code):
        try:
            return int(code)
        except Exception as e:
            return ''

    article_content = df_one_item['article_content'].values[0]
    part_code = convert2int(df_one_item['part_code'].values[0])
    chapter_code = convert2int(df_one_item['chapter_code'].values[0])
    section_code = convert2int(df_one_item['section_code'].values[0])
    article_code = convert2int(df_one_item['article_code'].values[0])
    article_sub_code = convert2int(df_one_item['article_sub_code'].values[0])
    part_name = df_one_item['part_name'].values[0]
    chapter_name = df_one_item['chapter_name'].values[0]
    section_name = df_one_item['section_name'].values[0]
    article_name = df_one_item['article_name'].values[0]
    res = {'part_code': part_code, 'chapter_code': chapter_code, 'section_code': section_code,
           'article_code': article_code, 'article_sub_code': article_sub_code,
           'part_name': part_name, 'chapter_name': chapter_name, 'section_name': section_name,
           'article_name': article_name, 'article_content': article_content}
    # print(res)
    return {'code': 200, 'description': description, 'features': feature_map, 'res': res}


def getArticleCodeByContent(content,vague=False):
    def getCHRF(df,query_content=content,reference_column='article_content'):
        return nltk.translate.chrf_score.sentence_chrf(df, query_content)
    if vague==True:
        df['CHRF_score']=df['article_content'].apply(getCHRF)


        # df_conditional=df.iloc[df['CHRF_score'].idxmax()]
        df_conditional=df[df.index==df['CHRF_score'].idxmax()]
    else:
        df_conditional=df[df['article_content'].str.contains(content)]
        if len(df_conditional)>1:
            raise Exception('查询到多条结果，请具体明确法条内容')
    return get_info_dict_by_df(df_conditional)



if __name__ == '__main__':
    uvicorn.run('run_start_api:app',host='114.55.211.167',port=8001)

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