# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ： process_data
@Author ：xiaowu
@Date   ：2022/10/18 19:14
@Desc   ：
=================================================='''



"""
中华人民共和国刑法

颁布日期：2020-12-26
执行日期：2021-3-1
时 效 性：现行有效

刑法是规定犯罪、刑事责任和刑罚的法律，是掌握政权的统治阶级为了维护本阶级政治上的统治和各阶级经济上的利益，根据自己的意志，规定哪些行为是犯罪并且应当负何种刑事责任 ，并给予犯罪嫌疑人何种刑事处罚的法律规范的总称。

2020年12月26日，第十三届全国人民代表大会常务委员会第二十四次会议通过刑法修正案(十一)。修改后的刑法自2021年3月1日开始施行。这也是继1997年全面修订刑法后通过的第十一个刑法修正案。

(1979年7月1日第五届全国人民代表大会第二次会议通过，1997年3月14日第八届全国人民代表大会第五次会议修订。根据1999年12月25日中华人民共和国刑法修正案，2001年8月31日中华人民共和国刑法修正案(二)，2001年12月29日中华人民共和国刑法修正案(三)，2002年12 月28日中华人民共和国刑法修正案(四)，2005年2月28日中华人民共和国刑法修正案(五)，2006年6月29日中华人民共和国刑法修正案(六)，2009年2月28日中华人民共和国刑法修正案(七)修正，根据2009年8月27日《全国人民代表大会常务委员会关于修改部分法律的决定》修正，根据2011年2月25日中华人民共和国刑法修正案(八)修正，根据2015年8月29日第十二届全国人民代表大会常务委员会第十六次会议通过的《刑法修正案(九)》修正，根据2017年11月4日第十二届全国人民代表大会常务委员会第三十次会议通过的《刑法修正案（十）》修正，根据2020年12月26日第十三届全国人民代表大会常务委员会第二十四次会议通过的《刑法修正案（十一）》修正。)

"""

"""
编：part,
章：chapter
节：section (第一章没有节)
条：article
款：paragraph
项：item
"""
import re
from cn2an import cn2an

features_name='part_code part_name chapter_code chapter_name section_code section_name ' \
              'article_code article_name article_sub_code article_content'.split(' ')

# def getPart(line):
#     #篇 part
#     re_part=re.match(r'(第([一二三四五六七八九十]+?)编) (.*)',line)
#     if re_part!=None:
#         part=re_part.group(2)
#         part_name=re_part.group(3)
#         return part,part_name
#     else:
#         return None
#
# def getChapter(line):
#     #章 chapter
#     re_chapter=re.match(r'(第([一二三四五六七八九十])+?章) (.*)',line)
#     if re_chapter!=None:
#         chapter=re_chapter.group(2)
#         chapter_name=re_chapter.group(3)
#         return chapter,chapter_name
#     else:
#         return None
#
# def getSection(line):
#     #节  section
#     re_section=re.match(r'(第([一二三四五六七八九十])+?节) (.*)',line)
#     if re_section!=None:
#         section=re_section.group(2)
#         section_name=re_section.group(3)
#         return section,section_name
#     else:
#         return None
#
# def getArcticle(line):
#     #条 article
#     re_article=re.match(r'(第([一二三四五六七八九十])+?条)　(【(.*)】.*)',line)
#     if re_article!=None:
#         article=re_article.group(2)
#         article_name=re_article.group(4)
#         article_content=re_article.group(3)
#         return article,article_name,article_content
#     else:
#         return None

#获取章节内的所有内容

def get_criminal_dict(all_txt):
    # matchs_part=re.findall(r'第([一二三四五六七八九十]+?)编 ([\s\S].+?)([\s\S]+?)(?=第[一二三四五六七八九十]+?编 |$)',all_txt)
    criminal_law = {x: [] for x in features_name}

    matchs_part=re.finditer(r'第([一二三四五六七八九十]+?)编 ([\S]*)(\s*)([\s\S]+?)(?=\s第[一二三四五六七八九十]+?编 |$)',all_txt)
    for match_part in matchs_part:
        part_name=match_part.group(2)
        part_code=match_part.group(1)
        content_chapter=match_part.group(4)


        matchs_chapter=re.finditer(r'第([一二三四五六七八九十]+?)章 ([\S]*)(\s*)([\s\S]+?)(?=\s第[一二三四五六七八九十]+?章 |\s第[一二三四五六七八九十]+?编 |$)',content_chapter)
        for match_chapter in matchs_chapter:
            chapter_code=match_chapter.group(1)
            chapter_name=match_chapter.group(2)
            content_section=match_chapter.group(4)



            def re_finditer_articles(content_article):

                matchs_article = re.finditer(
                    r'第([一二三四五六七八九十百]+?)条(之[一二三四五六七])?　(【[\S]*】)?([\s\S]+?)(?=\s第[一二三四五六七八九十百]+?条|\s第[一二三四五六七八九十百]+?节 |\s第[一二三四五六七八九十百]+?章 \s第[一二三四五六七八九十]+?编 |$)',
                    content_article)

                for match_article in matchs_article:
                    article_code = match_article.group(1)  #
                    article_sub_code = match_article.group(2)  # 之一
                    article_name = match_article.group(3)#【盗窃】

                    one_article_content=match_article.group(3) + match_article.group(4) if article_name!=None else match_article.group(4)

                    #汉字转成阿拉伯


                    if section_name==None:
                        criminal_law['section_code'].append(None)
                    else:
                        criminal_law['section_code'].append(cn2an(section_code))
                    if article_sub_code==None:
                        criminal_law['article_sub_code'].append(None)
                    else:
                        criminal_law['article_sub_code'].append(cn2an(article_sub_code.replace('之', '')))
                    criminal_law['part_code'].append(cn2an(part_code))
                    criminal_law['part_name'].append(part_name)
                    criminal_law['chapter_code'].append(cn2an(chapter_code))
                    criminal_law['chapter_name'].append(chapter_name)
                    criminal_law['section_name'].append(section_name)
                    criminal_law['article_code'].append(cn2an(article_code))
                    criminal_law['article_name'].append(article_name)
                    criminal_law['article_content'].append(one_article_content)

            matchs_section = re.finditer(
                r'第([一二三四五六七八九十百]+?)节 ([\S]*)(\s*)([\s\S]+?)(?=\s第[一二三四五六七八九十百]+?节 |\s第[一二三四五六七八九十]+?章 |\s第[一二三四五六七八九十]+?编 |$)',
                content_section)
            is_section=True if len(re.findall(r'第([一二三四五六七八九十百]+?)节 '
                                  r'([\S]*)(\s*)([\s\S]+?)(?=\s第[一二三四五六七八九十百]+?节 '
                                  r'|\s第[一二三四五六七八九十]+?章 |\s第[一二三四五六七八九十]+?编 |$)',
                                  content_section))>0 else False
            if not is_section:#没有节
                section_code=None
                section_name=None
                content_article=content_section
                re_finditer_articles(content_article)
            else:#有节
                for match_section in matchs_section:
                    section_code=match_section.group(1)
                    section_name=match_section.group(2)
                    content_article=match_section.group(4)
                    re_finditer_articles(content_article)


    return criminal_law


import pandas as pd
with open('data/xingfa.txt', 'r', encoding='gbk') as txt:
    lines=txt.read()
    criminal_law=get_criminal_dict(lines)
    df_law=pd.DataFrame(criminal_law)
    # df_law.to_excel('criminal_law.xlsx',encoding='utf_8_sig')
    df_law.to_csv('criminal_law.csv',encoding='utf_8_sig',index=False)
    # print(criminal_law)
    print('ok')