Action4()
{

	lr_think_time(12);

	web_submit_data("reservations.pl_3", 
		"Action=http://192.168.103.143:1080/webtours/reservations.pl", 
		"Method=POST", 
		"RecContentType=text/html", 
		"Referer=http://192.168.103.143:1080/webtours/reservations.pl", 
		"Snapshot=t6.inf", 
		"Mode=HTML", 
		ITEMDATA, 
		"Name=firstName", "Value=Joseph", ENDITEM, 
		"Name=lastName", "Value=Marshall", ENDITEM, 
		"Name=address1", "Value=234 Willow Drive", ENDITEM, 
		"Name=address2", "Value=San Jose/CA/94085", ENDITEM, 
		"Name=pass1", "Value=Joseph Marshall", ENDITEM, 
		"Name=creditCard", "Value=12234567890", ENDITEM, 
		"Name=expDate", "Value=", ENDITEM, 
		"Name=oldCCOption", "Value=", ENDITEM, 
		"Name=numPassengers", "Value=1", ENDITEM, 
		"Name=seatType", "Value=Coach", ENDITEM, 
		"Name=seatPref", "Value=None", ENDITEM, 
		"Name=outboundFlight", "Value=021;301;01/13/2018", ENDITEM, 
		"Name=advanceDiscount", "Value=0", ENDITEM, 
		"Name=returnFlight", "Value=", ENDITEM, 
		"Name=JSFormSubmit", "Value=off", ENDITEM, 
		"Name=.cgifields", "Value=saveCC", ENDITEM, 
		"Name=buyFlights.x", "Value=24", ENDITEM, 
		"Name=buyFlights.y", "Value=4", ENDITEM, 
		LAST);

	return 0;
}
