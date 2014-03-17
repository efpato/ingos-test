#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import time
from json import JSONDecoder
from selenium.webdriver import Firefox

from controller import Controller
from car import from_csv, Bonus


class KaskoCalcTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(KaskoCalcTestCase, self).__init__(*args, **kwargs)
        config = JSONDecoder().decode(open("config.json").read())
        self.url = config.get("url")
        csv_file = config.get("csv_file")
        self.cars = from_csv(csv_file)
        self.controller = None

    def tearDown(self):
        self.dump_out()

    def dump_out(self):
        with open("out.csv", 'w') as fd:
            fd.write("Марка,Модель,Год,Цена,Только ущерб (без угона),Угон (без ключей) + ущерб\n")
            for car in self.cars:
                fd.write('{0}\n'.format(car))

    def test(self):
        for car in self.cars:
            try:
                self.controller = Controller(Firefox())
                self.controller.driver.maximize_window()
                self.controller.driver.get(self.url)

                self.controller.option(self.controller.car_brand, car.brand).click()
                time.sleep(1)
                self.controller.option(self.controller.car_model, car.model).click()
                self.controller.option(self.controller.car_year, str(car.year)).click()
                self.controller.car_price.send_keys(car.price)
                self.controller.car_usage_date.send_keys("01.01.{0}".format(car.year))
                self.controller.option(self.controller.car_horse_power, u"201 и более").click()
                self.controller.new_car.click() if car.year == 2014 else self.controller.old_car.click()
                self.controller.no_credit.click()
                self.controller.auto_start_no.click()
                self.controller.closed_list.click()
                self.controller.driver_age.clear()
                self.controller.driver_age.send_keys(30)
                self.controller.driver_experience.clear()
                self.controller.driver_experience.send_keys(10)
                self.controller.option(self.controller.driver_sex, u"Мужской").click()
                self.controller.option(self.controller.driver_marital_status, u"Состою в браке").click()
                self.controller.option(self.controller.driver_children, u"Есть").click()
                self.controller.option(self.controller.insurance_period, u"1 год").click()
                self.controller.variable_insured_sum.click()
                self.controller.no_franchise.click()
                self.controller.last_name.send_keys(u"Фамилия")
                self.controller.first_name.send_keys(u"Имя")
                self.controller.patronymic.send_keys(u"Отчество")
                self.controller.phone_code.send_keys(u"999")
                self.controller.phone_number.send_keys(u"9999999")
                self.controller.email.send_keys(u"1@example.com")
                self.controller.calculate.click()
                while self.controller.calculate_loading.is_displayed():
                    time.sleep(1)

                self.controller.only_damage.click()
                while self.controller.loading.is_displayed():
                    time.sleep(1)
                bonus = Bonus(risk="Только ущерб (без угона)")
                self.controller.optimal.click()
                bonus.optimal = self.controller.result_cost.text.encode('utf-8')
                self.controller.premium.click()
                bonus.premium = self.controller.result_cost.text.encode('utf-8')
                self.controller.platinum.click()
                bonus.platinum = self.controller.result_cost.text.encode('utf-8')
                car.results.append(bonus)

                self.controller.driving_away_without_keys_plus_damage.click()
                while self.controller.loading.is_displayed():
                    time.sleep(1)
                bonus = Bonus(risk="Угон (без ключей) + ущерб")
                self.controller.optimal.click()
                bonus.optimal = self.controller.result_cost.text.encode('utf-8')
                self.controller.premium.click()
                bonus.premium = self.controller.result_cost.text.encode('utf-8')
                self.controller.platinum.click()
                bonus.platinum = self.controller.result_cost.text.encode('utf-8')
                car.results.append(bonus)
            except Exception as e:
                self.controller.driver.close()
                raise e


if __name__ == '__main__':
    unittest.main(verbosity=2)
