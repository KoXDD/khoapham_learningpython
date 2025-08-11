person={
    'first_name':'Khoa',
    'last name':'Pham',
    'age':'15',
    'country':'Vietnam',
    'is_married':False,
    'skills':['English','Writing','Reading','Python','React'],
    'address': {
        'city':'cao bang',
        'post code':'21000'
    }
}

if "skills" in person:                                 #1
    print("skills duoc tim thay trong dictionary")
    skills = person['skills']
    skillogiua = skills[len(skills)//2]
    print('\n')
    print("skill o giua la",skillogiua)
else:
    print("skills khong duoc tim thay")
 

print('\n')
if "skills" in person:                                       #2
    if "python" in person['skills']:
        print('Skill python duoc tim thay trong cac skills cua person')
    else:
        print('Skill python khong duoc tim thay trong cac skills cua person')
else:
    print('Muc \'skill\' khong duoc tim thay')


print('\n')
if ['JavaScript','React'] == skills:                    #3
    print('Ban nay la front end developer')
elif {'Node','Python','MongoDB'}.issubset(skills): #dung issubset
    print('Ban nay la back end dev')
elif {'React','MongoDB','Node'}.issubset(skills):
    print('Ban nay la full stack dev')
else:
    print('Ban nay co danh hieu khong xac dinh')


if person['is_married'] == True and person['country'] == 'Finland':
    print('\n')
    print("Ban nay da ket hon va song tai Finland")
else:
    print()
