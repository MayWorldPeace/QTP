Action()
{
    //web_reg_save_param();
    
	web_reg_save_param("session",
		"LB=name=userSession value=",
		"RB=>",
		"Ord=1",
		LAST);

   
	//����վ
	web_url("����վ","URL=http://192.168.103.98:1080/webtours/",LAST);
	//�����û�����������е�¼
    //��Ҫʵʱ�Ļ�ȡ��һ���������Ӧ�����е�userSession��Ӧ��ֵ���ŵ���¼�����������м���
	// ���֪�����ȡֵ��ô�Ϳ���ʵ�ֵ�¼�ɹ�
	// ʵʱ��ȡֵ�ķ�ʽ������
    // ������:web_reg_save_param();----->Ϊ�˻�ȡ��һ���������Ӧ�����е�userSessionֵ
    // �ù�������������reg���������Ǵ���reg�����ĺ������Ƕ���Ϊע���ͺ���
    // ע���ͺ������ص㣺�ĸ��������Ӧ������������Ҫ�����ݣ���ô�þͷ��������ǰ�棬Ҳ����˵�ú�����Ҫ����web_url()��������ǰ��
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

	return 0;
}
