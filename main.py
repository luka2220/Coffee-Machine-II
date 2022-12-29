from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from database import CoffeeDatabase
from sales_data import SalesData
import datetime

machine_on = True

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

coffee_machine_database = CoffeeDatabase()

while machine_on:
    menu_options = menu.get_items()
    machine_input = input(f'What would you like? ({menu_options}) ').lower()

    if machine_input == 'off':
        machine_on = False
        break

    if machine_input == 'report':
        coffee_maker.report()
        money_machine.report()
        continue

    if machine_input == 'view order history':
        sqlite_sales_data = SalesData(coffee_machine_database.get_data())
        sqlite_sales_data.print_sales()
        continue

    drink_item = menu.find_drink(machine_input)

    if machine_input == 'espresso' or machine_input == 'latte' or machine_input == 'cappuccino':
        drink_item = menu.find_drink(machine_input)
        if coffee_maker.is_resource_sufficient(drink_item):
            if money_machine.make_payment(drink_item.cost):
                coffee_maker.make_coffee(drink_item)

                # save to sqlite database
                current_date = datetime.datetime.now()
                date = current_date.strftime("%d/%m/%Y")
                coffee_machine_database.save_data(date, drink_item.name, str(drink_item.cost))


coffee_machine_database.close_connection()
