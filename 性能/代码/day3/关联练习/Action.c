Action()
{
    	web_reg_save_param("session",
		"LB=name=userSession value=",
		"RB=>",
		"Ord=1",
		LAST);

        web_url("����վ","URL=http://192.168.103.98:1080/webtours/",LAST);

        web_submit_data("��¼",
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

        //���fights
		web_url("���fights","URL=http://192.168.103.98:1080/webtours/welcome.pl?page=search",LAST);
//���������Ӧ��������������Ҫ�����ݣ������ҽ������������ڸ�����ǰ��
        
	web_reg_save_param("fight_data",
		"LB=name=outboundFlight value=",
		"RB=>",
		"Ord=2",
		LAST);


        //ѡ�������Ŀ�ĵأ����continue
        
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



        //ѡ�񺽰���Ϣ���continue
	
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


        //���������Ϣ�����continue


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
