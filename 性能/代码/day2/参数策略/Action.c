Action()
{


	//Sequential---A1
	//Random---A2
	// unique---A3
	// Each iteration---B1
	// each occurences----B2
	// once-----B3
	//组合1----A1B1----->不管输出多少内容，只要是同一次迭代，输出的值相同
	// 
		//输出参数的值
//	lr_output_message(lr_eval_string("{lrpwd}"));
//	lr_output_message(lr_eval_string("{lrpwd}"));

	//组合2：A1B2------>每次出现取值，就会得到新值，与迭代无关
//	lr_output_message(lr_eval_string("{lrpwd}"));


//	lr_output_message(lr_eval_string("{lrpwd}"));
//	lr_output_message(lr_eval_string("{lrpwd}"));
//	lr_output_message(lr_eval_string("{lrpwd}"));
//	lr_output_message(lr_eval_string("{lrpwd}"));


	//组合3----A1B3------选择值以后不再发生变化
//	lr_output_message(lr_eval_string("{lrpwd}"));
//	lr_output_message(lr_eval_string("{lrpwd}"));
// 
// 
// 组合4----A2B1----》只有发生迭代以后值才发生变化，每次迭代中的值不会随着输出而改变
//	lr_output_message(lr_eval_string("{lrpwd}"));
//	lr_output_message(lr_eval_string("{lrpwd}"));


//组合5----A2B2--->只要发生变化就会随机取值，与迭代次数无关
//	lr_output_message(lr_eval_string("{lrpwd}"));
//	lr_output_message(lr_eval_string("{lrpwd}"));
//组合6----A2B3---随之取值之后不再变化
		//lr_output_message(lr_eval_string("{lrpwd}"));
	//lr_output_message(lr_eval_string("{lrpwd}"));

//组合7----A3B1---每次迭代唯一取值与迭代有关
//	lr_output_message(lr_eval_string("{lrpwd}"));
	//lr_output_message(lr_eval_string("{lrpwd}"));

//组合8----A3B2----每次出现唯一取值
	//	lr_output_message(lr_eval_string("{lrpwd}"));
	//	lr_output_message(lr_eval_string("{lrpwd}"));

//组合9-A3B3---一旦选中不再发生变化
		lr_output_message(lr_eval_string("{lrpwd}"));
		lr_output_message(lr_eval_string("{lrpwd}"));

	return 0;
}
