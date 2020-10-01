import base64
def create_onedrive_directdownload (onedrive_link):
    data_bytes64 = base64.b64encode(bytes(onedrive_link, 'utf-8'))
    data_bytes64_String = data_bytes64.decode('utf-8').replace('/','_').replace('+','-').rstrip("=")
    resultUrl = f"https://api.onedrive.com/v1.0/shares/u!{data_bytes64_String}/root/content"
    return resultUrl


import pandas as pd 
# Input any OneDrive URL 
onedrive_url = "https://1drv.ms/x/s!AhnXJ-3UjJ5NgQzUCY5Hzbb8m8-j?e=SYKklv"
direct_download_url = create_onedrive_directdownload(onedrive_url)   
print(direct_download_url)# Load Dataset to the Dataframe   
df = pd.read_excel(direct_download_url)   
istop =1
print(df.head())# Continue with your data analysis ...