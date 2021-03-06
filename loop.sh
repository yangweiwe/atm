#!/bin/bash
# 设置开始系统时间
date -s $1
# 初始化git仓库
output=`git init`
# 计算天数
days=$(($(($(($(date -d $2 "+%s" ) - $(date -d $1 "+%s" ))) / 86400 ))+1))
# 获取当前执行脚本的绝对路径
basepath=$(cd `dirname $0`; pwd)
# 循环提交
for i in $(seq 1 $days)
do
# 随机数　随机提交次数
random=$((RANDOM % 3 + 1))
        for i in $(seq 1 $random)
        do
#	输出内容 模拟提交
	time=$(date "+%Y%m%d-%H%M%S")
        echo $time >> ${basepath}"/log"
#       echo $time > ${basepath}"/log"
        git add .
        git commit -m"$time"

        done
#　当前时间+1天
time=`date +'%G%m%d %H:%M:%S' -d '+1 days'`
# 更新系统时间
output=`date -s "$time"`
done

# 在执行命令前需要创建一个空的同名repository
git remote add origin git@github.com:yangweiwe/auto.git
git push -u origin master 

# 执行脚本 示例
# bash loop.sh 2017-05-01 2018-7-22
# 设置系统时间
# date -s "2017-07-22 23:54:00"
