Action()
{
	int i;
//	web_url("点击","URL=http://192.168.103.89:8181/dicuz/upload/forum.php?mod=forumdisplay&fid={fid}",LAST);
//	lr_output_message(lr_eval_string("{fid}"));
	//换个效果：想一次迭代，随机将所有板块点击

	//for循环格式：
	/*
	for(初始化语句,条件语句,循环变量变化){

		循环体
	}

	for(int i=0;i<10;i++){
		lr_output_message("值为:%d",i)
	}
    */
	//注意：在脚本编辑区用到的变量必须放在首行
	for(i=1;i<=7;i++){
		web_url("点击","URL=http://192.168.103.89:8181/dicuz/upload/forum.php?mod=forumdisplay&fid={fid}",LAST);
	}

	return 0;
}
