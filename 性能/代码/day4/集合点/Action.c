Action()
{
	int a;
	web_reg_save_param("session",
		"LB=name=userSession value=",
		"RB=>",
		"Ord=1",
		LAST);

   
	//打开网站
	web_url("打开网站","URL=http://192.168.103.103:1080/webtours/",LAST);

	
	
	lr_rendezvous("集合点");


	lr_start_transaction("login");


	web_submit_data("登录",
		"Action=http://192.168.103.103:1080/webtours/login.pl",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		"Mode=HTML",
		ITEMDATA,
		"Name=userSession", "Value={session}", ENDITEM,
		"Name=username", "Value=jojo", ENDITEM,
		"Name=password", "Value=bean", ENDITEM,
		"Name=login.x", "Value=36", ENDITEM,
		"Name=login.y", "Value=8", ENDITEM,
		"Name=login", "Value=Login", ENDITEM,
		"Name=JSFormSubmit", "Value=off", ENDITEM,
		LAST);
    lr_end_transaction("login",LR_AUTO);
    //通过web_find函数检查内容是否存在
    
	web_find("web_find",
		"LeftOf=,",
		"What=Welcome, jojo",
		LAST);

    

	return 0;
}
