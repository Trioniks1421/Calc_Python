import requests
import json
import pprint
import os

#
PRIVAT_BANK_URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
response = requests.get(PRIVAT_BANK_URL).text
response_to_json = json.loads(response)
file = os.path.join('operation.json')
for elem in response_to_json:
    print("Enter the currency available : {} ,on {} buy {}".format(elem["ccy"], elem["base_ccy"],
                                                                   elem["buy"]))


#
#
# def convert():
#     PRIVAT_BANK_URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
#     response = requests.get(PRIVAT_BANK_URL).text
#     response_to_json = json.loads(response)
#     file = os.path.join('operation.json')
#
#     def buy_convert():
#         for elem in response_to_json:
#             print("Enter the currency available : {} ,on {} buy {}".format(elem["ccy"], elem["base_ccy"],
#                                                                            elem["buy"]))
#
#         currency = input("")
#         for elem in response_to_json:
#             if currency.upper() == elem["ccy"]:
#                 num_ccy = float(input("Enter quantity->"))
#                 return {
#                     "currency": currency,
#                     "oper": act,
#                     "quantity": num_ccy,
#                     "res": num_ccy * float((elem["buy"])),
#                     "for_currency": elem["base_ccy"]
#                 }
#
#     def sale_convert():
#         for elem in response_to_json:
#             print("Enter the currency available : {} ,on {} buy {}".format(elem["ccy"], elem["base_ccy"],
#                                                                            elem["sale"]))
#         currency = input("").upper()
#         for elem in response_to_json:
#             if currency == elem["ccy"]:
#                 num_ccy = float(input("Enter quantity->"))
#                 return {
#                     "currency": elem["base_ccy"],
#                     "oper": act,
#                     "quantity": num_ccy,
#                     "result": num_ccy / float((elem["sale"])),
#                     "for_currency": elem["ccy"]
#                 }
#
#     try:
#
#         act = input("Buy or sale ? Enter on the keyboard \n").lower()
#         if act == "buy":
#             result = buy_convert()
#             with open(file, 'r') as f:
#                 operation_data = json.load(f)
#             operation_data.append(result)
#             with open(file, 'w+') as f:
#                 json.dump(operation_data, f)
#             print(result.values())
#
#         elif act == "sale":
#             result = sale_convert()
#             with open(file, 'r') as f:
#                 operation_data = json.load(f)
#             operation_data.append(result)
#             with open(file, 'w+') as f:
#                 json.dump(operation_data, f)
#             print(result.values())
#
#
#
#
#     except ValueError as a:
#         print(a)
#     except NameError as a:
#         print(a)
#     except ZeroDivisionError as a:
#         print(a)
#     except Exception as a:
#         print(a)
#
#     return True
#


# def buy_convert():
#         for elem in response_to_json:
#             print("Enter the currency available : {} ,on {} buy {}".format(elem["ccy"], elem["base_ccy"],
#                                                                            elem["buy"]))
#         currency = input(">")
#         for elem in response_to_json:
#             if currency == elem["ccy"]:
#                 num_ccy = float(input("Enter quantity->"))
#                 num_uah = num_ccy * float((elem["buy"]))
#                 nonlocal res
#                 res["currency"] = currency
#                 res["quantity"] = num_ccy
#                 res["res"] = num_uah
#                 return res
#
#
#     def sale_convert():
#         for elem in response_to_json:
#             print("Enter the currency available : {} ,on {} sale {}".format(elem["ccy"], elem["base_ccy"],
#                                                                             elem["sale"]))
#
#         currency = input(">")
#         for elem in response_to_json:
#             if currency == elem["ccy"]:
#                 num_uah = float(input("Enter quantity->"))
#                 num_ccy = num_uah / float((elem["sale"]))
#                 res = [num_ccy, elem["ccy"]]
#                 print(res)
#
#     while pool:
#         try:
#             act = input("Buy or sale ? Enter on the keyboard \n")
#             ###########################
#             if act == "buy":
#                 res=buy_convert()
#                 print(res1)
#             elif act == "sale":
#                 sale_convert()
#
#
#         except ValueError as a:
#             print(a)
#         except NameError as a:
#             print(a)
#         except ZeroDivisionError as a:
#             print(a)
#         except Exception as a:
#             print(a)
