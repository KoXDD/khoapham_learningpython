#Cach 1
names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']
nordic = names[:5]
es = names[5]
ru = names[6]
print("Cac quoc gia o vung Nordic:", nordic)
print("Cac quoc gia o vung es:",es)
print("Cac quoc gia o vung ru:",ru)
del nordic, es, ru

#Cach 2
*nordic, es, ru = names        
print("Cac quoc gia o vung Nordic:", nordic)
print("Cac quoc gia o vung es:",es)
print("Cac quoc gia o vung ru:",ru)