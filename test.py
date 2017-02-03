from semantic.numbers import NumberService
service = NumberService()
f = open('/home/himanshu/Desktop/python semantics/dict4.txt','r+')
#for line in f:
#	if '206' in line:
#		print("k");
for line in f:
	if str(service.parse("Two hundred and six")) in line:
		print("found");
	
