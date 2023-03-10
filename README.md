# Python_business-analyst
---

## OOP tasks

Завдання 1:

Створити класс автомобіля із функціями:
1. Функція виводу загальної інформації
2. Функція збільшення пробігу
3. функція підрахунку витрати палива на дорогу
4. функція підрахунку витрати часу на дорогу

Всі завдання зроблено в 1 классі. Результат виконання программи:
```
Марка автомобіля: Toyota Camry. Рік випуску: 2008. Колір: Чорний. Розхід палива на 100 кm: 10. Пробіг: 340000
Марка автомобіля: Toyota Camry. Рік випуску: 2008. Колір: Чорний. Розхід палива на 100 кm: 12.1. Пробіг: 375000
На дорогу відстаню 5000км прийдеться витратити 605.0л палива
На дорогу відстаню 5000км прийдеться витратити 62.5 годин
```

Завдання 2:

Створити батьківський клас Студент (Student). Встановлення усіх
атрибутів має відбуватись у методі ініціалізації екземпляра класу.
Атрибути:
1. Ім’я name.
2. Вік age.

Методи:

1. Метод виведення інформації про студента info().
2. Метод remains(), який визначає кількість років до випуску в
залежності від віку студента (з розрахунку: 17 років – залишилось навчатись
5 років, 22 роки – залишилось навчатись 0 років).

На основі батьківського класу Студент (Student) створити підкласи
Бакалавр (Bachelor), Магістр (Master) і Аспірант (PhDStudent). У кожному з
підкласів мають бути нові атрибути: рік вступу year та тема диплому topic.
Перевизначити метод info() для кожного підкласу так, щоб він виводив
додаткове повідомлення «Тема дипломного проекту (для підкласу Бакалавр) 

Результат виконання програми:
```
Студент класу 'Student'
метод 'about':
Студент: Andriy Kindrat.
Курс: 2.
Oцінки: 68/73/81 балів.
метод 'next_year':
Студент перейшов на 3 курс.

Студент класу 'ContractorStud'
метод 'about':
Студент: Vlad Melnuk.
Курс: 3.
Oцінки: 61/72/60 балів.
Неоплачено за навчання по контракту..
метод 'next_year':
Студент не перейшов на наступний курс через те, щo не оплатив контрактне навчання.

Студент класу 'BudgetStud'
метод 'about':
Студент: Oleg Biluy.
Курс: 1.
Oцінки: 81/92/83 балів.
Стипендія: відсутня..
метод 'next_year':
Студент перейшов на 1 курс.
Степендія студента: 1100грн.

Поліморфічна функція:
1. Для об'єкта класу 'ContractorStud':
Студент не перейшов на наступний курс через те, щo не оплатив контрактне навчання.

Вартість навчання студента становить 10000 гривень
2. Для об'єкта класу 'BudgetStud':
Студент перейшов на 1 курс.
Степендія студента: 1100грн.
```

---
## tasks

### Завдання 1.
Заданий малюнок, що являє собою матрицю, в якій частина клітинок зафарбована білою фарбою (має знаення ' ' (пробіл)), інша частина зафарбована іорною фарбою (має значення 'Х'). Фігурою на такому малюнку називається сукупність чорних клітин ('X'), для довільної пари яких центри клітин можнна з'єднати ламаною, що повністю міститься у чорних клітинках ('X'). Різними фінурами називають такі, які неможливосумістити послідовним застосуванням паралельних переносів, поворотів на 90° і симетрії відносно вертикальної чи горизонтальної прямої. Визначте кількість усіх фігур на малюнку та кількість різних фігур.

Матириця:

```Python
MATRIX = [ # Основна матриця
    ["X", " ", "X", " ", "X", " ", " ", "X"],
    ["X", "X", " ", "X", "X", "X", "X", "X"],
    ["X", "X", "X", " ", " ", "X", " ", " "],
    [" ", " ", "X", " ", "X", " ", "X", " "],
    [" ", "X", "X", "X", " ", "X", "X", "X"],
    ["X", "X", "X", "X", "X", " ", "X", " "],
    [" ", "X", " ", " ", "X", "X", "X", " "],
    [" ", " ", "X", " ", "X", " ", " ", "X"]
]
```

Результат виконання для цієї матриці:

```
На матриці знайдено 22 фігур, із яких:
11 рівнобедрених трикутників
3 Квадратів
8 фігур симетричних відносно своєї осі
усього 3 види різноманітних фігур
```

### Завдання 2.
За допомогою генератора псевдрвипадкових чисел згенерувати реченння. Слова
вибираються із масивів артиклів, іменників, дієслів, прийменників у такому порядку: артикль,
іменник, дієслово, прийменник, артикль, іменник. Перше слово речення має починатися з
великої літери.

Результат:
```
Що Влад взяв з-за чо хлопчина
```

### Завдання 3.
Алгоритм сортування масивів: суть, особливості, ефективність, складність. Приклад
программи одного із алгоритмів.

Результат виконання программи:

