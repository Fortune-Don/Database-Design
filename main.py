from flask import Flask, render_template, request, flash,  jsonify, redirect, url_for, session
from utils import query, map_student_course, recommed_module
import json
import time
import os
import MySQLdb
import pymysql
from config import config

# 创建flask对象
app = Flask(__name__)
app.config['SECRET_KEY'] = 'gsolvit'


# 登录后主页面
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


# 管理员页面
@app.route('/manager', methods=['GET', 'POST'])
def manager():
    return render_template('manager.html')


# 学生管理界面
@app.route('/manageStudent', methods=['GET', 'POST'])
def manageStudent():
    sql = "select * from STUDENT"
    result = query.query(sql)
    return render_template('manageStudent.html', result=result)

# 学生增加界面
@app.route('/manageStudentAdd', methods=['GET', 'POST'])
def manageStudentAdd():
    stu_id = session.get('stu_id') # 识别操作者身份
    if stu_id == 'admin':
        if request.method == 'GET':
            return  render_template('manageStudentAdd.html')
        else:
            stu_id = request.form.get('stu_id')
            name = request.form.get('name')
            sex = request.form.get('sex')
            department = request.form.get('department')
            major = request.form.get('major')
            ad_year = request.form.get('ad_year')
            password = request.form.get('password')
            phone = request.form.get('phone')
            email = request.form.get('email')
            political = request.form.get('political')
            sql = "select * from STUDENT WHERE STU_ID='%s'" % stu_id
            result = query.query(sql)
            if len(result) == 0:
                sql="INSERT INTO STUDENT VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (stu_id,name,sex,department,major,ad_year,password,phone,email,political)
                query.update(sql)
                return redirect(url_for('manageStudent'))
            else:
                return u"该学生已存在"
    else:
        return u'页面不存在'

# 学生删除界面
@app.route('/manageStudentDelete', methods=['GET', 'POST'])
def manageStudentDelete():
    stu_id = session.get('stu_id')
    if stu_id == 'admin':
        if request.method == 'GET':
            return render_template('manageStudentDelete.html')
        else:
            stu_id = request.form.get('stu_id')
            sql="select * from STUDENT WHERE STU_ID='%s'" % stu_id
            result = query.query(sql)
            if len(result) != 0:
                sql="DELETE FROM STUDENT WHERE STU_ID='%s'" % stu_id
                query.update(sql)
                return redirect(url_for('manageStudent'))
            else:
                return u'该学生不存在'
    else:
        return u'页面不存在'

# 学生编辑界面
@app.route('/manageStudentEdit', methods=['GET', 'POST'])
def manageStudentEdit():
    stu_id = session.get('stu_id')
    if stu_id == 'admin':
        if request.method == 'GET':
            return render_template('manageStudentEdit.html')
        else:
            stu_id = request.form.get('stu_id')
            name = request.form.get('name')
            sex = request.form.get('sex')
            department = request.form.get('department')
            major = request.form.get('major')
            ad_year = request.form.get('ad_year')
            password = request.form.get('password')
            phone = request.form.get('phone')
            email = request.form.get('email')
            political = request.form.get('political')
            sql = "select * from STUDENT WHERE STU_ID='%s'" % stu_id
            result = query.query(sql)
            if len(result) != 0:
                if stu_id=='':
                    stu_id=result[0][0]
                if name=='':
                    name=result[0][1]
                if sex=='':
                    sex=result[0][2]
                if department=='':
                    department=result[0][3]
                if major=='':
                    major=result[0][4]
                if ad_year=='':
                    ad_year=result[0][5]
                if password=='':
                    password=result[0][6]
                if phone=='':
                    phone=result[0][7]
                if email=='':
                    email=result[0][8]
                if political=='':
                    political=result[0][9]
                    
                sql="UPDATE STUDENT SET STU_ID ='%s',NAME='%s',SEX='%s',DEPARTMENT='%s',MAJOR='%s',AD_YEAR='%s',PASSWORD='%s',PHONE='%s',EMAIL='%s',POLITICAL='%s' WHERE STU_ID='%s'" % (stu_id,name,sex,department,major,ad_year,password,phone,email,political,stu_id)
                query.update(sql)
                return redirect(url_for('manageStudent'))
            else:
                return u'该学生不存在'
    else:
        return u'页面不存在'

