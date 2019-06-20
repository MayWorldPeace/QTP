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

	
	web_reg_find("Search=All",
		"SaveCount=number",
		"Text=Welcome, <b>{username}</b>",
		LAST);

	lr_start_transaction("login");


	web_submit_data("登录",
		"Action=http://192.168.103.103:1080/webtours/login.pl",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		"Mode=HTML",
		ITEMDATA,
		"Name=userSession", "Value={session}", ENDITEM,
		"Name=username", "Value={username}", ENDITEM,
		"Name=password", "Value={pwd}", ENDITEM,
		"Name=login.x", "Value=36", ENDITEM,
		"Name=login.y", "Value=8", ENDITEM,
		"Name=login", "Value=Login", ENDITEM,
		"Name=JSFormSubmit", "Value=off", ENDITEM,
		LAST);

    
//	lr_end_transaction("login", LR_AUTO);
	//在这里LR_AUTO判断的是服务器的返回状态码，而并没有判断该业务是否成功
	//LR_AUTO的实现方式:
	/*
	a=web_get_int_property(HTTP_INFO_RETURN_CODE);//返回状态码
	if(a == 200){
		lr_end_transaction("login",LR_PASS);
	}else{
		lr_end_transaction("login",LR_FAIL);
	}
*/
	//这个时候可以通过添加检查点的方式来验证业务是否成功，如果存在要检查的内容那么就给一状态LR_PASS，否则给LR_FAIL
	//这个时候就用到一个检查点函数:web_reg_find()---->带有reg的为注册型函数--->特点：如果某一请求的响应数据中有想要的数据，那么就将该函数放在请求前面
	if(atoi(lr_eval_string("{number}"))>0){
		lr_end_transaction("login",LR_PASS);
	}else{
		lr_end_transaction("login",LR_FAIL);
	}

	return 0;
}
