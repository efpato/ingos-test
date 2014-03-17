# -*- coding: utf-8 -*-

import csv


class Bonus:
    def __init__(self, risk, optimal=None, premium=None, platinum=None):
        self.risk = risk
        self.optimal = optimal
        self.premium = premium
        self.platinum = platinum

    def __repr__(self):
        return '"Оптимал=\'{0.optimal}\',Премиум=\'{0.premium}\',Платинум=\'{0.platinum}\'"'.format(self)


class Car:
    def __init__(self, brand, model, year=None, price=None):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.results = []

    def __repr__(self):
        row = "{0.brand},{0.model},{0.year},{0.price}".format(self)
        for result in self.results:
            row += ",{0}".format(result)
        return row


def from_csv(csv_name):
    reader = csv.reader(open(csv_name))
    header = next(reader)
    data = []
    for row in reader:
        brand = row[0]
        model = row[1]
        for i in range(2, len(row)):
            data.append(Car(
                brand=brand.upper(),
                model=model.upper(),
                year=int(header[i]),
                price=int(row[i].replace(',', ''))
            ))
    return data
