Action()
{
    //web_reg_save_param();
    
	web_reg_save_param("session",
		"LB=name=userSession value=",
		"RB=>",
		"Ord=1",
		LAST);

   
	//打开网站
	web_url("打开网站","URL=http://192.168.103.98:1080/webtours/",LAST);
	//输入用户名和密码进行登录
    //需要实时的获取上一个请求的响应数据中的userSession对应的值，放到登录的请求数据中即可
	// 如果知道如何取值那么就可以实现登录成功
	// 实时获取值的方式：关联
    // 函数名:web_reg_save_param();----->为了获取上一个请求的响应数据中的userSession值
    // 该关联函数：带有reg字样，凡是带有reg字样的函数我们都称为注册型函数
    // 注册型函数的特点：哪个请求的响应数据有我们需要的数据，那么该就放在请求的前面，也就是说该函数需要放在web_url()请求函数的前面
	web_submit_data("登录",
		"Action=http://192.168.103.98:1080/webtours/login.pl",
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

	return 0;
}
