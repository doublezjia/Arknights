#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : zealous (doublezjia@163.com)
# @Date    : 2019/5/15 9:55
# @Link    : https://github.com/doublezjia
# @Desc: Arknights

import requests,time,sys,os
from lxml import etree
import pymysql

url = 'http://wiki.joyme.com/arknights/%E5%B9%B2%E5%91%98%E6%95%B0%E6%8D%AE%E8%A1%A8'

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
}

db_user = 'user'
db_pwd = 'passwd'
db_host = 'localhost'
db_port = 3306
database = 'arknights'

# 数据库连接
def sql_conn():
    db = pymysql.connect(host=db_host,port=db_port,user=db_user,passwd=db_pwd,
                         db=database,charset='utf8')
    return db

# 查询数据库
def sql_select(**karg):
    sql = "select * from akn "

    if karg['gender']:
        for i in karg['gender']:
            if i == '男':
                i = 1
            elif i == '女':
                i = 0
            else:
                i = 2

            if 'where' not in sql:
                condition = " where gender='%s'" % i
                sql = sql + condition
            else:
                condition = " and gender='%s'" % i
                sql = sql + condition

    if karg['profession']:
        for i in karg['profession']:
            if 'where' not in sql:
                condition = " where profession='%s'" % i
                sql = sql + condition
            else:
                condition = " and profession='%s'" % i
                sql = sql + condition

    if karg['camp']:
        for i in karg['camp']:
            if 'where' not in sql:
                condition = " where camp='%s'" % i
                sql = sql + condition
            else:
                condition = " and camp='%s'" % i
                sql = sql + condition

    if karg['tag']:
        for i in karg['tag']:
            if 'where' not in sql:
                condition = " where tag like '%" + i + "%'"
                sql = sql + condition
            else:
                condition = " and tag like '%" + i + "%' "
                sql = sql + condition

    print (sql)

    db = sql_conn()
    cursor=db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    return results
    db.close()

# 添加数据到数据库
def sql_insert(name,camp,profession,gender,star,characteristic,tag,getway):
    sql = "insert into akn(name,camp,profession,gender,star,characteristic," \
          "tag,getway) values('%s','%s','%s','%s','%s','%s','%s','%s')" % \
          (name,camp,profession,gender,star,characteristic,tag,getway)

    db=sql_conn()
    cursor=db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        print ('Insert Successful.')
    except:
        db.rollback()
    db.close()

# 更新数据库
def sql_update(prof,id):
    sql = "update akn set profession='%s' where id=%s" % (prof,id)

    db = sql_conn()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        print('Update Successful.')
    except:
        db.rollback()
    db.close()


# 下载爬虫的图片
def down_pic(url,fname):
    req = requests.get(url,headers=headers)
    with open('./static/img/%s' % fname.replace('05',''),'wb') as f:
        f.write(req.content)

# 爬虫
def akninfo(url,headers):
    req = requests.get(url,headers=headers)
    html = etree.HTML(req.text,etree.HTMLParser())
    result = html.xpath('//table[@id="CardSelectTr"]/tr[position()>1]')
    for i in result:
        yield {
            'name':i.xpath('./td[2]/a/text()')[0].replace("\n","").strip(),
            'camp':i.xpath('./td[3]/text()')[0].replace("\n","").strip(),
            'profession': i.xpath('./td[4]/text()')[0].replace("\n","").strip(),
            'gender': i.xpath('./td[6]/text()')[0].replace("\n","").strip(),
            'star': i.xpath('./td[5]/text()')[0].replace("\n","").strip(),
            'characteristic': i.xpath('./td[18]/text()')[0].replace("\n","").strip(),
            'tag': i.xpath('./td[19]/text()')[0].replace("\n","").strip(),
            'getway': i.xpath('./td[8]/text()')[0].replace("\n","").strip(),
            'imgname': i.xpath('./td[1]/div/div/a/img/@alt')[0],
            'imgurl': i.xpath('./td[1]/div/div/a/img/@src')[0],
        }

# 处理爬虫结果，存入数据库
def main ():
    information_dict = akninfo(url,headers)
    for i in information_dict:
        name = i['name']
        camp = i['camp']
        profession = i['profession']
        if i['gender'] == '女':
            gender = 0
        elif i['gender'] == '男':
            gender = 1
        else:
            gender = 2
        star=i['star']
        characteristic=i['characteristic']
        tag=i['tag']
        getway=i['getway']
        imgname = i['imgname']
        imgurl = i['imgurl']
        sql_insert(name=name,camp=camp,profession=profession,
                   gender=gender,star=star,characteristic=characteristic,tag=tag,getway=getway)
        down_pic(url=imgurl,fname=imgname)



if __name__ == '__main__':
    main()
