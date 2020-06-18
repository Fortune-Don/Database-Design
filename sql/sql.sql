'''
数据库操作步骤
'''
--drop database studenttrainplan;
create database studenttrainplan;
use studenttrainplan;
source table.sql;
set SESSION sql_mode='';
set names 'utf8';
--show variables like "%char%";
source Student.sql;
source Lecture.sql;
source Class.sql;
source stu_plan.sql;
source Teacher.sql;