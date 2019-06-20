#!/bin/bash
#提示
read -p "请输入产品:" pro
case $pro in
"A")
	echo "笔几本";;
"B")
	echo "电凡报";;
"C")
	echo "小台灯";;
esac
