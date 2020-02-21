#%%
import requests
import json
import csv

def initializeAPI(filename):
#Open API keys
    api_file = open(filename,'r')
    api_key = api_file.read()
    return api_key

def get_device_list(filename):
    """currently the devices api returns all existing devices.
    Therefore we are only using saved list of devices.
    """
    with open(filename,newline = '') as f:
        reader = csv.reader(f)
        device_list = list(reader)
    return device_list
    


def main():
    devices = get_device_list('device_list.csv')
    for device in devices:
        url = 'https://api.quant-aq.com/device-api/v1/devices/'+'%s' %device + '/data/raw/'
        data = requests.get(url, auth = (initializeAPI('API_key.txt'),''))
        data_json = data.json()
        realtime_data = data_json['data']
        
    print(device_info_list[0])

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
