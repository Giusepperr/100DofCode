from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

#Initiate objects
machine = CoffeeMaker()
menu = Menu()
moneyMachine = MoneyMachine()

espresso = MenuItem(name = 'espresso', water=400, milk=0,coffee=30, cost=2.5)
latte = MenuItem(name = 'latte',water=100,milk=100,coffee=60, cost=3)
cappuccino = MenuItem(name = 'cappuccino',water=100, milk=50,coffee=60, cost=3)

dictItems = {
    'latte':latte,
    'espresso':espresso,
    'cappuccino':cappuccino
}

#Print report
machine.report()
again = True
while (again):
    print(f'What msenu item are you looking for? choose between: {menu.get_items()}')
    item = input('')
    #Check Res are sufficient
    if machine.is_resource_sufficient(dictItems[item]):
    #Process Coins
    #Check transaction successful
        if(moneyMachine.make_payment(dictItems[item].cost)):
            machine.make_coffee(dictItems[item])
            moneyMachine.report()
        else:
            print('As money were not enough please start again')

    #make coffee
    else:
        print('resources not sufficient')
