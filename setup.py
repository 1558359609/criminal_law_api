# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ： setup.py
@Author ：xiaowu
@Date   ：2022/10/24 17:09
@Desc   ：
=================================================='''
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="legal_documents_cn", # Replace with your own username
    version="0.0.6",
    author="dongyuwu omnilab",
    author_email="1558359609@qq.com",
    description="Chinese legal documents, you can get certain legal term content by the code of term and the code of term by its content",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['pandas>=1.5.0','nltk>=3.7'],
    python_requires='>=3.7',
    include_package_data=True,  # 打包包含静态文件标识
)