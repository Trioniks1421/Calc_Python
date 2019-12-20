import os
import requests
import json
import math

PRIVAT_BANK_URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
response = requests.get(PRIVAT_BANK_URL).text
response_to_json = json.loads(response)
file = os.path.join('operation.json')


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
    pool_guest = True
    while pool_guest:
        try:
            a = float(input("a="))
            oper = input("Enter an available operation-{}->".format(calc.keys()))
            b = float(input("b="))
            res = calc[oper](a, b)
            print(res)
            repl = input("Continue or not (y/n)->")
            if repl == "y":
                pass
            elif repl == "n":
                pool_guest = False
            else:
                raise ValueError
        except ValueError:
            print(" Data entered incorrectly!!!")
        except ZeroDivisionError:
            print("Do not div by zero!!!")
        except KeyError:
            print("Such an operation is not list")
        except Exception:
            print(type(Exception))


def Auth_calc():
    def add_to_json(dict):
        with open(file, "r") as f:
            data_operation = json.load(f)
        data_operation.append(dict)
        with open(file, "w") as f:
            json.dump(data_operation, f)

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

    def sin(x):
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

    def convert():
        def buy_convert():
            for elem in response_to_json:
                print("Enter the currency available : {} on {} buy {}".format(elem["ccy"], elem["base_ccy"],
                                                                              elem["buy"]))
            currency = input(" ")
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
                add_to_json(result)
                print(result)
            if act == "sale":
                result = sale_convert()
                add_to_json(result)
                print(result)
        # with open(DATA_FILENAME, mode='r', encoding='utf-8') as feedsjson:
        #     feeds = json.load(feedsjson)
        # with open(DATA_FILENAME, mode='w', encoding='utf-8') as feedsjson:
        #     entry = {}
        #     entry['name'] = args.name
        #     entry['url'] = args.url
        #     json.dump(entry, feedsjson)
        except Exception as a:
            print(a)

    calc_auth = {
        "+": add,
        "-": sub,
        "*": mult,
        "/": div,
        "sin": sin,
        "cos": cos,

    }
    try:
        print("open conversion or calculator?(Press *convert* if you want conversion"
              "or press *calc* if you want open calculator")
        press_str = input()
        if press_str == "convert":
            convert()
        elif press_str == "calc":
            a = float(input("a="))
            oper = input("Enter an available operation-{}->".format(calc_auth.keys()))
            if oper == "sin" or oper == "cos":
                res = calc_auth[oper](a)
                add_to_json(res)
            else:
                b = float(input("b="))
                res = calc_auth[oper](a, b)
                add_to_json(res)
                print(res.values())
    except Exception as a:
        print(a)
