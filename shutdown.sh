#!/bin/bash

pid=`lsof -i:5000|awk 'NR==2{print $2}'`
echo "进程号为"$pid
if [[ $pid -eq "" ]]
then
   echo "服务已经关闭"
else
   kill -9 $pid
   echo "杀死进程后,已完成服务关闭"
fi
