#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv


def dane_z_pliku(nazwa_pliku):
    dane = []  # pusta lista na dane
    with open(nazwa_pliku, 'r', newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delimiter='\t')
        for rekord in tresc:
            rekord = [x.strip() for x in rekord]  # oczyszczamy dane
            dane.append(rekord)  # dodawanie rekordów do listy
    return dane


#def kwerenda_1(cur):
    #cur.execute("""
       # SELECT * FROM fake_apps
    #""")

    #wyniki = cur.fetchall()  # pobranie wszystkich rekordów
    #for row in wyniki:  # odczytywanie rekordów
        #print(tuple(row))  # drukowanie pól


def main(args):
    con = sqlite3.connect('magazyn.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora

    # utworzenie tabeli w bazie
    with open('magazyn.sql', 'r') as plik:
        cur.executescript(plik.read())

    # dodawanie danych do bazy
    #dane = dane_z_pliku('dane_customers.txt')
    #print(dane)
    #dane.pop(0)  # usuń pierwszy rekord z listy
    #cur.executemany('INSERT INTO customers VALUES(?, ?, ?)', dane)
   
    dane = dane_z_pliku('dane_subscriptions.txt')
    print(dane)
    dane.pop(0)  # usuń pierwszy rekord z listy
    cur.executemany('INSERT INTO subscriptions VALUES(?, ?, ?, ?)', dane)
   
    dane = dane_z_pliku('dane_orders.txt')
    print(dane)
    dane.pop(0)  # usuń pierwszy rekord z listy
    cur.executemany('INSERT INTO orders VALUES(?, ?, ?, ?)', dane)



    #kwerenda_1(cur)

    con.commit()  # zatwierdzenie zmian w bazie
    con.close()  # zamknięcie połączenia z bazą
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
