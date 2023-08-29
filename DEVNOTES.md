# Zwiazane z plikami
## Przekazywanie plikow w form, np. obrazkow

Kluczowe jest w htmlu w <form> dodac enctype="multipart/form-data" - to oczywiste

ale nastepnie, w view obslugujacym form poniewaz multipart, odbierajac te wartosci z request.post, nalezy dodac:

    form = SignUpForm(request.POST, request.FILES)

i dopiero potem mozna robic
    
    if form.is_valid():

i odbierac np z

    img = request.POST.get('img')


## Defaultowy obrazek, gdyby jakis nie zostal przeslany:

W modelu dodac mozna pole default="path/to/default.img"