# -*- coding: utf-8 -*-


class Controller:
    @staticmethod
    def option(select, text):
        for option in select.find_elements_by_tag_name("option"):
            if option.text.encode('utf-8') == text:
                return option

    def __init__(self, driver):
        self.driver = driver

    @property
    def car_brand(self):
        return self.driver.find_element_by_xpath("//select[@id='view_marka']")

    @property
    def car_model(self):
        return self.driver.find_element_by_xpath("//select[@id='modell']")

    @property
    def car_year(self):
        return self.driver.find_element_by_xpath("//select[@id='view_year']")

    @property
    def car_price(self):
        return self.driver.find_element_by_xpath("//input[@id='price_auto']")

    @property
    def car_usage_date(self):
        return self.driver.find_element_by_xpath("//input[@id='UsageDate']")

    @property
    def car_horse_power(self):
        return self.driver.find_element_by_xpath("//select[@id='hoursePower']")

    @property
    def new_car(self):
        return self.driver.find_element_by_id("radio_var_new")

    @property
    def old_car(self):
        return self.driver.find_element_by_id("radio_var_old")

    @property
    def credit(self):
        return self.driver.find_element_by_id("radio_var_Credit")

    @property
    def no_credit(self):
        return self.driver.find_element_by_id("radio_var_NoCredit")

    @property
    def auto_start_yes(self):
        return self.driver.find_element_by_id("radio_var_startyes")

    @property
    def auto_start_no(self):
        return self.driver.find_element_by_id("radio_var_startno")

    @property
    def closed_list(self):
        return self.driver.find_element_by_id("radio_var_clossp")

    @property
    def driver_age(self):
        return self.driver.find_element_by_id("age_driver_first")

    @property
    def driver_experience(self):
        return self.driver.find_element_by_id("experience_first")

    @property
    def driver_sex(self):
        return self.driver.find_element_by_id("gender_first")

    @property
    def driver_marital_status(self):
        return self.driver.find_element_by_id("marstatus_first")

    @property
    def driver_children(self):
        return self.driver.find_element_by_id("children_first")

    @property
    def insurance_period(self):
        return self.driver.find_element_by_id("strahperiod")

    @property
    def invariable_insured_sum(self):
        return self.driver.find_element_by_id("radio_vp1")

    @property
    def variable_insured_sum(self):
        return self.driver.find_element_by_id("NoAmort")

    @property
    def no_franchise(self):
        return self.driver.find_element_by_id("radio_v1")

    @property
    def last_name(self):
        return self.driver.find_element_by_id("Cont_Family")

    @property
    def first_name(self):
        return self.driver.find_element_by_id("Cont_Last")

    @property
    def patronymic(self):
        return self.driver.find_element_by_id("Cont_First")

    @property
    def phone_code(self):
        return self.driver.find_element_by_id("Calc_PhoneCode")

    @property
    def phone_number(self):
        return self.driver.find_element_by_id("Calc_PhoneNumber")

    @property
    def email(self):
        return self.driver.find_element_by_id("Calc_Email")

    @property
    def calculate(self):
        return self.driver.find_element_by_id("CalcButton")

    @property
    def calculate_loading(self):
        return self.driver.find_element_by_id("loadingCalc")

    @property
    def only_damage(self):
        return self.driver.find_element_by_id("DamageVariant")

    @property
    def driving_away_without_keys_plus_damage(self):
        return self.driver.find_element_by_id("StealDamageVariant")

    @property
    def loading(self):
        return self.driver.find_element_by_id("loading")

    @property
    def optimal(self):
        return self.driver.find_element_by_id("forAGRMOTOROPT").find_element_by_xpath("..")

    @property
    def premium(self):
        return self.driver.find_element_by_id("forAGRMOTORCA2003").find_element_by_xpath("..")

    @property
    def platinum(self):
        return self.driver.find_element_by_id("forAGRMOTORPLATINUM").find_element_by_xpath("..")

    @property
    def result_cost(self):
        return self.driver.find_element_by_xpath("//div[@id='resultCost']/h1")