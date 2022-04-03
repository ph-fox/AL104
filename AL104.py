dds = {'a':'<->','b':'<|>','c':'<#>','d':'<h>','e':'<!>','f':'<X>','g':'<+>','h':'<&>','i':'<_>','j':'<@>','k':'<.>','l':'<*>','m':'<z>','n':'<^>','o':'<%>','p':'<~>','q':'<=>','r':'</>','s':'<?>','t':'<[>','u':'<]>','v':'<{>','w':'<}>','x':'<(>','y':'<)>','z':'<$>',' ':'###','1':'>5<','2':'>0<','3':'>7<','4':'>9<','5':'>6<','6':'>8<','7':'>3<','8':'>4<','9':'>1<','0':'>2<'}
ddz = {'<->':'a','<|>':'b','<#>':'c','<h>':'d','<!>':'e','<X>':'f','<+>':'g','<&>':'h','<_>':'i','<@>':'j','<.>':'k','<*>':'l','<z>':'m','<^>':'n','<%>':'o','<~>':'p','<=>':'q','</>':'r','<?>':'s','<[>':'t','<]>':'u','<{>':'v','<}>':'w','<(>':'x','<)>':'y','<$>':'z','###':' ','>5<':'1','>0<':'2','>7<':'3','>9<':'4','>6<':'5','>8<':'6','>3<':'7','>4<':'8','>1<':'9','>2<':'0'}

def encode(ui):
	msg_all = ''
	for charz in ui:
		try:
			if charz == charz.upper():
				x = dds.get(charz.lower())
				msg_all+=x.upper()
			else:
				x = dds.get(charz)
				msg_all+=x
		except:
			msg_all+=''
	return msg_all


def decode(x):
	msg_all=''
	code=[]
	s_code=''
	count=3
	x+=' '
	for charz in x:
		if count<1:
			count=3
			code.append(s_code)
			s_code=''
		count-=1
		s_code+=charz

	for sym in code:
		decoded = ddz.get(sym)
		msg_all+=str(decoded)

	return msg_all


if __name__ == "__main__":
	while True:
		print("""
[E] == Encode
[D] == Decode""")
		ui = input("==================\nSelc-> ").lower()
		if ui == 'e':
			ui = input("Enter msg to encode: ")
			encode(ui)
			print('\nResult: '+encode(ui)+'')
			print()
		elif ui == 'd':
			ui = input("Enter msg to decode: ")
			print('\nResult: '+decode(ui)+'')
			print()
