Action3()
{

	lr_think_time(8);

	web_submit_data("reservations.pl_2", 
		"Action=http://192.168.103.143:1080/webtours/reservations.pl", 
		"Method=POST", 
		"RecContentType=text/html", 
		"Referer=http://192.168.103.143:1080/webtours/reservations.pl", 
		"Snapshot=t5.inf", 
		"Mode=HTML", 
		ITEMDATA, 
		"Name=outboundFlight", "Value=021;301;01/13/2018", ENDITEM, 
		"Name=numPassengers", "Value=1", ENDITEM, 
		"Name=advanceDiscount", "Value=0", ENDITEM, 
		"Name=seatType", "Value=Coach", ENDITEM, 
		"Name=seatPref", "Value=None", ENDITEM, 
		"Name=reserveFlights.x", "Value=44", ENDITEM, 
		"Name=reserveFlights.y", "Value=6", ENDITEM, 
		LAST);

	return 0;
}
