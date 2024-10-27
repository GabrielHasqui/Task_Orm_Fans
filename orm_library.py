from library.models import Libro, Autor, AutorCapitulo, Editorial, LibroCronica

# sentencias orm 
# Incercion basica de datos en la tabla Autor
Autor.objects.create(nombre='Autor desde el orm')

# Incercion basica de datos en la tabla Autor con el metodo save
autor = Autor.objects.create(nombre='Gabril Garcia Marquez')
autor.save()

# Incercion basica de datos en la tabla Autor con el metodo bulk_create

autores = [
    Autor(nombre='Autor 1M'),
    Autor(nombre='Autor 2M'),
    Autor(nombre='Autor 3M')
]

Autor.objects.bulk_create(autores)

# Consulta basica de datos en la tabla Autor con el metodo all
autores = Autor.objects.all()
for autor in autores:
    print(autor.nombre)

# Incercion basica de datos en la tabla Editorial con el metodo create
Editorial.objects.create(nombre='Editorial 1')

#obtener la editorial creada con el metodo get
editorial = Editorial.objects.get(nombre='Editorial 1')

# Incercion basica de datos en la tabla Libro
libro = Libro.objects.create(
    isbn='1234567890123',
    titulo='Cien años de soledad',
    paginas=100,
    fecha_publicacion='2021-01-01',
    imagen='http://imagen.com',
    desc_corta='Descripcion corta',
    estatus='A',
    categoria='Categoria 1',
    editorial=editorial
)

# Incercion basica de datos en la tabla Libro con el metodo bulk_create

libros = [
    Libro(
        isbn='1644567890123',
        titulo='El amor en los tiempos del colera',
        paginas=100,
        fecha_publicacion='2021-01-01',
        imagen='http://imagen.com',
        desc_corta='Descripcion corta',
        estatus='A',
        categoria='Categoria 1',
        editorial=editorial
    ),
    Libro(
        isbn='1634567890125',
        titulo='El alquimista',
        paginas=100,
        fecha_publicacion='2021-01-01',
        imagen='http://imagen.com',
        desc_corta='Descripcion corta',
        estatus='A',
        categoria='Categoria 1',
        editorial=editorial
    )
]

Libro.objects.bulk_create(libros)

# Obtener un libro con el metodo get
libro = Libro.objects.get(isbn='1234567890123')
print(libro)

#Obtener el primer libro con el metodo first
libro = Libro.objects.first()
print(libro)

#Obtener el ultimo libro con el metodo last
libro = Libro.objects.last()
print(libro)

# Obtener los primeros 2 libros 
libros = Libro.objects.all()[:2]    
print(libros)


# Consultas por coincidencia
# Obtener los libros con el isbn que empieza con 16 con el metodo startswith
libros = Libro.objects.filter(isbn__startswith='16')
print(libros)

# Consultas mayor que con el metodo gt(>)
# Obtener los libros con mas de 200 paginas con el metodo gt
libros = Libro.objects.filter(paginas__gt=200)
print(libros)

# Consultas con not in con el metodo exclude 
# consultar los libros que tenga mas de 200 paginas y que no su isbn no sea 1234567890123
libros = Libro.objects.filter(paginas__gt=200).exclude(isbn='1234567890123')
print(libros)

# Consultas mayor o igual que con el metodo gte(>=)
# Consultar los libros que tengan 200 o mas paginas
libros = Libro.objects.filter(paginas__gte=200).values('titulo','paginas')
print(libros)

# Consulta menor que con el metodo lt(<)
# Consultar los libros que tengan menos de 200 paginas
libros = Libro.objects.filter(paginas__lt=200).values('titulo','paginas')
print(libros)

# Consulta menor o igual que con el metodo lte(<=)
# Consultar los libros que tengan 200 o menos paginas
libros = Libro.objects.filter(paginas__lte=200).values('titulo','paginas')
print(libros)

# Consultas con count
# Contar los libros que tengan menos de 200 paginas
libros = Libro.objects.filter(paginas__lt=200).count()
print(libros)

# Consulta con or forma larga
# Consultar los libros con 200 o 300 paginas
libros1 = Libro.objects.filter(paginas=200)
libros2 = Libro.objects.filter(paginas=300)
consulta = (libros1 | libros2).values('titulo','paginas')
print(consulta)


