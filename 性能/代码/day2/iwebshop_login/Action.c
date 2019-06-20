Action()
{
	//open
	web_url("open","URL=http://192.168.103.143:8888/iwebshop/",LAST);

	//click denglu
	web_url("click","URL=http://192.168.103.143:8888/iwebshop/index.php?controller=simple&action=login",LAST);

	//LOGIN
    
	web_submit_data("web_submit_data",
		"Action=http://192.168.103.143:8888/iwebshop/index.php?controller=simple&action=login_act",
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
	lr_output_message("output de neirong shi:%s",lr_eval_string("{username}"));


	return 0;
}
