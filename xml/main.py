# -*- coding: utf-8 -*-


# Імпорт необхідних бібліотек
import requests # Бібліотека для запросів на сервер
from bs4 import BeautifulSoup as bs # Бібліотека для обробки даних із xml файла
from tabulate import tabulate # Бібліотека для створення таблиць
from rich import print # Бібліотека для різнокольорового виводу
from time import sleep # бібліотека для затримки программи
# Встановити усі бібліотеки:
# pip install requirements.txt


def loadRSS():
  
    # Додаємо силку на сервер
    try:
        print("[italic green]Робимо запрос на сервер...[/italic green]")
        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
    
        # створення об’єкта відповіді HTTP з заданої URL-адреси
        sleep(2)
        print("[italic green]Збераємо дані із сервера...[/italic green]")
        resp = requests.get(url)
    
        # Відкриваємо xml файл та вписуємо в нього інформацію получену із сервера
        sleep(2)
        print("[italic green]Зберігаємо данні на комп'юері...[/italic green]")
        with open("currency.xml", "wb") as f:
            f.write(resp.content)

        sleep(2)
        print("[italic green]Дані збережено![/italic green]")
    
    except Exception as ex:
        print(f"[!] error:\n{ex}")
          
  
def parseXML(xmlfile = "currency.xml"):
    
    try:

        sleep(2)
        print("[italic green]\nОбробляємо дані...[/italic green]")
        content = []
        # Читаємо xml файл
        with open(xmlfile, "r", encoding="utf-8") as file:
            # Читаємо кожен рядок файлу
            content = file.readlines()
            # Об’єднуємо рядки списку в рядок
            content = "".join(str(content))
            # Передаємо дані у інструмент роботи з xml
            bs_content = bs(content, "lxml")

        #print(bs_content)
        sleep(2)
        print("[italic green]Збираємо потрібні дані...[/italic green]")
        # Дістаємо інформацію із тегів
        numbers = bs_content.findAll("r030")
        names = bs_content.findAll("txt")
        courses = bs_content.findAll("rate")
        dates = bs_content.findAll("exchangedate")

        mydata = []
        #print(names)
        for i in range(len(numbers)):

            # Збираємо із тегів лише текст
            names[i] = names[i].text
            numbers[i] = numbers[i].text
            courses[i] = courses[i].text
            dates[i] = dates[i].text

            # Створємо список для таблиці
            mydata.append([names[i], numbers[i], courses[i], dates[i]])

        sleep(2)
        print("[italic green]Форматуємо дані...[/italic green]")
        # Створюємо заголовок для таблиці
        head = ["Валюта", "Номер", "Курс", "Дата"]
        #print(mydata)
        sleep(2)
        print("[italic green]Усе готово!!!\n[/italic green]")
        sleep(2)
        # Створюємо та виводимо таблицю
        result = tabulate(mydata, headers=head, tablefmt="grid")

        f = open("result.txt", "w", encoding = "utf-8")
        f.write(result)

        print(result)

    except Exception as ex:
        print(f"[!] error:\n{ex}")
    
def main():

    # Викликаємо функції
    print("[bold blue]Программа для получення точного і свіжного курсу усіх відомих валют відносно гривні і подання у зручному форматі\n[/bold blue]")
    loadRSS()
    parseXML()
      
      
if __name__ == "__main__":
  
    # Запускаємо программу
    main()