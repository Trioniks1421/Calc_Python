import os
import requests
import json
import math


def Guest_calc():
    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def mult(x, y):
        return x * y

    def div(x, y):
        return x / y

    calc = {
        "+": add,
        "-": sub,
        "*": mult,
        "/": div,
    }
    while True:
        try:

            a = float(input("a="))
            oper = input("Введи доступную операцию-{}->".format(calc.keys()))
            b = float(input("b="))
            res = calc[oper](a, b)




        except ValueError:
            print("This is not number !!!")
        except ZeroDivisionError:
            print("Do not div by zero!!!")
        except KeyError:
            print("Such an operation is not list")
        except Exception:
            print(type(Exception))


def Auth_calc():
    file = os.path.join('operation.json')

    def convert():
        PRIVAT_BANK_URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
        response = requests.get(PRIVAT_BANK_URL).text
        response_to_json = json.loads(response)
        file = os.path.join('operation.json')

        def buy_convert():
            for elem in response_to_json:
                print("Enter the currency available : {} ,on {} buy {}".format(elem["ccy"], elem["base_ccy"],
                                                                               elem["buy"]))

            currency = input("")
            for elem in response_to_json:
                if currency.upper() == elem["ccy"]:
                    num_ccy = float(input("Enter quantity->"))
                    return {
                        "currency": currency,
                        "oper": act,
                        "quantity": num_ccy,
                        "res": num_ccy * float((elem["buy"])),
                        "for_currency": elem["base_ccy"]
                    }

        def sale_convert():
            for elem in response_to_json:
                print("Enter the currency available : {} ,on {} buy {}".format(elem["ccy"], elem["base_ccy"],
                                                                               elem["sale"]))
            currency = input("").upper()
            for elem in response_to_json:
                if currency == elem["ccy"]:
                    num_ccy = float(input("Enter quantity->"))
                    return {
                        "currency": elem["base_ccy"],
                        "oper": act,
                        "quantity": num_ccy,
                        "result": num_ccy / float((elem["sale"])),
                        "for_currency": elem["ccy"]
                    }

        try:

            act = input("Buy or sale ? Enter on the keyboard \n").lower()
            if act == "buy":
                result = buy_convert()
                with open(file, 'r') as f:
                    operation_data = json.load(f)
                operation_data.append(result)
                with open(file, 'w+') as f:
                    json.dump(operation_data, f)
                print(result.values())

            elif act == "sale":
                result = sale_convert()
                with open(file, 'r') as f:
                    operation_data = json.load(f)
                operation_data.append(result)
                with open(file, 'w+') as f:
                    json.dump(operation_data, f)
                print(result.values())




        except ValueError as a:
            print(a)
        except NameError as a:
            print(a)
        except ZeroDivisionError as a:
            print(a)
        except Exception as a:
            print(a)

        return True

    def add(x, y):
        return {
            "num1": x,
            "oper": "+",
            "num2": y,
            "result": x + y,

        }

    def sub(x, y):
        return {
            "num1": x,
            "oper": "-",
            "num2": y,
            "result": x - y,

        }

    def mult(x, y):
        return {
            "num1": x,
            "oper": "*",
            "num2": y,
            "result": x * y,

        }

    def div(x, y):
        return {
            "num1": x,
            "oper": "/",
            "num2": y,
            "result": x / y,

        }

    def sin_(x):
        return {
            "oper": "sin",
            "num1": x,
            "result": math.sin(x),

        }

    def cos(x):
        return {
            "oper": "cos",
            "num1": x,
            "result": math.cos(x),

        }

    calc_auth = {
        "+": add,
        "-": sub,
        "*": mult,
        "/": div,
        "sin": sin_,
        "cos": cos,
        "convert": convert
    }
    loop = True
    while loop:
        try:
            a = float(input("a="))
            oper = input("Введи доступную операцию-{}->".format(calc_auth.keys()))
            if oper == "sin" or oper == "cos" or oper == "convert":
                res = calc_auth[oper](a)
                with open(file, 'r') as f:
                    operation_data = json.load(f)
                operation_data.append(res)
                with open(file, 'w+') as f:
                    json.dump(operation_data, f)
                    print(res.values())
            else:
                b = float(input("b="))
                res = calc_auth[oper](a, b)
                with open(file, 'r') as f:
                    operation_data = json.load(f)
                operation_data.append(res)
                with open(file, 'w+') as f:
                    json.dump(operation_data, f)
                    print(res.values())



        except ValueError:
            print("This is not number !!!")
        except ZeroDivisionError:
            print("Do not div by zero!!!")
        except KeyError:
            print("Such an operation is not list")
        except Exception:
            print(type(Exception))
