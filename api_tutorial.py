#%%
import requests
import json
import csv
import pandas as pd

def initializeAPI(filename):
#Open API keys
    api_file = open(filename,'r')
    global api_key
    api_key = api_file.read()


def get_device_list(filename):
    """currently the devices api returns all existing devices.
    Therefore we are only using saved list of devices.
    """
    device_list = []
    with open(filename,'r',newline = '') as f:
        readCSV = csv.reader(f, delimiter = '\t')
        for row in readCSV:
            row = row[0]
            row = row.replace(u'\ufeff','')
            device_list.append(row)
    return device_list
    
def create_csv_frame():
    data = requests.get('https://api.quant-aq.com/device-api/v1/devices/SN000-062/data/raw/?limit=1', auth = (api_key,''))
    columns = list(data.json()['data'][0].keys())
    return columns

def save_data(device_sn):
    url = 'https://api.quant-aq.com/device-api/v1/devices/'+'%s' %device_sn + '/data/raw/'
    data = requests.get(url, auth = (api_key,''))
    data_json = data.json()
    # df = pd.read_json(json.dumps(data_json))
    # df = pd.read_json(data.text)
    realtime_data = data_json['data']
    data_list = []
    for one_time_dict in realtime_data:
        one_data_list = []
        for key in one_time_dict.keys():
            if type(one_time_dict[key]) is dict:
                one_time_dict[key] = flatDict(one_time_dict[key])
            one_data_list.append(one_time_dict[key])
        data_list.append(one_data_list)
    return data_list


def flatDict(dictt):
    flattened = []
    for key in dictt.keys():
        flattened.append(dictt[key])
    return flattened


def main():
    initializeAPI('API_key.txt')
    devices = get_device_list('device_list.csv')
    csv_column = create_csv_frame()
    for device in devices:
        all_data = save_data(device)
        df = pd.DataFrame(all_data)
        df.columns = csv_column
        df.to_csv('savedata/%s.csv' %device)



main()
#%%

# device_list_json = device_list.json()
# device_info_list = device_list_json['data']
# for i in range((len(device_info_list))):
#     print(device_info_list[i]['sn'])
# print(device_info_list[0]['sn'])



# data = requests.get('https://api.quant-aq.com/device-api/v1/devices/SN000-062/data/raw/', auth = (api_key,''))
# print(data.json())
# # %%


# %%
