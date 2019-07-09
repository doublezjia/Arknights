#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : zealous (doublezjia@163.com)
# @Date    : 2019/5/21 9:25
# @Link    : https://github.com/doublezjia
# @Desc:

import json,os
from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager,Shell
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate,MigrateCommand
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,TextAreaField,RadioField
# 设置csrf
from flask_wtf.csrf import CsrfProtect
# and_ 连接多条件
from sqlalchemy.sql import and_
from wtforms.validators import Required
from werkzeug import secure_filename
from PIL import Image

app = Flask(__name__)
CsrfProtect(app)
bootstrap = Bootstrap(app)
manager = Manager(app)

# 设置图片保存路径
UPLOAD_FOLDER = './static/img'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# 数据库配置信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost:3306/arknights'
# 设置每次请求完自动提交
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 防止出现这个错误 SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and ，SQLALCHEMY_TRACK_MODIFICATIONS默认不能为空，设置成True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'What animal is the Amiya'
db = SQLAlchemy(app)


# 实现数据库迁移
migrate= Migrate(app,db)

# 判断上传的文件是否为图片
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# 数据库表设计
class Akn(db.Model):
    __tablename__ = 'akn'
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(255),unique=True)
    camp = db.Column(db.String(255))
    profession = db.Column(db.String(255))
    gender = db.Column(db.Integer())
    star = db.Column(db.Integer())
    characteristic = db.Column(db.String(255))
    tag = db.Column(db.String(255))
    getway = db.Column(db.String(255))

    def __repr__(self):
        return '<Akn %r>' % self.name





# 集成Python Shell
def make_shell_context():
    return dict(app=app, db=db,Akn=Akn)








@app.route('/')
def index():
    #data = Akn.query.filter(Akn.gender==1,Akn.tag.like("%新手%"),Akn.tag.like("%远程%"))
    # 获取全部数据
    All_data = Akn.query.all()

    # .with_entities查询某一列，.distinct()去除重复
    # 获取职业
    professionlist = Akn.query.with_entities(Akn.profession).distinct().all()
    # 获取星数
    starlist =  Akn.query.with_entities(Akn.star).distinct().order_by(Akn.star.desc()).all()

    # 获取TAG
    taglist = []
    tagdata = Akn.query.with_entities(Akn.tag).distinct().all()
    for tags in tagdata:
        for tag in tags[0].split('、'):
            # if tag not in taglist and tag != '当前暂不实装':
            if tag not in taglist and tag != '' :
                taglist.append(tag)

    condition_dict = {
        'profession':professionlist,
        'star':starlist,
        'tag':taglist,
        'gender':{'男':1,'女':0},
    }

    return render_template('index.html',All_data=All_data,condition_dict=condition_dict)

@app.route('/add',methods=['GET','POST'])
def ark_add():
    # .with_entities查询某一列，.distinct()去除重复
    # 获取阵营
    camp = Akn.query.with_entities(Akn.camp).distinct().all()
    # 获取职业
    professionlist = Akn.query.with_entities(Akn.profession).distinct().all()
    # 获取星数
    starlist =  Akn.query.with_entities(Akn.star).distinct().order_by(Akn.star.desc()).all()
    condition_dict = {
        'profession': professionlist,
        'star': starlist,
        'camp': camp,
        'gender': {'男': 1, '女': 0},
    }

    if request.method == 'POST':
        name = request.form.get('name')
        gender = request.form.get('gender')
        star = request.form.get('star')
        camp = request.form.get('camp')
        profession = request.form.get('prof')
        characteristic = request.form.get('chara')
        tag = request.form.get('tag')
        getway = request.form.get('getway')

        file = request.files['file1']

        if Akn.query.filter_by(name=name).first():
            flash('名称已存在')
            return redirect(url_for('ark_add'))

        # 上传图片
        if file and allowed_file(file.filename):
            source_filename = secure_filename(file.filename)
            # 裁剪图片保存
            img_suffix = source_filename.split('.')[-1]
            # imgname = '%s.%s' % (name,img_suffix)
            imgname = '%s.%s' % (name, 'png')
            img = Image.open(file)
            w,h = img.size
            avatar = img.crop((w//3,0,w//3 +80,80))
            avatar.save(os.path.join(app.config['UPLOAD_FOLDER'], imgname))

            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        akn = Akn(name=name,camp=camp,gender=gender,star=star,characteristic=characteristic,
                  profession=profession,tag=tag,getway=getway)
        db.session.add(akn)
        flash('添加成功.')
        return redirect(url_for('ark_add'))
    return render_template('arknights_add.html',condition_dict=condition_dict)

# 处理ajax点击查询
@app.route('/select',methods=['GET','POST'])
def select():
    # 新建个列表下面汇总用
    countdata = []

    sql = (Akn.id>0)
    # 获取ajax传递过来的json
    dict = request.get_json()
    if 'tag'in dict:
        if dict['tag']:
            for tag in dict['tag']:
                # 通过sqlalchemy.sql的and_方法实现多条件查询
                sql = and_(sql,Akn.tag.like("%"+tag+"%"))
    if 'profession'in dict:
        if dict['profession']:
            # 通过in_直接查询列表中的值
            sql = and_(sql,Akn.profession.in_(dict['profession']))
    if 'star'in dict:
        if dict['star']:
            # 通过in_直接查询列表中的值
            sql = and_(sql,Akn.star.in_(dict['star']))
    if 'gender'in dict:
        if dict['gender']:
            # 通过in_直接查询列表中的值
            sql = and_(sql,Akn.gender.in_(dict['gender']))


    data = Akn.query.filter(sql).all()


    for i in data:
        seldata = {}
        seldata['name'] = i.name
        seldata['camp'] = i.camp
        seldata['profession'] = i.profession
        if i.gender == 0:
            seldata['gender'] = '女'
        elif i.gender == 1:
            seldata['gender'] = '男'
        else:
            seldata['gender'] = '未知'
        seldata['star'] = i.star
        seldata['characteristic'] = i.characteristic
        seldata['tag'] = i.tag
        countdata.append(seldata)


    # 如果不加ensure_ascii = False,如果有汉字的话都默认给转换成一堆编码如果加上的话就都能正常显示变成了汉字
    return json.dumps(countdata,ensure_ascii=False)

if __name__ == '__main__':
    manager.add_command("shell",Shell(make_context=make_shell_context()))
    manager.add_command('db', MigrateCommand)
    manager.run()





