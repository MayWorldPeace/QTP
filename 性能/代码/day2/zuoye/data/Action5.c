Action5()
{

	lr_think_time(5);

	web_submit_data("reservations.pl_4", 
		"Action=http://192.168.103.143:1080/webtours/reservations.pl", 
		"Method=POST", 
		"RecContentType=text/html", 
		"Referer=http://192.168.103.143:1080/webtours/reservations.pl", 
		"Snapshot=t7.inf", 
		"Mode=HTML", 
		ITEMDATA, 
		"Name=Book Another.x", "Value=34", ENDITEM, 
		"Name=Book Another.y", "Value=6", ENDITEM, 
		LAST);

	return 0;
}
