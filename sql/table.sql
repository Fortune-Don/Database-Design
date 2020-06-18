# DROP TABLE IF EXISTS Student;
create table Student(            #学生表
stu_id     varchar(50) COLLATE UTF8_BIN NOT NULL,
name       varchar(50) COLLATE UTF8_BIN NOT NULL,
sex         varchar(50) COLLATE UTF8_BIN,
department  varchar(50) COLLATE UTF8_BIN NOT NULL,
major       varchar(50) COLLATE UTF8_BIN NOT NULL,
ad_year     varchar(50) COLLATE UTF8_BIN NOT NULL,    #入学年份，替代年龄
password    varchar(50) COLLATE UTF8_BIN NOT NULL,
phone      varchar(50) COLLATE UTF8_BIN NOT NULL,
email       varchar(50) COLLATE UTF8_BIN NOT NULL,
political     varchar(50) COLLATE UTF8_BIN NOT NULL,   #政治面貌
primary key (stu_id)
)ENGINE=INNODB DEFAULT CHARSET=UTF8;

# DROP TABLE IF EXISTS Teacher;
create table Teacher(              #教师表
tea_name       varchar(50) COLLATE UTF8_BIN NOT NULL,
sex            varchar(50) COLLATE UTF8_BIN,
tea_id          varchar(50) COLLATE UTF8_BIN NOT NULL,
department     varchar(50) COLLATE UTF8_BIN NOT NULL,
major          varchar(50) COLLATE UTF8_BIN NOT NULL,
tea_pwd       varchar(50) COLLATE UTF8_BIN NOT NULL,
tea_phone         varchar(50) COLLATE UTF8_BIN NOT NULL,
tea_email          varchar(50) COLLATE UTF8_BIN NOT NULL,
title           varchar(50) COLLATE UTF8_BIN NOT NULL,   #职位级别
primary key (tea_id)
)ENGINE=INNODB DEFAULT CHARSET=UTF8;

# DROP TABLE IF EXISTS Lecture;
create table Lecture(                #课程表
lec_year        varchar(255) COLLATE UTF8_BIN NOT NULL,
major          varchar(255) COLLATE UTF8_BIN NOT NULL,
classification    varchar(255) COLLATE UTF8_BIN,    #课程类别（专业选修、必修等）
lec_id          varchar(255) COLLATE UTF8_BIN NOT NULL,
lec_has         varchar(255) COLLATE UTF8_BIN NOT NULL,       #已选课程 
lec_name       varchar(255) COLLATE UTF8_BIN NOT NULL,
tea_id          varchar(255) COLLATE UTF8_BIN NOT NULL, 
tea_name          varchar(255) COLLATE UTF8_BIN NOT NULL,    
credit          decimal(3,1),  #学分 
total_hour     int(10),  #总课时
start_time    date,
end_time     date,
lec_time        varchar(255)COLLATE UTF8_BIN,  #上课时间
max_students INT(10),
semester      INT(2) NOT NULL,
is_required    INT(2) DEFAULT '0',   #是否必修
department VARCHAR(255) COLLATE UTF8_BIN NOT NULL,
NOTE TEXT COLLATE UTF8_BIN,
primary key (lec_id)
)ENGINE=INNODB DEFAULT CHARSET=UTF8;

#DROP TABLE IF EXISTS Class;
create table Class(            #已选课程表
stu_id          varchar(50) COLLATE UTF8_BIN NOT NULL,
ad_year        varchar(50) COLLATE UTF8_BIN NOT NULL, 
major          varchar(50) COLLATE UTF8_BIN NOT NULL,
lec_id          varchar(50) COLLATE UTF8_BIN NOT NULL,        
grade          decimal(5,1),  #总长小于5，小数小于1
comment       varchar(50) COLLATE UTF8_BIN,  #课程评价
primary key (lec_id, stu_id),
foreign key (stu_id) references Student(stu_id),
foreign key (lec_id) references Lecture(lec_id)
)ENGINE=INNODB DEFAULT CHARSET=UTF8;

#DROP TABLE IF EXISTS Discuss;
create table Discuss(              #评价表
dis_id          varchar(50) COLLATE UTF8_BIN NOT NULL,
stu_id           varchar(50) COLLATE UTF8_BIN NOT NULL,
lec_id           varchar(50) COLLATE UTF8_BIN NOT NULL,
topic             varchar(50) COLLATE UTF8_BIN NOT NULL,    #发帖主题 
comment          varchar(50) COLLATE UTF8_BIN NOT NULL,
commenter        varchar(50) COLLATE UTF8_BIN NOT NULL,  
IS_FIRST           VARCHAR(50) COLLATE UTF8_BIN NOT NULL,
CREATE_TIME 		timestamp NOT NULL DEFAULT NOW(), 
primary key (dis_id),
foreign key(stu_id) references Student(stu_id),
foreign key(lec_id) references Lecture(lec_id)
)ENGINE=INNODB DEFAULT CHARSET=UTF8;

create table stu_plan(
stu_id           varchar(50) COLLATE UTF8_BIN NOT NULL,
direction         varchar(50) COLLATE UTF8_BIN,
finished          varchar(225) COLLATE UTF8_BIN,
has_credits       decimal(10,2),
not_credits       decimal(10,2),
primary key(stu_id),
foreign key(stu_id) references Student(stu_id)
)ENGINE=INNODB DEFAULT CHARSET=UTF8;



