```
Программа для визначення найкращого алгоритму сортування масивів
Алгоритми: 
Bubble Sort (Бульбашковий алгоритм)
Merge sort (Сортування злиттям)
Insertion sort (Сортування вставкою)
Shell sort (Сортування оболонкою)   
Selection sort (Видільне Сортування)
(Тест проводиться на рандомних масивах довжиною 5 000 елементів)
Таблиця лідерів
+----------------+----------------+------------+------------+----------------+-------------+
| Алгоритм:      | Insertion sort | Merge sort | Shell sort | Selection sort | Bubble Sort |
+----------------+----------------+------------+------------+----------------+-------------+
| Час виконання: | 0.001          | 0.004      | 0.01       | 0.84761        | 2.55211     |
+----------------+----------------+------------+------------+----------------+-------------+
Найкращий алгоритм сортування - Insertion sort
```

### Завдання 4

Поняття циклічних процесів: умови виконання циклів, умови зацикленості программи, переривання циклів, вкладені цикли, нескінчені цикли. Приклад програми із вкладеними циклами.

Як приклад ми за допомогою циклів виведемо елементи матриці через кому

Матриця:
```Python
matrix = [[2, 6, 10], [3, 1, 5], [0, 4, 9]]
```

Результат:
```
2, 6, 10, 3, 1, 5, 0, 4, 9
```

---
## xml

Завдання:

Знайти будь яке xml api, Спарсити дані у xml файл, обробити цей файл та вивести дані. Записати результат у .txt файл.

Для прикладу було взято api із курсами валют від bank.gov.ua "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

результат виконання программи:
```
Программа для получення точного і свіжного курсу усіх відомих валют відносно гривні і подання у зручному форматі

Робимо запрос на сервер...
Збераємо дані із сервера...
Зберігаємо данні на комп'юері...
Дані збережено!

Обробляємо дані...
Збираємо потрібні дані...
Форматуємо дані...
Усе готово!!!

+------------------------------------+---------+----------------+------------+
| Валюта                             |   Номер |           Курс | Дата       |
+====================================+=========+================+============+
| Австралійський долар               |      36 |    24.7752     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Канадський долар                   |     124 |    26.9999     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Юань Женьміньбі                    |     156 |     5.2506     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Чеська крона                       |     203 |     1.6159     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Данська крона                      |     208 |     5.2449     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Гонконгівський долар               |     344 |     4.6647     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Форинт                             |     348 |     0.097469   | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Індійська рупія                    |     356 |     0.44198    | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Рупія                              |     360 |     0.0023484  | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Новий ізраїльський шекель          |     376 |    10.3918     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Єна                                |     392 |     0.27586    | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Теньге                             |     398 |     0.079042   | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Вона                               |     410 |     0.028735   | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Мексиканське песо                  |     484 |     1.8887     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Молдовський лей                    |     498 |     1.9088     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Новозеландський долар              |     554 |    23.1662     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Норвезька крона                    |     578 |     3.7098     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Російський рубль                   |     643 |     0.5199     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Сінгапурський долар                |     702 |    27.1966     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Ренд                               |     710 |     2.1532     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Шведська крона                     |     752 |     3.4964     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Швейцарський франк                 |     756 |    39.6064     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Єгипетський фунт                   |     818 |     1.4804     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Фунт стерлінгів                    |     826 |    44.0834     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Долар США                          |     840 |    36.5686     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Білоруський рубль                  |     933 |    13.2919     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Азербайджанський манат             |     944 |    21.5109     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Румунський лей                     |     946 |     7.8903     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Турецька ліра                      |     949 |     1.9552     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| СПЗ (спеціальні права запозичення) |     960 |    48.7988     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Болгарський лев                    |     975 |    19.9424     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Євро                               |     978 |    39.0041     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Злотий                             |     985 |     8.3469     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Алжирський динар                   |      12 |     0.2662     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Така                               |      50 |     0.35078    | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Вірменський драм                   |      51 |     0.092915   | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Домініканське песо                 |     214 |     0.65264    | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Іранський ріал                     |     364 |     0.00087068 | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Іракський динар                    |     368 |     0.025047   | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Сом                                |     417 |     0.4268     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Ліванський фунт                    |     422 |     0.024258   | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Лівійський динар                   |     434 |     7.573      | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Малайзійський ринггіт              |     458 |     8.3035     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Марокканський дирхам               |     504 |     3.4993     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Пакистанська рупія                 |     586 |     0.16151    | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Саудівський ріял                   |     682 |     9.7311     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Донг                               |     704 |     0.0015474  | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Бат                                |     764 |     1.05907    | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Дирхам ОАЕ                         |     784 |     9.9569     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Туніський динар                    |     788 |    11.7456     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Узбецький сум                      |     860 |     0.0032576  | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Новий тайванський долар            |     901 |     1.18988    | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Туркменський новий манат           |     934 |    10.4482     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Сербський динар                    |     941 |     0.33288    | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Сомоні                             |     972 |     3.5843     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Ларі                               |     981 |    13.5605     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Бразильський реал                  |     986 |     6.9267     | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Золото                             |     959 | 66326.3        | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Срібло                             |     961 |   875.64       | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Платина                            |     962 | 37702.2        | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
| Паладій                            |     964 | 64909.3        | 03.01.2023 |
+------------------------------------+---------+----------------+------------+
```

xml та txt файли зберержено у директорії проекту

---