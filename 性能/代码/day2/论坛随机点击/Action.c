Action()
{
	int i;
//	web_url("���","URL=http://192.168.103.89:8181/dicuz/upload/forum.php?mod=forumdisplay&fid={fid}",LAST);
//	lr_output_message(lr_eval_string("{fid}"));
	//����Ч������һ�ε�������������а����

	//forѭ����ʽ��
	/*
	for(��ʼ�����,�������,ѭ�������仯){

		ѭ����
	}

	for(int i=0;i<10;i++){
		lr_output_message("ֵΪ:%d",i)
	}
    */
	//ע�⣺�ڽű��༭���õ��ı��������������
	for(i=1;i<=7;i++){
		web_url("���","URL=http://192.168.103.89:8181/dicuz/upload/forum.php?mod=forumdisplay&fid={fid}",LAST);
	}

	return 0;
}
