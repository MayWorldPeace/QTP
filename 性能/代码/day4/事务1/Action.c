Action()
{
	int a;
	web_reg_save_param("session",
		"LB=name=userSession value=",
		"RB=>",
		"Ord=1",
		LAST);

   
	//����վ
	web_url("����վ","URL=http://192.168.103.103:1080/webtours/",LAST);

	
	web_reg_find("Search=All",
		"SaveCount=number",
		"Text=Welcome, <b>{username}</b>",
		LAST);

	lr_start_transaction("login");


	web_submit_data("��¼",
		"Action=http://192.168.103.103:1080/webtours/login.pl",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		"Mode=HTML",
		ITEMDATA,
		"Name=userSession", "Value={session}", ENDITEM,
		"Name=username", "Value={username}", ENDITEM,
		"Name=password", "Value={pwd}", ENDITEM,
		"Name=login.x", "Value=36", ENDITEM,
		"Name=login.y", "Value=8", ENDITEM,
		"Name=login", "Value=Login", ENDITEM,
		"Name=JSFormSubmit", "Value=off", ENDITEM,
		LAST);

    
//	lr_end_transaction("login", LR_AUTO);
	//������LR_AUTO�жϵ��Ƿ������ķ���״̬�룬����û���жϸ�ҵ���Ƿ�ɹ�
	//LR_AUTO��ʵ�ַ�ʽ:
	/*
	a=web_get_int_property(HTTP_INFO_RETURN_CODE);//����״̬��
	if(a == 200){
		lr_end_transaction("login",LR_PASS);
	}else{
		lr_end_transaction("login",LR_FAIL);
	}
*/
	//���ʱ�����ͨ����Ӽ���ķ�ʽ����֤ҵ���Ƿ�ɹ����������Ҫ����������ô�͸�һ״̬LR_PASS�������LR_FAIL
	//���ʱ����õ�һ�����㺯��:web_reg_find()---->����reg��Ϊע���ͺ���--->�ص㣺���ĳһ�������Ӧ����������Ҫ�����ݣ���ô�ͽ��ú�����������ǰ��
	if(atoi(lr_eval_string("{number}"))>0){
		lr_end_transaction("login",LR_PASS);
	}else{
		lr_end_transaction("login",LR_FAIL);
	}

	return 0;
}
