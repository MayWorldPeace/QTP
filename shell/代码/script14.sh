#!/bin/bash
#提示
read -p "请做出平价:" pj
case $pj in
[0-3])
	echo "不满意";;
[4-6])
	echo "满意";;
[7-9])
	echo "非常满意";;
esac
