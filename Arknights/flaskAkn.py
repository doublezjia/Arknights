#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : zealous (doublezjia@163.com)
# @Date    : 2019/5/21 9:25
# @Link    : https://github.com/doublezjia
# @Desc:

import json,os,hashlib
from datetime import datetime
from flask import Flask,render_template,request,redirect,url_for,flash,session,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager,Shell
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate,MigrateCommand
from flask_login import LoginManager,login_required,login_user,logout_user
from flask_login import current_user,UserMixin

# 设置csrf
from flask_wtf.csrf import CsrfProtect
# and_ 连接多条件
from sqlalchemy.sql import and_
from werkzeug import secure_filename
from PIL import Image

from pyecharts import options as opts
from pyecharts.charts import Pie,Bar,Grid,Line
from random import randrange

app = Flask(__name__)
CsrfProtect(app)
bootstrap = Bootstrap(app)
manager = Manager(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "admin_login"
login_manager.login_message = '请先登录.'

# 配置
# 设置图片保存路径
UPLOAD_FOLDER = './static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# 数据库配置信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123@192.168.226.129:3306/arknights'
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
# 干员数据表
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
    imgsrc = db.Column(db.String(255))
    add_time = db.Column(db.DateTime(), default=datetime.utcnow)
    update_time = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<Akn %r>' % self.name

# 用户表，用于登陆后台
# 使用Flask_login要加上UserMixin才可以使用
class aknUser(db.Model,UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    role = db.Column(db.Integer(),default=0)
    status = db.Column(db.Boolean(), default=True, index=True)
    avatar = db.Column(db.String(255))
    add_time = db.Column(db.DateTime(), default=datetime.utcnow)
    update_time = db.Column(db.DateTime(), default=datetime.utcnow)


    def __repr__(self):
        return '<Akn %r>' % self.name


# 集成Python Shell
def make_shell_context():
    return dict(app=app, db=db,Akn=Akn,aknUser=aknUser)


# MD5加密
def aknMd5(str):
    md5 = hashlib.md5()
    md5.update(str.encode(encoding='utf-8'))
    md5_str = md5.hexdigest()
    return md5_str



# 生成图表
# 饼图
def pie_base() -> Pie:
    # 获取星数
    star = []
    starlist = Akn.query.with_entities(Akn.star).distinct().order_by(Akn.star.desc()).all()
    for i in starlist:
        count = Akn.query.filter_by(star=i[0]).count()
        star.append(('%s星' % i[0],count))
    pie = (
        Pie()
        .add('', star, radius=[40, 100])
        .set_global_opts(title_opts=opts.TitleOpts(title="干员星级分布百分比:"),
                         legend_opts=opts.LegendOpts(orient="vertical",pos_left="1%",pos_top="10%"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}"))
    )
    return pie

def pie2_base() -> Pie:
    # 获取阵型
    camp = []
    campdata = Akn.query.with_entities(Akn.camp).distinct().all()
    for i in campdata:
        count = Akn.query.filter_by(camp=i[0]).count()
        camp.append((i[0],count))
    pie = (
        Pie()
        .add('', camp, radius=[40, 80])
        .set_global_opts(title_opts=opts.TitleOpts(title="干员阵型分布百分比:"),
                         legend_opts=opts.LegendOpts(orient="",pos_top="10%"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}"))
    )
    return pie


# 柱形图
def bar_base() -> Bar:
    # 获取职业
    profession = []
    countlist = []
    professionlist = Akn.query.with_entities(Akn.profession).distinct().all()
    for prof in professionlist:
        profession.append(prof[0])
        count = Akn.query.filter_by(profession=prof[0]).count()
        countlist.append(count)
    bar = (
        Bar()
        .add_xaxis(profession)
        .add_yaxis("", countlist)
        .set_global_opts(title_opts=opts.TitleOpts(title="各种类干员统计(单位:个):"),
                         legend_opts=opts.LegendOpts(pos_left="20%"), )
    )
    return bar
# 组合图表，测试怎么使用组合图表
def grid_vertical() -> Grid:
    pie = (
        Pie()
        .add('',[('a',10),('b',20),('c',70)],center=[200,500],radius=[0,75])
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"),
                         legend_opts=opts.LegendOpts(pos_left="10%",pos_top="60%"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    bar = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
        .add_yaxis("商家B", [15, 25, 16, 55, 48, 8])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例"),
                         legend_opts=opts.LegendOpts(pos_left="20%"),)
    )

    grid = (
        Grid()
        .add(bar,grid_opts=opts.GridOpts(pos_right="60%",pos_bottom="60%"))
        .add(pie, grid_opts=opts.GridOpts(pos_left="10%",pos_top="60%"))
    )
    return grid




# 前端
# 主页
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

# 后台处理
# 使用flask_login要有这个，不然login_user()用不了
@login_manager.user_loader  # 使用user_loader装饰器的回调函数非常重要，他将决定 user 对象是否在登录状态
def user_loader(id):  # 这个id参数的值是在 login_user(user)中传入的 user 的 id 属性
    user = aknUser.query.filter_by(id=id).first()
    return user


# 后台登录
@app.route('/admin/login/',methods=['GET','POST'])
def admin_login():
    if request.method == 'POST':
        user = request.form.get('user')
        password = aknMd5(request.form.get('password'))
        akn_user = aknUser.query.filter(aknUser.name==user).first()
        if akn_user.status == 0:
            flash('该账户已禁用.')
            return redirect('admin_login')
        if akn_user is not None and akn_user.password == password:
            login_user(akn_user)
            return redirect(url_for('admin_index'))
        else:
            flash('用户名或者密码不对.')
    return  render_template('admin_login.html')

# 退出登录
@app.route('/admin/logout/',methods=['GET','POST'])
@login_required
def admin_logout():
    logout_user()
    return render_template('admin_login.html')

# 后台用户添加
@app.route('/admin/user/add/',methods=['GET','POST'])
@login_required
def admin_userAdd():
    if current_user.status == 0:
        flash('该账户已禁用.')
        logout_user()
        return redirect(url_for('admin_login'))
    if current_user.role !=1:
        flash('没有权限访问这个页面')
        return redirect(url_for('admin_index'))
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        role = request.form.get('role')
        email = request.form.get('email')

        if aknUser.query.filter_by(name=user).first():
            flash('该用户名已存在.')
            return redirect(url_for('admin_userAdd'))

        if repassword != password:
            flash('确认密码跟输入的密码不一致.')
            return redirect(url_for('admin_userAdd'))

        arkuser = aknUser(name=user,password=aknMd5(password),role=role,email=email)
        db.session.add(arkuser)
        db.session.commit()
        flash('用户添加成功.')
        return redirect(url_for('admin_userAdd'))

    return  render_template('admin_useradd.html')
# 后台修改用户密码
@app.route('/admin/user/repassword/',methods=['GET','POST'])
@login_required
def admin_userRepassword():
    if current_user.status == 0:
        flash('该账户已禁用.')
        logout_user()
        return redirect(url_for('admin_login'))
    if request.method == 'POST':
        oldpassword = request.form.get('oldpassword')
        newpassword = request.form.get('newpassword')
        repassword = request.form.get('repassword')

        if current_user.password != aknMd5(oldpassword):
            flash('旧密码不正确.')
            return redirect(url_for('admin_userRepassword'))
        if repassword != newpassword:
            flash('确认密码跟密码不一致.')
            return redirect(url_for('admin_userRepassword'))

        current_user.password = aknMd5(newpassword)
        current_user.update_time = datetime.now()
        db.session.add(current_user)
        db.session.commit()
        flash('密码修改成功.')
        return redirect(url_for('admin_userRepassword'))
    return  render_template('admin_repassword.html')

# 后台用户列表
@app.route('/admin/user/list/',methods=['GET','POST'])
@login_required
def admin_userList():
    if current_user.status == 0:
        flash('该账户已禁用.')
        logout_user()
        return redirect(url_for('admin_login'))
    if current_user.role !=1:
        flash('没有权限访问这个页面')
        return redirect(url_for('admin_index'))
    data = aknUser.query.all()
    return  render_template('admin_userlist.html',data=data)

# 启用用户
@app.route('/admin/user/enablestatus/<int:id>',methods=['GET','POST'])
@login_required
def admin_enableStatus(id):
    if current_user.status == 0:
        flash('该账户已禁用.')
        logout_user()
        return redirect(url_for('admin_login'))
    if current_user.role != 1:
        flash('没有权限访问这个页面')
        return redirect(url_for('admin_index'))
    user = aknUser.query.get_or_404(id)
    user.status = 1
    db.session.add(user)
    db.session.commit()
    flash('账户已启用.')
    return redirect(url_for('admin_userList'))

# 禁用用户
@app.route('/admin/user/disablestatus/<int:id>',methods=['GET','POST'])
@login_required
def admin_disableStatus(id):
    if current_user.status == 0:
        flash('该账户已禁用.')
        logout_user()
        return redirect(url_for('admin_login'))
    if current_user.role != 1:
        flash('没有权限访问这个页面')
        return redirect(url_for('admin_index'))
    user = aknUser.query.get_or_404(id)
    user.status = 0
    db.session.add(user)
    db.session.commit()
    flash('账户已禁用.')
    return redirect(url_for('admin_userList'))

# 编辑用户资料
@app.route('/admin/user/edit/<int:id>',methods=['GET','POST'])
@login_required
def admin_userEdit(id):
    if current_user.status == 0:
        flash('该账户已禁用.')
        logout_user()
        return redirect(url_for('admin_login'))
    if current_user.role != 1:
        flash('没有权限访问这个页面')
        return redirect(url_for('admin_index'))

    user = aknUser.query.get_or_404(id)
    if request.method == 'POST':
        email = request.form.get('email')
        role = request.form.get('role')
        status = request.form.get('status')

        user.email = email
        user.role = role
        user.status = int(status)
        db.session.add(user)
        db.session.commit()
        flash('更新成功.')
        return redirect(url_for('admin_userEdit',id=user.id))
    return render_template('admin_useredit.html',data=user)

# 删除用户
@app.route('/admin/user/delete/<int:id>',methods=['GET','POST'])
@login_required
def admin_userDelete(id):
    if current_user.status == 0:
        flash('该账户已禁用.')
        logout_user()
        return redirect(url_for('admin_login'))
    if current_user.role != 1:
        flash('没有权限访问这个页面')
        return redirect(url_for('admin_index'))
    user = aknUser.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('用户删除成功.')
    return redirect(url_for('admin_userList'))



# 前端图表请求地址
@app.route("/barChart")
def get_bar_chart():
    bar = bar_base()
    pie = pie_base()
    pie2 = pie2_base()
    result = {
        'pie':json.loads(pie.dump_options()),
        'bar':json.loads(bar.dump_options()),
        'pie2':json.loads(pie2.dump_options()),
    }
    return jsonify(result)


# 后台主页
@app.route('/admin/')
@login_required
def admin_index():
    if current_user.status == 0:
        flash('该账户已禁用.')
        logout_user()
        return redirect(url_for('admin_login'))
    
    return render_template('admin_index.html')

# 后台查询页面
@app.route('/admin/select/',methods=['GET','POST'])
@login_required
def admin_select():
    if current_user.status == 0:
        flash('该账户已禁用.')
        logout_user()
        return redirect(url_for('admin_login'))
    sql = (Akn.id > 0)
    # .with_entities查询某一列，.distinct()去除重复
    # 获取阵营
    camp = Akn.query.with_entities(Akn.camp).distinct().all()
    # 获取职业
    professionlist = Akn.query.with_entities(Akn.profession).distinct().all()
    # 获取星数
    starlist = Akn.query.with_entities(Akn.star).distinct().order_by(Akn.star.desc()).all()
    condition_dict = {
        'profession': professionlist,
        'star': starlist,
        'camp': camp,
        'gender': {'男': 1, '女': 0},
    }

    # 分页
    # 页数请求从request.args.get获得，默认为第一页，int型
    page = request.args.get('page',1,type=int)
    if request.method == 'GET':
        session['name'] = request.args.get('name')
        session['gender'] = request.args.get('gender')
        session['star'] = request.args.get('star')
        session['camp'] = request.args.get('camp')
        session['prof'] = request.args.get('prof')
    if session.get('name') :
        sql = and_(sql,Akn.name == session.get('name') )
    if session.get('gender') :
        sql = and_(sql,Akn.gender == session.get('gender') )
    if session.get('star') :
        sql = and_(sql,Akn.star == session.get('star'))
    if session.get('camp') :
        sql = and_(sql,Akn.camp == session.get('camp') )
    if session.get('prof'):
        sql = and_(sql,Akn.profession == session.get('prof'))
    # 通过paginate对象来获取记录
    # 参数说明：
    # page为页数,从上面的request.args.get获得
    # per_page为每页显示的记录数
    # error_out设置为True时，超出请求页数范围返回的是404错误，设置为False时返回的时候空列表

    pagination = Akn.query.filter(sql).order_by(Akn.id.desc()).paginate(page, per_page=10, error_out=False)
    All_data = pagination.items

    return render_template('admin_select.html',
                           condition_dict=condition_dict, All_data=All_data,
                           pagination=pagination)

# 添加
@app.route('/admin/add',methods=['GET','POST'])
@login_required
def ark_add():
    if current_user.status == 0:
        flash('该账户已禁用.')
        logout_user()
        return redirect(url_for('admin_login'))
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

        if Akn.query.filter_by(name=name).first():
            flash('名称已存在')
            return redirect(url_for('ark_add'))

        # 上传图片
        file = request.files['file1']
        if file and allowed_file(file.filename):
            source_filename = secure_filename(file.filename)
            # 裁剪图片保存
            img_suffix = source_filename.split('.')[-1]
            # imgname = '%s.%s' % (name,img_suffix)
            imgname = '%s.%s' % (name, 'png')
            img = Image.open(file)
            # w,h = img.size
            # avatar = img.crop((w//3,0,w//3 +80,80))
            avatar = img.resize((80,80))
            avatar.save(os.path.join(app.config['UPLOAD_FOLDER'], imgname))
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            imgsrc = '%s/%s' % (os.path.join(app.config['UPLOAD_FOLDER']),imgname)
        else:
            imgsrc = '%s/12F.png' % os.path.join(app.config['UPLOAD_FOLDER'])

        akn = Akn(name=name,camp=camp,gender=gender,star=star,characteristic=characteristic,
                  profession=profession,tag=tag,getway=getway,imgsrc=imgsrc)
        db.session.add(akn)
        db.session.commit()
        flash('添加成功.')
        return redirect(url_for('ark_add'))
    return render_template('admin_add.html',condition_dict=condition_dict)

# 修改
@app.route('/admin/edit/<int:id>',methods=['GET','POST'])
@login_required
def ark_edit(id):
    if current_user.status == 0:
        flash('该账户已禁用.')
        logout_user()
        return redirect(url_for('admin_login'))
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

    aknData = Akn.query.get_or_404(id)

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

        if name != aknData.name:
            if Akn.query.filter_by(name=name).first():
                flash('名称已存在')
                return redirect(url_for('ark_edit',id=aknData.id))

        # 上传图片
        if file and allowed_file(file.filename):
            source_filename = secure_filename(file.filename)
            # 裁剪图片保存
            img_suffix = source_filename.split('.')[-1]
            # imgname = '%s.%s' % (name,img_suffix)
            imgname = '%s.%s' % (name, 'png')
            img = Image.open(file)
            # w,h = img.size
            # avatar = img.crop((w//3,0,w//3 +80,80))
            avatar = img.resize((80,80))
            avatar.save(os.path.join(app.config['UPLOAD_FOLDER'], imgname))
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        aknData.name = name
        aknData.camp = camp
        aknData.gender = gender
        aknData.star = star
        aknData.profession = profession
        aknData.characteristic = characteristic
        aknData.tag = tag
        aknData.getway = getway
        aknData.update_time = datetime.now()
        db.session.add(aknData)
        db.session.commit()
        flash('修改成功.')
        return redirect(url_for('ark_edit',id=aknData.id))

    return render_template('admin_edit.html',condition_dict=condition_dict,data=aknData)

# 删除
@app.route('/admin/delete/<int:id>',methods=['GET','POST'])
@login_required
def ark_delete(id):
    if current_user.status == 0:
        flash('该账户已禁用.')
        logout_user()
        return redirect(url_for('admin_login'))
    arkData = Akn.query.get_or_404(id)
    db.session.delete(arkData)
    db.session.commit()

    os.remove('%s/%s.png' % (os.path.join(app.config['UPLOAD_FOLDER']),arkData.name))

    flash('删除成功。')
    return redirect(url_for('admin_index'))

# 错误代码处理
@app.errorhandler(403)
def page_not_found(e):
    return render_template('error/403.html'),403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'),404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('error/500.html'),500

if __name__ == '__main__':
    manager.add_command("shell",Shell(make_context=make_shell_context()))
    manager.add_command('db', MigrateCommand)
    manager.run()





