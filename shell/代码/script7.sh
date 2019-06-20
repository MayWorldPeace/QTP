#!/bin/bash
read -p "请输入目录:" dir
d=`ls $dir`
if [ "$d" == "" ];then
	echo "目录为空"
else
	echo "目录不为空"
fi