# 学生查找界面
@app.route('/manageStudentQuery', methods=['GET', 'POST'])
def manageStudentQuery():
    stu_id = session.get('stu_id')
    if stu_id == 'admin':
        if request.method == 'GET':
            return render_template('manageStudentQuery.html')
        else:
            stu_id = request.form.get('stu_id')
            sql="select * from STUDENT where stu_id = %s" % stu_id
            result = query.query(sql)
            if len(result) != 0:
                return render_template('manageStudentQuery.html', result=result)
            else:
                return u'该学生不存在'
    else:
        return u'页面不存在'

# 教师管理界面
@app.route('/manageTeacher', methods=['GET', 'POST'])
def manageTeacher():
    sql="select * from TEACHER"
    result = query.query(sql)
    return render_template('manageTeacher.html', result=result)

# 教师增加界面
@app.route('/manageTeacherAdd', methods=['GET', 'POST'])
def manageTeacherAdd():
    stu_id = session.get('stu_id')
    if stu_id == 'admin':
        if request.method == 'GET':
            return  render_template('manageTeacherAdd.html')
        else:
            tea_name = request.form.get('tea_name')
            sex = request.form.get('sex')
            tea_id = request.form.get('tea_id')
            department = request.form.get('department')
            major = request.form.get('major')
            password = request.form.get('password')
            phone = request.form.get('phone')
            email = request.form.get('email')
            title = request.form.get('title')
            sql = "select * from TEACHER WHERE TEA_ID='%s'" % tea_id
            result = query.query(sql)
            if len(result) == 0:
                sql="INSERT INTO TEACHER VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (tea_name,sex,tea_id,department,major,password,phone,email,title)
                query.update(sql)
                return redirect(url_for('manageTeacher'))
            else:
                return u'该教师已存在'
    else:
        return u'页面不存在'

# 教师删除界面
@app.route('/manageTeacherDelete', methods=['GET', 'POST'])
def manageTeacherDelete():
    stu_id = session.get('stu_id')
    if stu_id == 'admin':
        if request.method == 'GET':
            return render_template('manageTeacherDelete.html')
        else:
            tea_id = request.form.get('tea_id')
            sql = "select * from TEACHER WHERE TEA_ID='%s'" % tea_id
            result = query.query(sql)
            if len(result) != 0:
                sql="DELETE FROM TEACHER WHERE TEA_ID='%s'" % tea_id
                query.update(sql)
                return redirect(url_for('manageTeacher'))
            else:
                return u'该教师不存在'
    else:
        return u'页面不存在'


# 教师编辑界面
@app.route('/manageTeacherEdit', methods=['GET', 'POST'])
def manageTeacherEdit():
    stu_id = session.get('stu_id')
    if stu_id == 'admin':
        if request.method == 'GET':
            return render_template('manageTeacherEdit.html')
        else:
            tea_id = request.form.get('tea_id')
            tea_name = request.form.get('tea_name')
            sex = request.form.get('sex')
            department = request.form.get('department')
            major = request.form.get('major')
            password = request.form.get('password')
            phone = request.form.get('phone')
            email = request.form.get('email')
            title = request.form.get('title')
            sql = "select * from TEACHER WHERE TEA_ID='%s'" % tea_id
            result = query.query(sql)
            if len(result) != 0:
                if tea_name=='':
                    tea_name=result[0][0]
                if sex=='':
                    sex=result[0][1]
                if tea_id=='':
                    tea_id=result[0][2]
                if department=='':
                    department=result[0][3]
                if major=='':
                    major=result[0][4]
                if password=='':
                    password=result[0][5]
                if phone=='':
                    phone=result[0][6]
                if email=='':
                    email=result[0][7]
                if title=='':
                    title=result[0][8]
                    
                sql="UPDATE TEACHER SET TEA_NAME ='%s',SEX='%s',TEA_ID='%s',DEPARTMENT='%s',MAJOR='%s',PASSWORD='%s',PHONE='%s',EMAIL='%s',TITLE='%s' WHERE TEA_ID='%s'" % (tea_name,sex,tea_id,department,major,password,phone,email,title,tea_id)
                query.update(sql)
                return redirect(url_for('manageTeacher'))
            else:
                return u'该教师不存在'
    else:
        return u'页面不存在'

