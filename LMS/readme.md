# 简介

LMS(Library Management System),是给洛阳理工梦想机器人协会实验室使用的一套管理系统.
## 目录详情
└─LMS
    ├─CMS                   耗材管理
    │  ├─migrations
    │  │  └─__pycache__
    │  └─__pycache__
    ├─DataMS                数据管理
    │  └─migrations
    ├─DMS                   设备管理
    │  ├─migrations
    │  │  └─__pycache__
    │  └─__pycache__
    ├─KBMS                  开发板管理
    │  ├─migrations
    │  │  └─__pycache__
    │  ├─templates
    │  │  └─KBMS
    │  └─__pycache__
    ├─LMS                   主程序
    │  └─__pycache__
    ├─Notice                公告
    │  └─migrations
    ├─PMS                   人员管理
    │  ├─migrations
    │  │  └─__pycache__
    │  └─__pycache__
    ├─RMS                   发票管理
    │  ├─migrations
    │  │  └─__pycache__
    │  └─__pycache__
    ├─templates             view层模板管理
    └─Tracker               行为记录
        ├─migrations
        └─__pycache__

## 变量命名规范

model: Aaaaa_aaaaa
app: KBMS(kitboard mange system)

## TODO

* [x] 完成所有模型的建立
* [ ] 前端采用react框架

## 疑难杂症(杂七杂八的问题)

[数据库问题看这](https://www.cnblogs.com/aaron-agu/p/8985055.html)

### 创建网站管理员

运行`python manage.py createsuperuser`

> 迁移是非常强大的功能，它能让你在开发过程中持续的改变数据库结构而不需要重新删除和创建表 - 它专注于使数据库平滑升级而不会丢失数据。我们会在后面的教程中更加深入的学习这部分内容，现在，你只需要记住，改变模型需要这三步：

### 生成数据库的方法

1.编辑 models.py 文件，改变模型。
2.运行 `python manage.py makemigrations` 为模型的改变生成迁移文件。
3.运行 `python manage.py migrate` 来应用数据库迁移。
