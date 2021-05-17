import xml.etree.ElementTree as ET
import requests


def root_xml(url):
    header = {'Accept': 'application/xml'}
    r = requests.get(url, headers=header)
    tree = ET.ElementTree(ET.fromstring(r.content))
    return tree.getroot()


def validate_price_products(context):
    root = root_xml(context.endpoint)
    products = []
    for product in root:
        if float(product[4].text) <= 0:
            products.append(product[0].text)

    return False if len(products) > 0 else True