# 教师查找界面
@app.route('/manageTeacherQuery', methods=['GET', 'POST'])
def manageTeacherQuery():
    stu_id = session.get('stu_id')
    if stu_id == 'admin':
        if request.method == 'GET':
            return render_template('manageTeacherQuery.html')
        else:
            tea_id = request.form.get('tea_id')
            sql="select * from TEACHER where tea_id = %s" % tea_id
            result = query.query(sql)
            if len(result) != 0:
                return render_template('manageTeacherQuery.html', result=result)
            else:
                return u'该教师不存在'
    else:
        return u'页面不存在'


# 课程管理界面
@app.route('/manageLecture', methods=['GET', 'POST'])
def manageLecture():
    sql = "select * from LECTURE"
    result = query.query(sql)
    return render_template('manageLecture.html', result=result)

# 课程增加界面
@app.route('/manageLectureAdd', methods=['GET', 'POST'])
def manageLectureAdd():
    stu_id = session.get('stu_id')
    if stu_id == 'admin':
        if request.method == 'GET':
            return  render_template('manageLectureAdd.html')
        else:
            ad_year = request.form.get('ad_year')
            major = request.form.get('major')
            classification = request.form.get('classification')
            lec_id = request.form.get('lec_id')
            lec_has = request.form.get('lec_has')
            lec_name = request.form.get('lec_name')
            tea_id = request.form.get('tea_id')
            tea_name = request.form.get('tea_name')
            credit = request.form.get('credit')
            total_hour = request.form.get('total_hour')
            start_time = request.form.get('start_time')
            end_time = request.form.get('end_time')
            lec_time = request.form.get('lec_time')
            MAX_STUDENTS = request.form.get('MAX_STUDENTS')
            semester = request.form.get('semester')
            is_required = request.form.get('is_required')
            department = request.form.get('department')
            mark = request.form.get('mark')
            sql = "select * from LECTURE WHERE LEC_ID='%s'" % lec_id
            result = query.query(sql)
            if len(result) == 0:
                sql="INSERT INTO LECTURE VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (ad_year,major,classification,lec_id,lec_has,lec_name,tea_id,tea_name,credit,total_hour,start_time,end_time,lec_time,MAX_STUDENTS,semester,is_required,department,mark)
                query.update(sql)
                return redirect(url_for('manageLecture'))
            else:
                return u'该课程已存在'
    else:
        return u'页面不存在'

# 课程删除界面
@app.route('/manageLectureDelete', methods=['GET', 'POST'])
def manageLectureDelete():
    stu_id = session.get('stu_id')
    if stu_id == 'admin':
        if request.method == 'GET':
            return render_template('manageLectureDelete.html')
        else:
            lec_id = request.form.get('lec_id')
            sql = "select * from LECTURE WHERE LEC_ID='%s'" % lec_id
            result = query.query(sql)
            if len(result) != 0:
                sql="DELETE FROM LECTURE WHERE LEC_ID='%s'" % lec_id
                query.update(sql)
                return redirect(url_for('manageLecture')) 
            else:
                return u'该课程不存在'
    else:
        return u'页面不存在'

