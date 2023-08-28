TODO: views zwiazane z logowaniem i rejestracja

TODO: przejscia miedzy profilem a edycja profilu a edycja konta (rozne rzeczy - dodac linki w profile view itd)

TODO: form views

TODO: rozwijalna js form na komentarz?

TODO: users list view

TODO: ogbsluga lajkow wszedzie

TODO: obsluga followow tak jak faljkow

TODO: stylizacja przyciskow like i submit search na gridzie

FIXME: aktualnie obsluga infinite scrolla z waypoints nie dodaje ?page=.. do linku w browser wiec redirect do tej strony tez tego nie zawiera i wraca na sama gore - trzeba by jakos moze zrealizowac lajkowanie w glownym view, ktore zawiera parametr page?

albo przesylac parametr page w form?

TODO: kwestia lajkowania - jak lajkujesz, to mozesz zmienic stan na backendzie, ale zeby zaktualizowalo sie na froncie trzeba odswiezyc strone, ale co z pozycja na stronie? aktualnie jest to realizowane poprzez paginacje, wiec powinno sie dac zrobic to tak by w redirect przekazywalo takie page jakie bylo

TODO: tag list view i przenoszenie do strony z postami przefiltrowanymi przez ten tag (wystarczy grid)

TODO: posty polubione jako po prostu grid z query ze polubione przez uzytkownika?

TODO: jak zrealizowac dodawanie nowych tagow z predefiniowanymi forms z crispy itd? bo select zalatwia a tworzenie? musialbym miec oddzielne form dla uzytkownika i gdzies je jakos umiescic

ale fajnie gdyby uzytkownik mogl tworzyc nowe w locie, idk: moze jakies dodatkowe pole recznie dopisane do form, ale wtedy ograniczaloby to do jednego, wiec moze wiele pol, ale wtedy tez fajnie gdyby byl jakis autocomplete by uzytkownik mogl wpisac tag i wybrac z istniejacych...

albo tylko wpisywanie i max 3 tagi, bo luj, niech uzytkownik mysli jakie tagi dac?
i wtedy sprawdzanie w form czy tak istnieje czy nie musialoby byc i jak nie to przypisanie

FIXME: poki co cover img w poscie a nie oddzielny model ,bo nie potrzebuje, fajne to jest gdy masz serializator i API z ktorego mozna ciagnac tylko obrazki itd

TODO: dodanie obslugi filtrow z opencv, tylko wtedy by trzeba jakis custom form z przyciskami izeby wyswietlalo od razu tego rezultaty na przeslanym obrazku?