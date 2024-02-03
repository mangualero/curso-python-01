#biblioteca

# seccion_fantasia = [['el señor de los anillos', 2000], ['alicia en el paía de las maravillas', 2000]]
# seccion_ciencias = [['python 1', 2001], ['fisicca', 2005]]
# seccion_historia = [['segunda guerra mundial', 1990], ['Simon bolivar', 2015]]

# biblioteca = [seccion_fantasia, seccion_ciencias, seccion_historia]

#Dictionarios
# biblioteca = {
#     "seccion_fantasia": [
#         {
#             "nombre": "El señor de los anillo",
#             "año_publicacion": 2000
#         },
#         {
#             "nombre": "Alicia en el pais de las maravillas",
#             "año_publicacion": 2000
#         }
#     ],

#     "seccion_ciencias": [
#         {
#             "nombre": "Python 1",
#             "año_publicacion": 2001
#         },
#         {
#             "nombre": "Fisica",
#             "año_publicacion": 2001
#         }
#     ],

#     "seccion_historia": [
#         {
#             "nombre": "Simon Bolivar",
#             "año_publicacion": 2015
#         },
#         {
#             "nombre": "Segunda guerra mundial",
#             "año_publicacion": 1990
#         }
#     ]
# }

# biblioteca = [
#     {
#         "nombre": "El señor de los anillo",
#         "año_publicacion": 2000,
#         "autor": "JRR. TOLKIEN",
#         "categoria": "fantasia"
#     },
#     {
#         "nombre": "Alicia en el pais de las maravillas",
#         "año_publicacion": 2000,
#         "autor": "Mariana",
#         "categoria": "fantasia"
#     },
#     {
#         "nombre": "Python 1",
#         "año_publicacion": 2001,
#         "autor": "Mariana",
#         "categoria": "ciencia"
#     },
#     {
#         "nombre": "Fisica",
#         "año_publicacion": 2001,
#         "autor": "Mariana",
#         "categoria": "ciencia"
#     },
#     {
#         "nombre": "Simon Bolivar",
#         "año_publicacion": 2015,
#         "autor": "Mariana",
#         "categoria": "historia"
#     },
#     {
#         "nombre": "Segunda guerra mundial",
#         "año_publicacion": 1990,
#         "autor": "Mariana",
#         "categoria": "historia"
#     }
# ]


# for libro in biblioteca:
#     if libro["categoria"] == "historia":
#         print(f"{libro["nombre"]} [{libro["categoria"]}]")


# seccion_ciencias = {
#      "libro_1":{ 
#          "nombre": "El señor de los anillos",
#          "año":2000
#     },
#     "libro_2":{
#         "nombre": "alicia en el paais de laas maraavillas",
#         "año":2005
#     }    
# }


# for seccion in seccion_ciencias:
#         print(seccion_ciencias[seccion]["nombre"])

