Action()
{
//1.录制以后关联，必须先运行脚本一次
//2.扫描脚本
// 

//Correlation comment - Do not change!Original value='122796.130741191zDVzDcfpQHfDHiQHpQffif' Name ='CorrelationParameter_1'

	web_reg_save_param_ex(
		"ParamName=CorrelationParameter_1",
		"LB=userSession value=",
		"RB=>\n<table border",
		SEARCH_FILTERS,
		"Scope=Body",
		"RequestUrl=*/nav.pl*",
		LAST);

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
		"Name=userSession", "Value={CorrelationParameter_1}", ENDITEM,
		"Name=username", "Value=jojo", ENDITEM,
		"Name=password", "Value=bean", ENDITEM,
		"Name=JSFormSubmit", "Value=off", ENDITEM,
		"Name=login.x", "Value=35", ENDITEM,
		"Name=login.y", "Value=8", ENDITEM,
		LAST);

return 0;
}
