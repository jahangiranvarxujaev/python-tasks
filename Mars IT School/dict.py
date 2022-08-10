"""
mother = {
    'name' : 'Nasiba',
    'age' : '35',
    'hobby' : 'housework'
}
father = {
    'name'  : 'Akbar',
    'age' : '38',
    'hobby' : 'bodybuilder'
}
son = {
    'name' : 'Jahongir',
    'age' : '15',
    'hobby' : 'python programming'
}
family = [mother, father, son]
for i in family:
    for a, b in i.items():
        print(a, ":", b)
    print('========')
"""

#English - Russia Dictionary

menu = {
    'burger' : '15$',
    'hot-dog' : '12$',
    'chiken-burger' : '18$',
    'gam-burger' : '19$',
    'small-peperoni-pizza' : '20$',
    'average-peperoni-pizza' : '30$',
    'large-peperoni-pizza' : '40$',
    'small-margarit-pizza' : '20$',
    'average-margarit-pizza' : '30$',
    'large-margarit-pizza' : '40$',
    'gold-cola' : '100$',
    'coca-cola' : '5$',
    'gold-sprite' : '99$',
    'sprite' : '4$'

}

s = input('Order smth from our menu! '
          '')
a = menu.get(f'{s}', "Sorry!, We don't have it")
print(a)

'''
#countries
contries = {
    "Rossiya" : "Moskva" ,
    "Velicobritaniya" : "London" ,
    "Germaniya" : "Berlin",
    "Ispaniya" : "Madrid",
    "Ukraina" : "Kiev",
    "Italiya" : "Rim",
    "Ruminiya" : "Buxarest" ,
    "Fransiya" : "Parij" ,
    "Belorus" : "Minsk" ,
    "Shveciya" : "Stokgolm" ,
    "Avstriya" : "Vena" ,
    "Polsha" : "Varshava" ,
    "Vengriya" : "Budopesht" ,
    "Serbiya" : "Belgrad" ,
    "Bolgariya" : "Sofiya" ,
    "Chexiya" : "Praga",
    "Albaniya" : "Tirana" ,
    "Doneciya" : "Doneck" ,
    "Niderlandiya" : "Amsterdam" ,
    "Xorvatiya" : "Zagreb" ,
    "Norvegiya" : "Oslo" ,
    "Greciya" : "Ofina" ,
    "Filyandiya" : " Xelsinki" ,
    "Daniya" : "Kopengagen" ,
    "Moldaviya" : "Kushinev" ,
    "Litviya" : "Riga" ,
    "Irlandiya" : "Dublin" ,
    "Litviya" : "Vilnus" ,
    "Portugaliya" : "Lissabon" ,
    "Severnaya Makedoniya" : "Skope" ,
    "Slovakiya" : "Bratislava" ,
    "Estoniya" : "Taliin" ,
    "Lugansk" : "Lugansk" ,
    "Bonsiya i Gersegovina" : "Saraevo" ,
    "Kolosovo" : "Prishtina" ,
    "Belgiya" : "Bryusel" ,
    "Chernogoriya" : "Podgorica" ,
    "Pridnestrovskaya Moldaviya" : "Tiraspol" ,
    "Shvecariya" : "Bern" ,
    "Luksimburg" : "Luksimburg" ,
    "Andorra" : "Andora-la-Velya",
    "Malta" : "Valletta" ,
    "Lixtenshteyn" : "Vaduc" ,
    "San-Marino" : "San-Marino" ,
    "OAE" :  "Abu-Dabi" ,
    "Iordaniya" : "Amman" ,
    "Tursiya" : "Ankara" ,
    "Turkmeniya" : "Ashxabat",
    "Iraq" : "Bagdad",
    "Azerbaydjan" : "Baku",
    "Tailand" : "Bangkok" ,
    "Bruney" : "Bandar-Seri-Begavan",
    "Livan" : " Beyrut" ,
    "Kirgiziya" : "Bishkek",
    "Laos" : "Vetnam" ,
    "Bangladesh" : "Dakka",
    "Siriya" : "Damask",
    "Indiya" : "Deli",
    "Indoneziya" : "Djakarta",
    "Vostochniy Timor" : "Dili",
    "Katar" : "Doxa",
    "Tadjikistan" : "Dushanbe" ,
    "Armeniya" : "Erevan" ,
    "Izrail" : "Ierusalim",
    "Pakistan" : "Islamabad",
    "Afganistan" : "Kabul",
    "Nepal" : "Katmandu",
    "Malayziya" : "Kulala-Lumpur",
    "Maldivi" : "Male",
    "Baxreyn" : "Manama",
    "Filipini" : "Manila",
    "Oman" : "Maskat",
    "Myanma" : "Neypido",
    "Kipr" : "Nikosiya",
    "Kazahistan" : "Nur-Sulton",
    "Kitay" : "Pekin",
    "Kambodja" : "Pnompen" ,
    "KNDR" : "Pxenyan",
    "Yemen" : "Sana" ,
    "Koreya" : "Seul",
    "Singapur" : "Singapur",
    "Uzbekistan" : "Tashkent" ,
    "Gruziya" : "Tbilisi",
    "Yaponiya" : "Tokiyo" ,
    "Butan" : "Tximpxy",
    "Mongoliya" : "Ulan-Bator" ,
    "Vetnam" : "Xanoy",
    "Wri-Lanka" : "Wri-Djayardenepura-Katte",
    "Kuveyt" : "El-Kuveyt",
    "Saudovskaya Araviya" : "Er-Riyad",
    "Azad Kashmir" :"Muzaffarabad",
    "Severniy Kapir" : "Nikosiya",
    "Palestina" : "Ramalla" ,
    "NKP" : "Stepanakert",
    "Kitayskaya Respublika" : "Taybey",
    "Yujnaya Osetiya" : "Cxinval",
    "Abxaziya" : "Suxum",
    "Nigeriya" : "Abudja",
    "Efiopiya" : "Addis-Abeba",
    "Gina" : "Akkra",
    "Aljir" : "Aljir",
    "Madagaskar" : "Antananativu",
    "Eritreya" : "Asmera",
    "Mali" : "Bamako",
    "CAR" : "Bangi",
    "Gambiya" : "Banjul",
    "Gvineya-Bisay" : "Bisay",
}
c = input("Shaharni tanglang ")
ams = contries.get(f'{c}',"sorry we dont have it!")
print(ams)
'''