# 课程编辑界面
@app.route('/manageLectureEdit', methods=['GET', 'POST'])
def manageLectureEdit():
    stu_id = session.get('stu_id')
    if stu_id == 'admin':
        if request.method == 'GET':
            return render_template('manageLectureEdit.html')
        else:
            lec_id = request.form.get('lec_id')
            ad_year = request.form.get('ad_year')
            major = request.form.get('major')
            classification = request.form.get('classification')
            lec_has = request.form.get('lec_has')
            lec_name = request.form.get('lec_name')
            tea_id = request.form.get('tea_id')
            tea_name = request.form.get('tea_name')
            credit = request.form.get('credit')
            total_hour = request.form.get('total_hour')
            start_time = request.form.get('start_time')
            end_time = request.form.get('end_time')
            lec_time = request.form.get('lec_time')
            MAX_STUDENTS = request.form.get('MAX_STUDENTS')
            semester = request.form.get('semester')
            is_required = request.form.get('is_required')
            department = request.form.get('department')
            mark = request.form.get('mark')
            sql = "select * from LECTURE WHERE LEC_ID='%s'" % lec_id
            result = query.query(sql)
            if len(result) != 0:
                if lec_id=='':
                    lec_id=result[0][0]
                if ad_year=='':
                    ad_year=result[0][1]
                if major=='':
                    major=result[0][2]
                if classification=='':
                    classification=result[0][3]
                if lec_has=='':
                    lec_has=result[0][4]
                if lec_name=='':
                    lec_name=result[0][5]
                if tea_id=='':
                    tea_id=result[0][6]
                if tea_name=='':
                    tea_name=result[0][7]
                if credit=='':
                    credit=result[0][8]
                if total_hour=='':
                    total_hour=result[0][9]
                if start_time=='':
                    start_time=result[0][10]
                if end_time=='':
                    end_time=result[0][11]
                if lec_time=='':
                    lec_time=result[0][12]
                if MAX_STUDENTS=='':
                    MAX_STUDENTS=result[0][13]
                if semester=='':
                    semester=result[0][19]
                if is_required=='':
                    is_required=result[0][20]
                if department=='':
                    department=result[0][21]
                if mark=='':
                    mark=result[0][22]
                sql="UPDATE LECTURE SET AD_YEAR ='%s', MAJOR='%s', CLASSIFICATION='%s', LEC_HAS='%s', LEC_NAME='%s', TEA_ID='%s', TEA_NAME='%s', CREDIT='%s', TOTAL_HOUR='%s', START_TIME='%s', END_TIME='%s', LEC_TIME='%s', MAX_STUDENTS='%s',SEMESTER='%s',IS_REQUIRED='%s',DEPARTMENT='%s',MARK='%s' WHERE LEC_ID='%s'" % (ad_year,major,classification,lec_has,lec_name,tea_id,tea_name,credit,total_hour,start_time,end_time,lec_time,MAX_STUDENTS,semester,is_required,department,mark,lec_id)
                query.update(sql)
                return redirect(url_for('manageLecture'))
            else:
                return u'该课程不存在'
    else:
        return u'页面不存在'

# 课程查找界面
@app.route('/manageLectureQuery', methods=['GET', 'POST'])
def manageLectureQuery():
    stu_id = session.get('stu_id')
    if stu_id == 'admin':
        if request.method == 'GET':
            return render_template('manageLectureQuery.html')
        else:
            lec_id = request.form.get('lec_id')
            sql="select * from LECTURE where lec_id = %s" % lec_id
            result = query.query(sql)
            if len(result) != 0:
                return render_template('manageLectureQuery.html', result=result)
            else:
                return u'该课程不存在'
    else:
        return u'页面不存在'

@app.route('/', methods=['GET', 'POST'])
# 登录界面
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        stu_id = request.form.get('stu_id')
        password = request.form.get('password')
        
        # 防止sql注入
        result = ''
        sql = "select * from STUDENT where STU_ID = %s"
        db = pymysql.connect('localhost', 'root', config['MYSQL_PASSWORD'], config['DATABASE_NAME'], charset='utf8')
        cur = db.cursor()
        try:
            cur.execute(sql, stu_id)
            result = cur.fetchall()
            print(result)
            db.commit()
        except:
            db.rollback()
        cur.close()
        db.close()

        if len(result) != 0:
            #print(result[0][6], password)
            if result[0][6] == password:
                session['stu_id'] = result[0][0]
                session.permanent=True
                if stu_id=='admin':
                    return redirect(url_for('manager'))
                else:
                    return redirect(url_for('index'))
            else:
                return u'账号或密码错误'
        else:
            return u'不存在这个用户'

# 修改密码界面
@app.route('/edit_password', methods=['GET', 'POST'])
def edit_password():
    if request.method=='GET':
        return render_template('edit_password.html')
    else:
        stu_id = request.form.get('stu_id')
        originalPassword = request.form.get('originalPassword')
        newPassword = request.form.get('newPassword')
        newPassword1 = request.form.get('newPassword1')
        print(stu_id, originalPassword, newPassword, newPassword1)
        # 检查密码
        if(newPassword1 != newPassword):
            return u'两次输入密码不同，请检查'
        else:
            sql = "select * from STUDENT where STU_ID = '%s'" % stu_id
            #print(sql)
            result = query.query(sql)
            #print(result)
            if len(result) == 0:
                return u'不存在这个用户'
            else:
                if result[0][6] == originalPassword:
                    sql = "UPDATE STUDENT SET PASSWORD='%s' WHERE STU_ID='%s'" % (newPassword, stu_id)
                    query.update(sql)
                    return redirect(url_for('edit_password'))
                else:
                    return u'密码错误'
					
