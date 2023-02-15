/* Задание на урок:

1) Создать переменную numberOfFilms и в неё поместить ответ от пользователя на вопрос:
'Сколько фильмов вы уже посмотрели?'

2) Создать объект personalMovieDB и в него поместить такие свойства:
    - count - сюда передается ответ на первый вопрос
    - movies - в это свойство поместить пустой объект
    - actors - тоже поместить пустой объект
    - genres - сюда поместить пустой массив
    - privat - в это свойство поместить boolean(логическое) значение false

3) Задайте пользователю по два раза вопросы:
    - 'Один из последних просмотренных фильмов?'
    - 'На сколько оцените его?'
Ответы стоит поместить в отдельные переменные
Записать ответы в объект movies в формате: 
    movies: {
        'logan': '8.1'
    }

Проверить, чтобы все работало без ошибок в консоли */

'use strict';

const numberOfFilms = +prompt('Сколько фильмов вы уже посмотрели?', '');

const personalMovieDB = {
    count: numberOfFilms,
    movies: {},
    actors: {},
    genres: [],
    privat: false
};

const answer1 = prompt('Один из последних просмотренных фильмов?', ''),
      answer2 = prompt('На сколько оцените его?', ''),
      answer3 = prompt('Один из последних просмотренных фильмов?', ''),
      answer4 = prompt('На сколько оцените его?', '');

 personalMovieDB.movies[answer1] = answer2;
 personalMovieDB.movies[answer3] = answer4;

 console.log(personalMovieDB );

const storeName =  'My store';
const storeDescription = {
    budget: 10000,
    employees: ['Denis', 'Lena', 'Stefan'],
    products: {
        Tea: 1,
        Koffe: 2
    },
    open: true
};