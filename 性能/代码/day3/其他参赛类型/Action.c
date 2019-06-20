Action()
{
//其他参数类型：
	//Data/time类型
	//update value:each iteration--->每次迭代发生变化
//	lr_output_message(lr_eval_string("{datatime}"));
//	lr_output_message(lr_eval_string("{datatime}"));
	//update value:each occurence--->每次出现发生变化
//	lr_output_message(lr_eval_string("{datatime}"));
//	lr_output_message(lr_eval_string("{datatime}"));

	//update value---->once--->一旦取到值不再发生变化
//	lr_output_message(lr_eval_string("{datatime}"));
//	lr_output_message(lr_eval_string("{datatime}"));
// 


	//RandomNumber---->update value--->each iteration--->发生迭代更新值
//	lr_output_message(lr_eval_string("{randomnumber}"));
//	lr_output_message(lr_eval_string("{randomnumber}"));

	//update value--->each occurence-->每次出现更新值
//	lr_output_message(lr_eval_string("{randomnumber}"));
//	lr_output_message(lr_eval_string("{randomnumber}"));
	//update value--->once--->一旦取到值，不再发生变化
//	lr_output_message(lr_eval_string("{randomnumber}"));
//	lr_output_message(lr_eval_string("{randomnumber}"));

//unique number
	lr_output_message(lr_eval_string("{uniquenum}"));

	return 0;
}
