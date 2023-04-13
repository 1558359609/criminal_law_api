# Legal Documents CN 
# criminal_law_cn《中华人民共和国刑法》数据查询功能包 /《刑法》数据查询接口

>[GitHub地址](https://github.com/1558359609/criminal_law_api)
> 
> [PyPI地址](https://pypi.org/project/legal-documents-cn/)

## 功能
《中华人民共和国刑法》
- 可以根据法条的编号查询到法条的内容信息。
- 可以根据法条的内容查询到其所在的章节条等信息，支持模糊查询。

## 安装
```shell
pip install pandas
pip install nltk
pip install legal_documents_cn
```
## 示例

```python
from legal_documents_cn import criminal_law_cn as law
law.getInfoByArticleCode(article_code=219,article_sub_code=1)
#第二百一十九条之一

```

```python
from legal_documents_cn import criminal_law_cn as law
law.getInfoByContent(content='小明交通肇事',vague=True)
#content为需要查询的法条内容，vague为模糊查询

```
```python
law.getInfoByArticleName('交通肇事罪;危险驾驶罪')
#根据案由（法条名称）获取信息内容。需要尽量写全案由名称。
```
```python
law.getInfoByArticleCode(73,3)
#获取第七十三条，第三款具体内容 -> str
```

```python
law.getContentsAll()
#获取刑法中所有的法条内容，return: a list of string
```

## return
```text
dict: 
{'description': '\n中华人民共和国刑法\n颁布日期：2020-12-26\n执行日期：2021-3-1\n时 效 性：现行有效\n刑法是规定犯罪、刑事责任和刑罚的法律，是掌握政权的统治阶级为了维护本阶级政治上的统治和各阶级经济上的利益，根据自己的意志，规定哪些行为是犯罪并且应当负何种刑事责任 ，并给予犯罪嫌疑人何种刑事处罚的法律规范的总称。\n2020年12月26日，第十三届全国人民代表大会常务委员会第二十四次会议通过刑法修正案(十一)。修改后的刑法自2021年3月1日开始施行。这也是继1997年全面修订刑法后通过的第十一个刑法修正案。\n(1979年7月1日第五届全国人民代表大会第二次会议通过，1997年3月14日第八届全国人民代表大会第五次会议修订。根据1999年12月25日中华人民共和国刑法修正案，2001年8月31日中华人民共和国刑法修正案(二)，2001年12月29日中华人民共和国刑法修正案(三)，2002年12 月28日中华人民共和国刑法修正案(四)，2005年2月28日中华人民共和国刑法修正案(五)，2006年6月29日中华人民共和国刑法修正案(六)，2009年2月28日中华人民共和国刑法修正案(七)修正，根据2009年8月27日《全国人民代表大会常务委员会关于修改部分法律的决定》修正，根据2011年2月25日中华人民共和国刑法修正案(八)修正，根据2015年8月29日第十二届全国人民代表大会常务委员会第十六次会议通过的《刑法修正案(九)》修正，根据2017年11月4日第十二届全国人民代表大会常务委员会第三十次会议通过的《刑法修正案（十）》修正，根据2020年12月26日第十三届全国人民代表大会常务委员会第二十四次会议通过的《刑法修正案（十一）》修正。)\n',
 'features': {'part_code': '编',
  'chapter_code': '章',
  'section_code': '节',
  'article_code': '条',
  'paragraph_code': '款',
  'article_sub_code': '子条',
  'part_name': '编名称',
  'chapter_name': '章名称',
  'section_name': '节名称',
  'article_name': '条名称',
  'article_content': '条内容(包括所有款)',
  'paragraph_content': '款内容'},
 'res': {'part_code': 2,
  'chapter_code': 2,
  'section_code': '',
  'article_code': 133,
  'article_sub_code': '',
  'part_name': '分则',
  'chapter_name': '危害公共安全罪',
  'section_name': '',
  'article_name': '【交通肇事罪;危险驾驶罪】',
  'article_content': '【交通肇事罪;危险驾驶罪】违反交通运输管理法规，因而发生重大事故，致人重伤、死亡或者使公私财产遭受重大损失的，处三年以下有期徒刑或者拘役;交通运输肇事后逃逸或者有其他特别恶劣情节的，处三年以上七年以下有期徒刑;因逃逸致人死亡的，处七年以上有期徒刑。'}}

``` 

## 说明
```text
中华人民共和国刑法
颁布日期：2020-12-26
执行日期：2021-3-1
时 效 性：现行有效
刑法是规定犯罪、刑事责任和刑罚的法律，是掌握政权的统治阶级为了维护本阶级政治上的统治和各阶级经济上的利益，根据自己的意志，规定哪些行为是犯罪并且应当负何种刑事责任 ，并给予犯罪嫌疑人何种刑事处罚的法律规范的总称。
2020年12月26日，第十三届全国人民代表大会常务委员会第二十四次会议通过刑法修正案(十一)。修改后的刑法自2021年3月1日开始施行。这也是继1997年全面修订刑法后通过的第十一个刑法修正案。
(1979年7月1日第五届全国人民代表大会第二次会议通过，1997年3月14日第八届全国人民代表大会第五次会议修订。根据1999年12月25日中华人民共和国刑法修正案，2001年8月31日中华人民共和国刑法修正案(二)，2001年12月29日中华人民共和国刑法修正案(三)，2002年12 月28日中华人民共和国刑法修正案(四)，2005年2月28日中华人民共和国刑法修正案(五)，2006年6月29日中华人民共和国刑法修正案(六)，2009年2月28日中华人民共和国刑法修正案(七)修正，根据2009年8月27日《全国人民代表大会常务委员会关于修改部分法律的决定》修正，根据2011年2月25日中华人民共和国刑法修正案(八)修正，根据2015年8月29日第十二届全国人民代表大会常务委员会第十六次会议通过的《刑法修正案(九)》修正，根据2017年11月4日第十二届全国人民代表大会常务委员会第三十次会议通过的《刑法修正案（十）》修正，根据2020年12月26日第十三届全国人民代表大会常务委员会第二十四次会议通过的《刑法修正案（十一）》修正。)
——摘自刑法网
```

# 更新说明
- 2023-4-13:v0.0.11 修复已知BUG
- 2023-2-27:v0.0.10 更新了款的内容提取BUG
- 2023-2-21:v0.0.9 修复已知BUG
- 2023-2-21:v0.0.8 更新了款号的切割方式。（之前带有“项”的款号切割方式不准确）
- 2023-2-20:v0.0.7 更新了通过款号查询的“第X款”查询功能。
