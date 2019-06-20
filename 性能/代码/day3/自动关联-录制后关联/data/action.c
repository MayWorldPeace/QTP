Action()
{

	web_url("webtours", 
		"URL=http://192.168.103.98:1080/webtours", 
		"TargetFrame=", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=", 
		"Snapshot=t1.inf", 
		"Mode=HTML", 
		LAST);

	lr_think_time(7);

	web_submit_data("login.pl", 
		"Action=http://192.168.103.98:1080/webtours/login.pl", 
		"Method=POST", 
		"TargetFrame=body", 
		"RecContentType=text/html", 
		"Referer=http://192.168.103.98:1080/webtours/nav.pl?in=home", 
		"Snapshot=t2.inf", 
		"Mode=HTML", 
		ITEMDATA, 
		"Name=userSession", "Value=122796.130741191zDVzDcfpQHfDHiQHpQffif", ENDITEM, 
		"Name=username", "Value=jojo", ENDITEM, 
		"Name=password", "Value=bean", ENDITEM, 
		"Name=JSFormSubmit", "Value=off", ENDITEM, 
		"Name=login.x", "Value=35", ENDITEM, 
		"Name=login.y", "Value=8", ENDITEM, 
		LAST);

	return 0;
}