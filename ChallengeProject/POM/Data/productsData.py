import random
import time


class Products():
    def __init__(self, driver):
        self.driver = driver


    women = [
        {
            "Product_Name": "Alphaboost shoes",
            "Sale_Price": 778.80,
            "Size": ['L'],
            "Color": ['Blue']
        },
        {
            "Product_Name": "Alphaedge 4d reflective shoes R",
            "Sale_Price": 146.30,
            "Size": ['M', 'XL'],
            "Color": ['Black', 'White']
        },
        {
            "Product_Name": "Edge gameday shoes",
            "Sale_Price": 1059.30,
            "Size": ['L', 'S'],
            "Color": ['Red', 'Blue', 'Black', 'White']
        },
        {
            "Product_Name": "Lite racer adapt 3.0 shoes",
            "Sale_Price": 984.50,
            "Size": ['L', 'S'],
            "Color": ['Red', 'Black', 'White']
        },
        {
            "Product_Name": "Senseboost go shoes",
            "Sale_Price": 687.00,
            "Size": ['X', 'XL'],
            "Color": ['Blue', 'Black', 'White']
        },
        {
            "Product_Name": "Custom chuck taylor all star by you",
            "Sale_Price": 510.40,
            "Size": ['X', 'M'],
            "Color": ['Green', 'Pink', 'Purple']
        }
    ]

    men = [
        {
            "Product_Name": "Strutter shoes",
            "Sale_Price": 422.40,
            "Size": ['L', 'XL'],
            "Color": ['Black', 'White', 'Grey']
        },
        {
            "Product_Name": "Nizza trefoil shoes",
            "Sale_Price": 217.80,
            "Size": ['M', 'L'],
            "Color": ['Black', 'White']
        },
        {
            "Product_Name": "Hacked fashion chuck taylor all star",
            "Sale_Price": 882.20,
            "Size": ['S', 'XL'],
            "Color": ['Blue', 'Brown']
        },
        {
            "Product_Name": "Seasonal color chuck 70",
            "Sale_Price": 185.90,
            "Size": ['S', 'XL'],
            "Color": ['Blue', 'Black', 'Green', 'Pink', 'Brown']
        },
        {
            "Product_Name": "Nike air zoom pegasus 35",
            "Sale_Price": 452.10,
            "Size": ['M', 'L'],
            "Color": ['Blue', 'Black', 'Green']
        }

    ]


    def getProducts(self, gender):
        if gender == "women":
            productsList : list = self.women

        elif gender == "men":
            productsList : list = self.men

        else:
            productsList : list = []

        return productsList



