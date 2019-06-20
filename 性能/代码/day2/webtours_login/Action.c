Action()
{
	//my fist func
	web_url("open","URL=http://192.168.103.143:1080/webtours/",LAST);
	// login
/*	
	web_submit_data("web_submit_data",
		"Action=http://192.168.103.143:1080/webtours/login.pl",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		"Mode=HTML",
		ITEMDATA,
		"Name=userSession", "Value=122780.424058323zDVffVipAzcfDHiQDpVAiDHf", ENDITEM,
		"Name=username", "Value=jojo", ENDITEM,
		"Name=password", "Value=bean", ENDITEM,
		"Name=login.x", "Value=48", ENDITEM,
		"Name=login.y", "Value=11", ENDITEM,
		"Name=login", "Value=Login", ENDITEM,
		"Name=JSFormSubmit", "Value=off", ENDITEM,
		LAST);
*/
	//web_custom_request
	web_custom_request("web_custom_request",
		"URL=http://192.168.103.143:1080/webtours/login.pl",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Mode=HTML",
		"Body=userSession=122780.424058323zDVffVipAzcfDHiQDpVAiDHf&username=jojo&password=bean&login.x=48&login.y=11&login=Login&JSFormSubmit=off",
		LAST);


	return 0;
}
