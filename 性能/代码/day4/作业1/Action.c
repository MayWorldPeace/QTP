Action()
{
		char * str;
		int i;
    	web_reg_save_param("session",
		"LB=name=userSession value=",
		"RB=>",
		"Ord=1",
		LAST);

        web_url("����վ","URL=http://192.168.103.103:1080/webtours/",LAST);

        web_submit_data("��¼",
            "Action=http://192.168.103.103:1080/webtours/login.pl",
            "Method=POST",
            "TargetFrame=",
            "Referer=",
            "Mode=HTML",
            ITEMDATA,
            "Name=userSession", "Value={session}", ENDITEM,
            "Name=username", "Value={user}", ENDITEM,
            "Name=password", "Value={pwd}", ENDITEM,
            "Name=login.x", "Value=36", ENDITEM,
            "Name=login.y", "Value=8", ENDITEM,
            "Name=login", "Value=Login", ENDITEM,
            "Name=JSFormSubmit", "Value=off", ENDITEM,
            LAST);

		lr_output_message("����������Ϊ:%s",lr_eval_string("{pwd}"));
		lr_output_message("�������û���Ϊ:%s",lr_eval_string("{user}"));
        //���fights
		web_url("���fights","URL=http://192.168.103.103:1080/webtours/welcome.pl?page=search",LAST);
//���������Ӧ��������������Ҫ�����ݣ������ҽ������������ڸ�����ǰ��----��ʱ�ø߼�������ʽ
		
	web_reg_save_param("fights",
		"LB=name=outboundFlight value=",
		"RB=>",
		"Ord=ALL",
		LAST);


        //ѡ�������Ŀ�ĵأ����continue
        
	web_submit_data("web_submit_data",
		"Action=http://192.168.103.103:1080/webtours/reservations.pl",
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


	//�߼�����ʹ��ʱ����Ѷ�λ���Ķ��ֵ�ŵ�������������   
   //���ھ���Ҫ����������ȡֵ
//	str=lr_paramarr_idx("fights",lr_paramarr_len("fights")-1);//������������������
//	lr_output_message("%s",str);
	//str�д�ŵ�ֵΪ�ַ��������ǲ��������Բ���ֱ�ӽ��ַ������뵽����Ĵ�����
   //��ʱ����Ҫ���ַ������ݱ��浽������
//	 lr_save_string()
//	 lr_save_string("helloworld","aaa");//��helloworld�������aaa��
//	 lr_output_message(lr_eval_string("{aaa}"));
//	lr_save_string(str,"bbb");

//	lr_output_message(lr_eval_string("{bbb}"));
//	lr_paramarr_len()
//	lr_paramarr_random()
//	lr_paramarr_random("fights");
//	lr_save_string(lr_paramarr_random("fights"),"bbb");

        //ѡ�񺽰���Ϣ���continue
	for(i=1;i<=4;i++){
		
		lr_save_string(lr_paramarr_idx("fights",i),"bbb");
		web_submit_data(lr_eval_string("{bbb}"),
			"Action=http://192.168.103.103:1080/webtours/reservations.pl",
			"Method=POST",
			"TargetFrame=",
			"Referer=",
			"Mode=HTML",
			ITEMDATA,
			"Name=outboundFlight", "Value={bbb}", ENDITEM,
			"Name=numPassengers", "Value=1", ENDITEM,
			"Name=advanceDiscount", "Value=0", ENDITEM,
			"Name=seatType", "Value=Coach", ENDITEM,
			"Name=seatPref", "Value=None", ENDITEM,
			"Name=reserveFlights.x", "Value=60", ENDITEM,
			"Name=reserveFlights.y", "Value=4", ENDITEM,
			LAST);

	}

    //��ҵ��ʹ��һ�ε�����ѡ�񺽰���Ϣ˳��ı���һ��
    //��ҵ����¼--��Ʊʹ�ò������͹���ʵ��

        //���������Ϣ�����continue


	web_submit_data("web_submit_data",
		"Action=http://192.168.103.103:1080/webtours/reservations.pl",
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

