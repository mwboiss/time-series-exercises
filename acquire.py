import pandas as pd
import requests
import os
from vega_datasets import data

def get_items(use_cache=True):
    
    filename = 'items.csv'
    if os.path.exists(filename) and use_cache:
        return pd.read_csv(filename)
    
    domain = 'https://api.data.codeup.com'
    endpoint = '/api/v1/items'
    items = []

    while endpoint != None:
        url = domain + endpoint
        response = requests.get(url)
        data = response.json()
        items.extend(data['payload']['items'])
        endpoint = data['payload']['next_page']

    items = pd.DataFrame(items)
    items.to_csv('items.csv',index=False)
    return items

def get_stores(use_cache=True):
    
    filename = 'stores.csv'
    if os.path.exists(filename) and use_cache:
        return pd.read_csv(filename)
    
    domain = 'https://api.data.codeup.com'
    endpoint = '/api/v1/stores'
    stores = []

    while endpoint != None:
        url = domain + endpoint
        response = requests.get(url)
        data = response.json()
        stores.extend(data['payload']['stores'])
        endpoint = data['payload']['next_page']

    stores = pd.DataFrame(stores)
    stores.to_csv('stores.csv',index=False)
    return stores

def get_sales(use_cache=True):
    
    filename = 'sales.csv'
    if os.path.exists(filename) and use_cache:
        return pd.read_csv(filename)
    
    domain = 'https://api.data.codeup.com'
    endpoint = '/api/v1/sales'
    sales = []

    while endpoint != None:
        url = domain + endpoint
        response = requests.get(url)
        data = response.json()
        sales.extend(data['payload']['sales'])
        endpoint = data['payload']['next_page']
        #print(endpoint)

    sales = pd.DataFrame(sales)
    sales.to_csv('sales.csv',index=False)
    return sales

def combine():
    
    sales = get_sales()
    items = get_items()
    stores = get_stores()
    
    combined = sales.merge(items,left_on='item',right_on='item_id')
    combined = combined.merge(stores,left_on='store',right_on='store_id')
    
    return combined

def get_power_data(use_cache=True):
    '''
    A function to acquire the German power systems data
    '''
    # Assign filename to look up
    filename = 'german_power.csv'
    
    #Check for file and return csv if present
    if os.path.exists(filename) and use_cache:
        return pd.read_csv(filename)
    
    # Aquire data
    power = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
    
    # Assign to CSV
    power.to_csv('german_power.csv',index=False)
    
    # Return power
    return power
    