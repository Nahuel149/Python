# Exercise 1: List Manipulation

fruits = ['date', 'apple', 'banana', 'cherry']
fruits.append('elderberry')
fruits.remove('banana')
fruits.sort()
print(fruits)

# Exercise 2: Dictionary Basics

student = {'name': 'John doe', 'age': 25, 'major': 'Computer Science'}
student['major'] = 'Electrical Engineering'
student['Year'] = 'Senior'
print(student.keys())
print(student.values())

# Exercise 3: List of Dictionaries

dict_movies = [
    {'title': 'Zohan', 'author': 'Adam Sandler', 'Year': 2010}, 
    {'title': 'Uncut Gems', 'author': 'Adam Sand.', 'Year': 2018},
    {'title': 'Fockers', 'author': 'Ben Stiller', 'Year': 2007}
]
print(f"The name of the movie is {dict_movies[1]['title']}")
print(f"The year of the movie is {dict_movies[2]['Year']}")

for movie in dict_movies:
    print(f"The name of the movie is {movie['title']}, the author is {movie['author']}")
else:
    print('There are no more movies')

# Exercise 4: Dictionary containing a List

dict_courses = [
    {'Math': 'Gabriel, Jonathan, Ramiro, Leonel, Matias, Leo'},
    {'History': 'Carlos, Ariel, Osmar, Leonardo, Pedro, Pablo'},
    {'Chemistry': 'Teo, Rodrigo, Fernando, Sebastian, Gio, Lucas'}
]

dict_courses[0].update({'Math': dict_courses[0]['Math'] + ', Eder, German, Emanuel, Bruno, Lucas'})
history_students = dict_courses[1]['History'].split(', ')
history_students.remove('Osmar')
dict_courses[1]['History'] = ', '.join(history_students)
# dict_courses.append({'Physics': 'Marcelo, Matias, Hernan, Sandra'})
dict_courses.insert(1, {'Physics': 'Marcelo, Matias, Hernan, Sandra'})
print(dict_courses)
print(dict_courses[2])
