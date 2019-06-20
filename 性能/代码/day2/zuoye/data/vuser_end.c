vuser_end()
{

	lr_think_time(15);

	web_url("welcome.pl_2", 
		"URL=http://192.168.103.143:1080/webtours/welcome.pl?signOff=1", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=http://192.168.103.143:1080/webtours/nav.pl?page=menu&in=flights", 
		"Snapshot=t8.inf", 
		"Mode=HTML", 
		LAST);

	return 0;
}