books =   [
  {
    "author": 'Chinua Achebe',
    "country": 'Nigeria',
    "language": 'English',
    "title": 'Things Fall Apart',
    "year": 1958,
    "category": 'Poetry',
  },
  {
    "author": 'Hans Christian Andersen',
    "country": 'Denmark',
    "language": 'Danish',
    "title": 'Fairy tales',
    "year": 1836,
    "category": 'Science Fiction',
  },
  {
    "author": 'Dante Alighieri',
    "country": 'Italy',
    "language": 'Italian',
    "title": 'The Divine Comedy',
    "year": 1315,
    "category": 'Fantasy',
  },
  {
    "author": 'Unknown',
    "country": 'Sumer and Akkadian Empire',
    "language": 'Akkadian',
    "title": 'The Epic Of Gilgamesh',
    "year": -1700,
    "category": 'Historical',
  },
  {
    "author": 'Unknown',
    "country": 'Achaemenid Empire',
    "language": 'Hebrew',
    "title": 'The Book Of Job',
    "year": -600,
    "category": 'Science Fiction',
  },
  {
    "author": 'Unknown',
    "country": 'India/Iran/Iraq/Egypt/Tajikistan',
    "language": 'Arabic',
    "title": 'One Thousand and One Nights',
    "year": 1200,
    "category": 'Science Fiction',
  },
  {
    "author": 'Unknown',
    "country": 'Iceland',
    "language": 'Old Norse',
    "title": "Njál's Saga",
    "year": 1350,
    "category": 'Fiction',
  },
  {
    "author": 'Jane Austen',
    "country": 'United Kingdom',
    "language": 'English',
    "title": 'Pride and Prejudice',
    "year": 1813,
    "category": 'Thriller',
  },
  {
    "author": 'Honoré de Balzac',
    "country": 'France',
    "language": 'French',
    "title": 'Le Père Goriot',
    "year": 1835,
    "category": 'Historical',
  },
  {
    "author": 'Samuel Beckett',
    "country": 'Republic of Ireland',
    "language": 'French, English',
    "title": 'Molloy, Malone Dies, The Unnamable, the trilogy',
    "year": 1952,
    "category": 'Non-Fiction',
  },
  {
    "author": 'Giovanni Boccaccio',
    "country": 'Italy',
    "language": 'Italian',
    "title": 'The Decameron',
    "year": 1351,
    "category": 'Poetry',
  },
  {
    "author": 'Jorge Luis Borges',
    "country": 'Argentina',
    "language": 'Spanish',
    "title": 'Ficciones',
    "year": 1965,
    "category": 'Fiction',
  },
  {
    "author": 'Emily Brontë',
    "country": 'United Kingdom',
    "language": 'English',
    "title": 'Wuthering Heights',
    "year": 1847,
    "category": 'Drama',
  },
  {
    "author": 'Albert Camus',
    "country": 'Algeria, French Empire',
    "language": 'French',
    "title": 'The Stranger',
    "year": 1942,
    "category": 'Mystery',
  },
  {
    "author": 'Paul Celan',
    "country": 'Romania, France',
    "language": 'German',
    "title": 'Poems',
    "year": 1952,
    "category": 'Non-Fiction',
  },
  {
    "author": 'Louis-Ferdinand Céline',
    "country": 'France',
    "language": 'French',
    "title": 'Journey to the End of the Night',
    "year": 1932,
    "category": 'Fantasy',
  },
  {
    "author": 'Miguel de Cervantes',
    "country": 'Spain',
    "language": 'Spanish',
    "title": 'Don Quijote De La Mancha',
    "year": 1610,
    "category": 'Drama',
  },
  {
    "author": 'Geoffrey Chaucer',
    "country": 'England',
    "language": 'English',
    "title": 'The Canterbury Tales',
    "year": 1450,
    "category": 'Non-Fiction',
  },
  {
    "author": 'Anton Chekhov',
    "country": 'Russia',
    "language": 'Russian',
    "title": 'Stories',
    "year": 1886,
    "category": 'Fantasy',
  },
  {
    "author": 'Joseph Conrad',
    "country": 'United Kingdom',
    "language": 'English',
    "title": 'Nostromo',
    "year": 1904,
    "category": 'Non-Fiction',
  },
  {
    "author": 'Charles Dickens',
    "country": 'United Kingdom',
    "language": 'English',
    "title": 'Great Expectations',
    "year": 1861,
    "category": 'Mystery',
  },
  {
    "author": 'Denis Diderot',
    "country": 'France',
    "language": 'French',
    "title": 'Jacques the Fatalist',
    "year": 1796,
    "category": 'Fiction',
  },
  {
    "author": 'Alfred Döblin',
    "country": 'Germany',
    "language": 'German',
    "title": 'Berlin Alexanderplatz',
    "year": 1929,
    "category": 'Thriller',
  },
  {
    "author": 'Fyodor Dostoevsky',
    "country": 'Russia',
    "language": 'Russian',
    "title": 'Crime and Punishment',
    "year": 1866,
    "category": 'Fiction',
  },
  {
    "author": 'Fyodor Dostoevsky',
    "country": 'Russia',
    "language": 'Russian',
    "title": 'The Idiot',
    "year": 1869,
    "category": 'Non-Fiction',
  },
  {
    "author": 'Fyodor Dostoevsky',
    "country": 'Russia',
    "language": 'Russian',
    "title": 'The Possessed',
    "year": 1872,
    "category": 'Mystery',
  },
  {
    "author": 'Fyodor Dostoevsky',
    "country": 'Russia',
    "language": 'Russian',
    "title": 'The Brothers Karamazov',
    "year": 1880,
    "category": 'Drama',
  },
  {
    "author": 'George Eliot',
    "country": 'United Kingdom',
    "language": 'English',
    "title": 'Middlemarch',
    "year": 1871,
    "category": 'Non-Fiction',
  },
  {
    "author": 'Ralph Ellison',
    "country": 'United States',
    "language": 'English',
    "title": 'Invisible Man',
    "year": 1952,
    "category": 'Romance',
  },
  {
    "author": 'Euripides',
    "country": 'Greece',
    "language": 'Greek',
    "title": 'Medea',
    "year": -431,
    "category": 'Drama',
  },
  {
    "author": 'William Faulkner',
    "country": 'United States',
    "language": 'English',
    "title": 'Absalom, Absalom!',
    "year": 1936,
    "category": 'Mystery',
  },
  {
    "author": 'William Faulkner',
    "country": 'United States',
    "language": 'English',
    "title": 'The Sound and the Fury',
    "year": 1929,
    "category": 'Fiction',
  },
  {
    "author": 'Gustave Flaubert',
    "country": 'France',
    "language": 'French',
    "title": 'Madame Bovary',
    "year": 1857,
    "category": 'Fantasy',
  },
  {
    "author": 'Gustave Flaubert',
    "country": 'France',
    "language": 'French',
    "title": 'Sentimental Education',
    "year": 1869,
    "category": 'Poetry',
  },
  {
    "author": 'Federico García Lorca',
    "country": 'Spain',
    "language": 'Spanish',
    "title": 'Gypsy Ballads',
    "year": 1928,
    "category": 'Mystery',
  },
  {
    "author": 'Gabriel García Márquez',
    "country": 'Colombia',
    "language": 'Spanish',
    "title": 'One Hundred Years of Solitude',
    "year": 1967,
    "category": 'Fantasy',
  },
  {
    "author": 'Gabriel García Márquez',
    "country": 'Colombia',
    "language": 'Spanish',
    "title": 'Love in the Time of Cholera',
    "year": 1985,
    "category": 'Mystery',
  },
  {
    "author": 'Johann Wolfgang von Goethe',
    "country": 'Saxe-Weimar',
    "language": 'German',
    "title": 'Faust',
    "year": 1832,
    "category": 'Fantasy',
  },
  {
    "author": 'Nikolai Gogol',
    "country": 'Russia',
    "language": 'Russian',
    "title": 'Dead Souls',
    "year": 1842,
    "category": 'Fiction',
  },
  {
    "author": 'Günter Grass',
    "country": 'Germany',
    "language": 'German',
    "title": 'The Tin Drum',
    "year": 1959,
    "category": 'Fantasy',
  },
  {
    "author": 'João Guimarães Rosa',
    "country": 'Brazil',
    "language": 'Portuguese',
    "title": 'The Devil to Pay in the Backlands',
    "year": 1956,
    "category": 'Fiction',
  },
  {
    "author": 'Knut Hamsun',
    "country": 'Norway',
    "language": 'Norwegian',
    "title": 'Hunger',
    "year": 1890,
    "category": 'Thriller',
  },
  {
    "author": 'Ernest Hemingway',
    "country": 'United States',
    "language": 'English',
    "title": 'The Old Man and the Sea',
    "year": 1952,
    "category": 'Drama',
  },
  {
    "author": 'Homer',
    "country": 'Greece',
    "language": 'Greek',
    "title": 'Iliad',
    "year": -735,
    "category": 'Historical',
  },
  {
    "author": 'Homer',
    "country": 'Greece',
    "language": 'Greek',
    "title": 'Odyssey',
    "year": -800,
    "category": 'Thriller',
  },
  {
    "author": 'Henrik Ibsen',
    "country": 'Norway',
    "language": 'Norwegian',
    "title": "A Doll's House",
    "year": 1879,
    "category": 'Mystery',
  },
  {
    "author": 'James Joyce',
    "country": 'Irish Free State',
    "language": 'English',
    "title": 'Ulysses',
    "year": 1922,
    "category": 'Non-Fiction',
  },
  {
    "author": 'Franz Kafka',
    "country": 'Czechoslovakia',
    "language": 'German',
    "title": 'Stories',
    "year": 1924,
    "category": 'Fantasy',
  },
  {
    "author": 'Franz Kafka',
    "country": 'Czechoslovakia',
    "language": 'German',
    "title": 'The Trial',
    "year": 1925,
    "category": 'Fantasy',
  },
  {
    "author": 'Franz Kafka',
    "country": 'Czechoslovakia',
    "language": 'German',
    "title": 'The Castle',
    "year": 1926,
    "category": 'Poetry',
  },
  {
    "author": 'Kālidāsa',
    "country": 'India',
    "language": 'Sanskrit',
    "title": 'The recognition of Shakuntala',
    "year": 150,
    "category": 'Fantasy',
  },
  {
    "author": 'Yasunari Kawabata',
    "country": 'Japan',
    "language": 'Japanese',
    "title": 'The Sound of the Mountain',
    "year": 1954,
    "category": 'Science Fiction',
  },
  {
    "author": 'Nikos Kazantzakis',
    "country": 'Greece',
    "language": 'Greek',
    "title": 'Zorba the Greek',
    "year": 1946,
    "category": 'Mystery',
  },
  {
    "author": 'D. H. Lawrence',
    "country": 'United Kingdom',
    "language": 'English',
    "title": 'Sons and Lovers',
    "year": 1913,
    "category": 'Mystery',
  },
  {
    "author": 'Halldór Laxness',
    "country": 'Iceland',
    "language": 'Icelandic',
    "title": 'Independent People',
    "year": 1934,
    "category": 'Mystery',
  },
  {
    "author": 'Giacomo Leopardi',
    "country": 'Italy',
    "language": 'Italian',
    "title": 'Poems',
    "year": 1818,
    "category": 'Thriller',
  },
  {
    "author": 'Doris Lessing',
    "country": 'United Kingdom',
    "language": 'English',
    "title": 'The Golden Notebook',
    "year": 1962,
    "category": 'Poetry',
  },
  {
    "author": 'Astrid Lindgren',
    "country": 'Sweden',
    "language": 'Swedish',
    "title": 'Pippi Longstocking',
    "year": 1945,
    "category": 'Romance',
  },
  {
    "author": 'Lu Xun',
    "country": 'China',
    "language": 'Chinese',
    "title": 'Diary of a Madman',
    "year": 1918,
    "category": 'Thriller',
  },
  {
    "author": 'Naguib Mahfouz',
    "country": 'Egypt',
    "language": 'Arabic',
    "title": 'Children of Gebelawi',
    "year": 1959,
    "category": 'Non-Fiction',
  },
  {
    "author": 'Thomas Mann',
    "country": 'Germany',
    "language": 'German',
    "title": 'Buddenbrooks',
    "year": 1901,
    "category": 'Fiction',
  },
  {
    "author": 'Thomas Mann',
    "country": 'Germany',
    "language": 'German',
    "title": 'The Magic Mountain',
    "year": 1924,
    "category": 'Thriller',
  },
  {
    "author": 'Herman Melville',
    "country": 'United States',
    "language": 'English',
    "title": 'Moby Dick',
    "year": 1851,
    "category": 'Drama',
  },
  {
    "author": 'Michel de Montaigne',
    "country": 'France',
    "language": 'French',
    "title": 'Essays',
    "year": 1595,
    "category": 'Romance',
  },
  {
    "author": 'Elsa Morante',
    "country": 'Italy',
    "language": 'Italian',
    "title": 'History',
    "year": 1974,
    "category": 'Historical',
  },
  {
    "author": 'Toni Morrison',
    "country": 'United States',
    "language": 'English',
    "title": 'Beloved',
    "year": 1987,
    "category": 'Drama',
  },
  {
    "author": 'Murasaki Shikibu',
    "country": 'Japan',
    "language": 'Japanese',
    "title": 'The Tale of Genji',
    "year": 1006,
    "category": 'Thriller',
  },
  {
    "author": 'Robert Musil',
    "country": 'Austria',
    "language": 'German',
    "title": 'The Man Without Qualities',
    "year": 1931,
    "category": 'Mystery',
  },
  {
    "author": 'Vladimir Nabokov',
    "country": 'Russia/United States',
    "language": 'English',
    "title": 'Lolita',
    "year": 1955,
    "category": 'Fantasy',
  },
  {
    "author": 'George Orwell',
    "country": 'United Kingdom',
    "language": 'English',
    "title": 'Nineteen Eighty-Four',
    "year": 1949,
    "category": 'Fiction',
  },
  {
    "author": 'Ovid',
    "country": 'Roman Empire',
    "language": 'Classical Latin',
    "title": 'Metamorphoses',
    "year": 100,
    "category": 'Thriller',
  },
  {
    "author": 'Fernando Pessoa',
    "country": 'Portugal',
    "language": 'Portuguese',
    "title": 'The Book of Disquiet',
    "year": 1928,
    "category": 'Non-Fiction',
  },
  {
    "author": 'Edgar Allan Poe',
    "country": 'United States',
    "language": 'English',
    "title": 'Tales',
    "year": 1950,
    "category": 'Fantasy',
  },
  {
    "author": 'Marcel Proust',
    "country": 'France',
    "language": 'French',
    "title": 'In Search of Lost Time',
    "year": 1920,
    "category": 'Science Fiction',
  },
  {
    "author": 'François Rabelais',
    "country": 'France',
    "language": 'French',
    "title": 'Gargantua and Pantagruel',
    "year": 1533,
    "category": 'Fantasy',
  },
  {
    "author": 'Juan Rulfo',
    "country": 'Mexico',
    "language": 'Spanish',
    "title": 'Pedro Páramo',
    "year": 1955,
    "category": 'Poetry',
  },
  {
    "author": 'Rumi',
    "country": 'Sultanate of Rum',
    "language": 'Persian',
    "title": 'The Masnavi',
    "year": 1236,
    "category": 'Romance',
  },
  {
    "author": 'Salman Rushdie',
    "country": 'United Kingdom, India',
    "language": 'English',
    "title": "Midnight's Children",
    "year": 1981,
    "category": 'Fiction',
  },
  {
    "author": 'Saadi',
    "country": 'Persia, Persian Empire',
    "language": 'Persian',
    "title": 'Bostan',
    "year": 1257,
    "category": 'Drama',
  },
  {
    "author": 'Tayeb Salih',
    "country": 'Sudan',
    "language": 'Arabic',
    "title": 'Season of Migration to the North',
    "year": 1966,
    "category": 'Mystery',
  },
  {
    "author": 'José Saramago',
    "country": 'Portugal',
    "language": 'Portuguese',
    "title": 'Blindness',
    "year": 1995,
    "category": 'Historical',
  },
  {
    "author": 'William Shakespeare',
    "country": 'England',
    "language": 'English',
    "title": 'Hamlet',
    "year": 1603,
    "category": 'Fiction',
  },
  {
    "author": 'William Shakespeare',
    "country": 'England',
    "language": 'English',
    "title": 'King Lear',
    "year": 1608,
    "category": 'Historical',
  },
  {
    "author": 'William Shakespeare',
    "country": 'England',
    "language": 'English',
    "title": 'Othello',
    "year": 1609,
    "category": 'Historical',
  },
  {
    "author": 'Sophocles',
    "country": 'Greece',
    "language": 'Greek',
    "title": 'Oedipus the King',
    "year": -430,
    "category": 'Non-Fiction',
  },
  {
    "author": 'Stendhal',
    "country": 'France',
    "language": 'French',
    "title": 'The Red and the Black',
    "year": 1830,
    "category": 'Thriller',
  },
  {
    "author": 'Laurence Sterne',
    "country": 'England',
    "language": 'English',
    "title": 'The Life And Opinions of Tristram Shandy',
    "year": 1760,
    "category": 'Romance',
  },
  {
    "author": 'Italo Svevo',
    "country": 'Italy',
    "language": 'Italian',
    "title": 'Confessions of Zeno',
    "year": 1923,
    "category": 'Non-Fiction',
  },
  {
    "author": 'Jonathan Swift',
    "country": 'Ireland',
    "language": 'English',
    "title": "Gulliver's Travels",
    "year": 1726,
    "category": 'Non-Fiction',
  },
  {
    "author": 'Leo Tolstoy',
    "country": 'Russia',
    "language": 'Russian',
    "title": 'War and Peace',
    "year": 1867,
    "category": 'Mystery',
  },
  {
    "author": 'Leo Tolstoy',
    "country": 'Russia',
    "language": 'Russian',
    "title": 'Anna Karenina',
    "year": 1877,
    "category": 'Fantasy',
  },
  {
    "author": 'Leo Tolstoy',
    "country": 'Russia',
    "language": 'Russian',
    "title": 'The Death of Ivan Ilyich',
    "year": 1886,
    "category": 'Historical',
  },
  {
    "author": 'Mark Twain',
    "country": 'United States',
    "language": 'English',
    "title": 'The Adventures of Huckleberry Finn',
    "year": 1884,
    "category": 'Drama',
  },
  {
    "author": 'Valmiki',
    "country": 'India',
    "language": 'Sanskrit',
    "title": 'Ramayana',
    "year": -450,
    "category": 'Fiction',
  },
  {
    "author": 'Virgil',
    "country": 'Roman Empire',
    "language": 'Classical Latin',
    "title": 'The Aeneid',
    "year": -23,
    "category": 'Romance',
  },
  {
    "author": 'Vyasa',
    "country": 'India',
    "language": 'Sanskrit',
    "title": 'Mahabharata',
    "year": -700,
    "category": 'Mystery',
  },
  {
    "author": 'Walt Whitman',
    "country": 'United States',
    "language": 'English',
    "title": 'Leaves of Grass',
    "year": 1855,
    "category": 'Drama',
  },
  {
    "author": 'Virginia Woolf',
    "country": 'United Kingdom',
    "language": 'English',
    "title": 'Mrs Dalloway',
    "year": 1925,
    "category": 'Historical',
  },
  {
    "author": 'Virginia Woolf',
    "country": 'United Kingdom',
    "language": 'English',
    "title": 'To the Lighthouse',
    "year": 1927,
    "category": 'Non-Fiction',
  },
  {
    "author": 'Marguerite Yourcenar',
    "country": 'France/Belgium',
    "language": 'French',
    "title": 'Memoirs of Hadrian',
    "year": 1951,
    "category": 'Thriller',
  },
]

# Número de libros por país

# contador = 0

# for book in books:
#     if book['country'] == 'France':
#         contador += 1
        
# print(contador)

# Número de libros por lenguaje
# Número de libros por autor
# allAuthors = []

# for i in range(len(books)):
#     if books[i]['author']:
#         allAuthors.append(books[i]['author'])

# numBooksPerAuthor = { i: allAuthors.count(i) for i in allAuthors}

# print(numBooksPerAuthor)

#  Por categoria, ej: 

allCategories = []

for book in books:
    if book["category"] not in allCategories:
            allCategories.append(book["category"])

booksPerCategory = {}

for i in allCategories:
    book = []
    for j in books:
        if j["category"] == i:
            book.append(j)  
    booksPerCategory[i] = book

# print(booksPerCategory)
# Por autor, ej #7
    
categories = {}

# for book in books:
#     if categories.get(book['category']):
#         categories[book['category']].append(book)
#     else:
#         categories[book['category']] = [book]

# Por language
# for book in books:
#     if categories.get(book['language']):
#         categories[book['language']].append(book)
#     else:
#         categories[book['language']] = [book]

print(categories)