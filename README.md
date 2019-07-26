# Arknights
明日方舟公开招募计算器实现

>环境：python3.7+mysql+flask

仅供学习之用，尝试通过Python+flask实现明日方舟公开招募的计算。

## 目录说明

- aknspider.py 用来一开始爬取初始数据并存入数据库，数据来源明日方舟wiki

- flaskAkn.py  公开招募计算器后端处理。

- template目录 网页文件存放地方

- static目录 静态文件和图片存放地方

- MysqlDATA 初始数据的sql文件


## 说明

运行过程主要是通过点击页面的按钮触发ajax，然后通过ajax生成json对象传递到后端flask处理。

通过flask根据一个或者多个条件查找数据库并返回json，然后把数据显示出来。从而实现游戏中公开招募根据TAG筛选干员。

后台可以添加删除查询修改干员，可以添加后台登陆用户。

通过pyecharts生成图表，要使用Python3.6以上

## 更新

目前只实现了前端大致显示页面，资深干员、高级资深干员还没进行分类，还没写添加修改删除干员功能。 ----2019.06.13

分类OK，还不能添加修改删除干员啊！！！ ----2019.06.17

添加功能有了 ------2019.07.08

后台功能实现了，算是完成了-----2019.07.26 

## 笔记

使用flask-login登录认证记得要先在用户表的数据库模型类中继承UserMixin才可以使用

使用flask-login的login_user,logout_user要先记得写上以下代码
```
# 使用flask_login要有这个，不然login_user()用不了
@login_manager.user_loader  # 使用user_loader装饰器的回调函数非常重要，他将决定 user 对象是否在登录状态
def user_loader(id):  # 这个id参数的值是在 login_user(user)中传入的 user 的 id 属性
    user = aknUser.query.filter_by(id=id).first()
    return user
```

使用pyecharts的组合图表的时候，第一个图不能为饼图。