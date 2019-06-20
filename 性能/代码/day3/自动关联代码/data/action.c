Action()
{

	web_set_max_html_param_len("1024");

	/* Registering parameter(s) from source task id 512
	// {WCSParam2} = "122796.104414743zDVzDctpzcAiDDDDDHiQHpQtHHcf"
	// */

	web_reg_save_param("WCSParam2", 
		"LB/IC=name=userSession value=", 
		"RB/IC=>", 
		"Ord=1", 
		"Search=Body", 
		"RelFrameId=1.2.1", 
		LAST);

	web_url("webtours", 
		"URL=http://192.168.103.98:1080/webtours", 
		"TargetFrame=", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=", 
		"Snapshot=t3.inf", 
		"Mode=HTML", 
		LAST);

	lr_think_time(8);

	web_submit_data("login.pl", 
		"Action=http://192.168.103.98:1080/webtours/login.pl", 
		"Method=POST", 
		"TargetFrame=body", 
		"RecContentType=text/html", 
		"Referer=http://192.168.103.98:1080/webtours/nav.pl?in=home", 
		"Snapshot=t4.inf", 
		"Mode=HTML", 
		ITEMDATA, 
		"Name=userSession", "Value={WCSParam2}", ENDITEM, 
		"Name=username", "Value=jojo", ENDITEM, 
		"Name=password", "Value=bean", ENDITEM, 
		"Name=JSFormSubmit", "Value=off", ENDITEM, 
		"Name=login.x", "Value=43", ENDITEM, 
		"Name=login.y", "Value=7", ENDITEM, 
		LAST);

	return 0;
}