# 课程讨论界面
@app.route('/course_discussion', methods=['GET', 'POST'])
def course_discussion():
    if request.method == 'GET':
        return render_template('course_discussion.html')
    else:
        topic = request.form.get('topic')
        comments = request.form.get('comments')
        lec_name = request.form.get('lec_name')
        sql = "select lec_id from LECTURE where lec_name = '%s'" % lec_name
        lec_id = query.query(sql)
        lec_id = lec_id[0][0]
        stu_id = session.get('stu_id')
        sql = "select NAME from STUDENT where STU_ID = '%s'" % stu_id
        stu_name = query.query(sql)
        stu_name = stu_name[0][0]
        now = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))
        now = str(now)
        dis_id = stu_name + now
        sql = "INSERT INTO DISCUSS(DIS_ID, STU_ID, LEC_ID, TOPIC, COMMENT, COMMENTER, IS_FIRST) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '0')" % (dis_id, stu_id, lec_id, topic, comments, stu_name)
        print(sql)
        query.update(sql)
        return redirect(url_for('discuss_center'))

# 讨论中心
@app.route('/discuss_choose/<lec_id>', methods=['GET', 'POST'])
def discuss_choose(lec_id):
    sql = "select * from DISCUSS WHERE IS_FIRST='0' and lec_id = '%s'" % lec_id
    print(sql)
    result = query.query(sql)
    print(result)
    return render_template('discuss_choose.html', result=result)

# 讨论中心界面
@app.route('/discuss_center', methods=['GET', 'POST'])
def discuss_center():
    sql = "select * from lecture"
    result = query.query(sql)
    print(result)
    return render_template('discuss_center.html', result=result)

# 回复界面
@app.route('/detail/<question>', methods=['GET', 'POST'])
def detail(question):
    # 显示当前页面
    if request.method=='GET':
        # 发布者的内容
        sql="SELECT TOPIC, COMMENTS, COMMENTER, CREATE_TIME FROM DISCUSS WHERE DIS_ID='%s' AND IS_FIRST='0'" % (question)
        print(sql)
        title=query.query(sql)
        title=title[0]
        print(title)
        # 评论者的内容
        sql="SELECT * FROM DISCUSS WHERE IS_FIRST='%s'" % question
        result=query.query(sql)
        print(result)
        return render_template('detail.html', title=title, result=result)
    else:
        comments = request.form.get('comments')
        stu_id = session.get('stu_id')
        sql = "select NAME from STUDENT where STU_ID = '%s'" % stu_id
        stu_name = query.query(sql)
        stu_name = stu_name[0][0]
        now = time.time()
        now = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(now))
        now = str(now)
        dis_id = stu_name + now
        # 用is_first来标识该条评论属于此发布者
        sql = "INSERT INTO DISCUSS(DIS_ID, TOPIC, COMMENTS, COMMENTER, IS_FIRST) VALUES ('%s', '回复', '%s', '%s', '%s')" % (dis_id, comments, stu_name, question)
        query.update(sql)

        # print(dis_id)
        # 发布评论之后再打印
        sql = "SELECT TOPIC, COMMENTS, COMMENTER, CREATE_TIME FROM DISCUSS WHERE DIS_ID='%s'" % (question)
        title = query.query(sql)
        print(title)
        title = title[0]
        sql = "SELECT * FROM DISCUSS WHERE IS_FIRST='%s'" % question
        result = query.query(sql)
        return render_template('detail.html', title=title, result=result)

# 个人中心界面：根据"stu_id"从数据库中得到学生基本信息，用于个人中心信息显示
@app.route('/personal_information', methods=['GET', 'POST'])
def personal_information():
    stu_id = session.get('stu_id')
    sql = "SELECT * FROM student WHERE STU_ID = '%s'" % stu_id
    result = query.query(sql)
    return render_template('personal_information.html', result=result)

# 个人信息修改
@app.route('/personal_information_edit', methods=['GET', 'POST'])
def personal_information_edit():
    if request.method == 'GET':
        return render_template('personal_information_edit.html')
    else:
        stu_id = session.get('stu_id')
        phone = request.form.get('phone')
        email = request.form.get('email')
        sql = "UPDATE student SET phone='%s', email='%s' WHERE STU_ID = '%s'" % (phone, email, stu_id)
        query.update(sql)
        return redirect(url_for('personal_information'))

