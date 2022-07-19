#Słowniki, piękne słowniki
#Tworzymy mapowanie nazwy stanu na skróty
states = {
  'Oregon': 'OR',
  'Floryda': 'FL',
  'Kalifornia': 'KA',
  'Nowy Jork': 'NJ',
  'Michigan': 'MI'
}

#tworzymy podstawowy zestaw stanów i znajdujących się miast

cities = {
  'KA': 'San Francisco',
  'MI': 'Detroit',
  'FL': 'Jacksonville'
}

#dodajemy kilka miast
cities['NJ'] = 'Nowy Jork'
cities['OR'] = 'Portland'

#drukujemy kilka miast
print('-'*10)
print("Stan NJ ma: ", cities['NJ'])
print("Stan OR ma: ", cities['OR'])

#drukujemy kilka stanów
print('-'*10)
print("Skrót dla Michgan to: ", states['Michigan'])
print("Skrót dla Floryda to: ", states['Floryda'])

#używamy najpierw słownika state, apotem cities
print('-'*10)
print("Michigan ma: ", cities[states['Michigan']])
print("Floryda ma: ", cities[states['Floryda']])

#drukujemy skrót każdego stanu
print('-'*10)
for state, abbrev in list(states.items()):
  print(f"{state} ma skrót {abbrev}")

#drukujemy każde miasto w stanie
print('-'*10)
for abbrev, city in list(cities.items()):
  print(f"{abbrev} ma miasto w stanie {city}")

#Teraz obie te rzeczy na raz
print('-'*10)
for state, abbrev in  list(states.items()):
  print(f"Stan {state} ma skrót {abbrev}")
  print(f"oraz miasto {cities[abbrev]}")

print('-'*10)
#bezpiecznie pobieramy skrót według nazwy stanu, który może nei istnieć
state = states.get('Texas')

#Pobieramy miasto za pomocą domyślnej wartości
city = cities.get('TX', 'Nie istnieje')
print(f"Miasto dla stanu 'TX' to: {city}")

#Directory and dictionary Poland

Wojewodztwa = {
  'Pomorskie': 'POM',
  'Mazowieckie': 'MAZO',
  'Podlaskie': 'POD',
  'Mazurskie': 'MAZU',
  'Lodzkie': 'LOD'
}

Miasta = {
  'POM': 'Gdańsk',
  'POM': 'Gdynia',
  'POM': 'Sopot',
  'LOD': 'Lodz',
  'ZACHPOM': 'Szczecin'
}
print('-'*10)
for state, abbrev in list(Wojewodztwa.items()):
  print(f"Wojewodztwo {state} ma skrot {abbrev} ")
print("Wojewodztwo Podlaskie ma skrót ", Wojewodztwa['Podlaskie'])

miejscowosc = Miasta.get('POM', 'Nie istnieje')
print(miejscowosc)