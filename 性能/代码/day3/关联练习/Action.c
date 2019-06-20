Action()
{
    	web_reg_save_param("session",
		"LB=name=userSession value=",
		"RB=>",
		"Ord=1",
		LAST);

        web_url("打开网站","URL=http://192.168.103.98:1080/webtours/",LAST);

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

        //点击fights
		web_url("点击fights","URL=http://192.168.103.98:1080/webtours/welcome.pl?page=search",LAST);
//该请求的响应数据中有我们需要的数据，所以我将关联函数放在该请求前面
        
	web_reg_save_param("fight_data",
		"LB=name=outboundFlight value=",
		"RB=>",
		"Ord=2",
		LAST);


        //选择出发地目的地，点击continue
        
	web_submit_data("web_submit_data",
		"Action=http://192.168.103.98:1080/webtours/reservations.pl",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		"Mode=HTML",
		ITEMDATA,
		"Name=advanceDiscount", "Value=0", ENDITEM,
		"Name=depart", "Value=Denver", ENDITEM,
		"Name=departDate", "Value=01/15/2018", ENDITEM,
		"Name=arrive", "Value=London", ENDITEM,
		"Name=returnDate", "Value=01/16/2018", ENDITEM,
		"Name=numPassengers", "Value=1", ENDITEM,
		"Name=seatPref", "Value=None", ENDITEM,
		"Name=seatType", "Value=Coach", ENDITEM,
		"Name=findFlights.x", "Value=28", ENDITEM,
		"Name=findFlights.y", "Value=5", ENDITEM,
		"Name=.cgifields", "Value=roundtrip", ENDITEM,
		"Name=.cgifields", "Value=seatType", ENDITEM,
		"Name=.cgifields", "Value=seatPref", ENDITEM,
		LAST);



        //选择航班信息点击continue
	
	web_submit_data("web_submit_data",
		"Action=http://192.168.103.98:1080/webtours/reservations.pl",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		"Mode=HTML",
		ITEMDATA,
		"Name=outboundFlight", "Value={fight_data}", ENDITEM,
		"Name=numPassengers", "Value=1", ENDITEM,
		"Name=advanceDiscount", "Value=0", ENDITEM,
		"Name=seatType", "Value=Coach", ENDITEM,
		"Name=seatPref", "Value=None", ENDITEM,
		"Name=reserveFlights.x", "Value=60", ENDITEM,
		"Name=reserveFlights.y", "Value=4", ENDITEM,
		LAST);


        //输入个人信息，点击continue


	web_submit_data("web_submit_data",
		"Action=http://192.168.103.98:1080/webtours/reservations.pl",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		"Mode=HTML",
		ITEMDATA,
		"Name=firstName", "Value=Joseph", ENDITEM,
		"Name=lastName", "Value=Marshall", ENDITEM,
		"Name=address1", "Value=234 Willow Drive", ENDITEM,
		"Name=address2", "Value=San Jose/CA/94085", ENDITEM,
		"Name=pass1", "Value=Joseph Marshall", ENDITEM,
		"Name=creditCard", "Value=1234567890", ENDITEM,
		"Name=expDate", "Value=", ENDITEM,
		"Name=oldCCOption", "Value=", ENDITEM,
		"Name=numPassengers", "Value=1", ENDITEM,
		"Name=seatType", "Value=Coach", ENDITEM,
		"Name=seatPref", "Value=None", ENDITEM,
		"Name=outboundFlight", "Value=022;320;01/15/2018", ENDITEM,
		"Name=advanceDiscount", "Value=0", ENDITEM,
		"Name=returnFlight", "Value=", ENDITEM,
		"Name=JSFormSubmit", "Value=off", ENDITEM,
		"Name=buyFlights.x", "Value=45", ENDITEM,
		"Name=buyFlights.y", "Value=5", ENDITEM,
		"Name=.cgifields", "Value=saveCC", ENDITEM,
		LAST);


	return 0;
}