# 培养计划
@app.route('/training_program', methods=['GET', 'POST'])
def training_program():
    return render_template('training_program.html')

# 科学方向
@app.route('/science', methods=['GET', 'POST'])
def science():
    return render_template('science.html')

# 信息方向
@app.route('/information', methods=['GET', 'POST'])
def information():
    return render_template('information.html')

# 工程方向
@app.route('/engineering', methods=['GET', 'POST'])
def engineering():
    return render_template('engineering.html')

# 课程信息
@app.route('/lec_information', methods=['GET', 'POST'])
def lec_information():
    sql = "select * from LECTURE"
    result = query.query(sql)
    stu_id = session.get('stu_id')
    sql = "select grade from CLASS where stu_id = '%s'" % stu_id
    result2 = query.query(sql)
    return render_template('lec_information.html', result=result, result2 = result2)

# 课程信息
@app.route('/lec_detail/<lec_id>', methods=['GET', 'POST'])
def lec_detail(lec_id):
    # 统计人数
    sql = "select * from class where lec_id = '%s'" % lec_id
    result = query.query(sql)
    count = 0
    total = 0
    for person in result:
        count = count + 1
        total = total + person[4]
    average = total / count

    sql = "select * from LECTURE"
    result = query.query(sql)
    return render_template('lec_detail.html', result=result, count = count, average = average)

# 教师界面
@app.route('/tea_information/<teacher>', methods=['GET', 'POST'])
def tea_information(teacher):
    # 显示当前页面
    print(teacher)
    sql = "SELECT * FROM TEACHER WHERE TEA_ID = '%s'" % (teacher)
    print(sql)
    result = query.query(sql)
    print(result)
    return render_template('tea_information.html', result=result)

@app.route('/train_plan', methods=['GET', 'POST'])
def train_plan():
    return render_template('train_plan.html')

# 功能(培养计划界面): 初始进入培养计划界面，根据stu_id从数据库中得到数据并将其转换为计划树所需json格式数据
# :return: planTree:(json) 计划树所需数据
@app.route('/get_info', methods=['GET', 'POST'])
def get_info():
    stu_id = session.get('stu_id')
    planTree = query.getPlanTreeJson(stu_id)
    print(planTree)
    return jsonify(planTree)

# 功能1：实现数据库学生选课信息的更新
# 功能2: 实现计划树以及进度条的提交更新。
# :return:
@app.route('/submit_train_plan', methods=['GET', 'POST'])
def submit_train_place():
    # 功能1：
    twoData = request.get_json(force=True)
    train_plan = twoData['tree']
    scores = twoData['scores']

    #train_plan['name'] = "数据转换成功"
    print('反馈回来的数据是：')
    print(train_plan)
    data = train_plan['children']
    array_finish = [0]*120
    #print(array_finish)
    for data_children in data:
        data_children = data_children['children']
        #print(data_children)
        for data_children_child_1 in data_children:
            #print('data_children_child', data_children_child)
            data_children_child_1 = data_children_child_1['children']
            for data_children_child in data_children_child_1:
                name = data_children_child['children'][0]['name']
                color = data_children_child['children'][0]['itemStyle']['borderColor']
                #print(name, color)
                sql = "select LEC_HAS from LECTURE WHERE LEC_NAME='%s'" % name
                co_100 = query.query(sql)
                co_100 = co_100[0][0]

                if color == 'red':
                    array_finish[int(co_100)] = 0
                else:
                    array_finish[int(co_100)] = 1
    finish_co = ''
    for i in range(1, 119):
        if array_finish[i] == 1:
            finish_co += '1'
        else:
            finish_co += '0'
    print(finish_co)
    #print(array_finish)

    stu_id = session.get('stu_id')
    query.updateDatabase(stu_id, train_plan)
    query.updateScore(stu_id, scores)

    # 功能2：
    train_plan_str = json.dumps(train_plan)
    train_plan_str = train_plan_str.replace("yellow", "green")
    train_plan = json.loads(train_plan_str)
    return jsonify(train_plan)


if __name__ == '__main__':
    app.run("127.0.0.1", port = 8088, debug=True)
