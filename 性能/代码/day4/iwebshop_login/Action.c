Action()
{
	//open
	web_url("open","URL=http://192.168.103.103:8888/iwebshop/",LAST);

	//click denglu
	web_url("click","URL=http://192.168.103.103:8888/iwebshop/index.php?controller=simple&action=login",LAST);

    
	web_reg_find("Search=All",
		"SaveCount=num",
		"Text={username}",
		LAST);

	//LOGIN
	lr_start_transaction("开始事务点");

	web_submit_data("web_submit_data",
		"Action=http://192.168.103.103:8888/iwebshop/index.php?controller=simple&action=login_act",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		"Mode=HTML",
		ITEMDATA,
		"Name=callback", "Value=", ENDITEM,	
		"Name=login_info", "Value={username}", ENDITEM,
		"Name=password", "Value=123456", ENDITEM,
		LAST);
	
//	lr_output_message(lr_eval_string("{username}"));
//	lr_output_message("output de neirong shi:%s",lr_eval_string("{username}"));
	if(atoi(lr_eval_string("{num}"))>0){
		lr_end_transaction("开始事务点",LR_PASS);
	}else{
		lr_end_transaction("开始事务点",LR_FAIL);
	}

	return 0;
}
