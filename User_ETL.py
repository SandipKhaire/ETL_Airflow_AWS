import pandas as pd
import requests
import json
import s3fs
from datetime import datetime


def user_detail_etl():
    user_detail_list=[]
    for i in range(2):
        response = requests.get("https://randomuser.me/api/")
        json_data = response.json()
        refined_user_detail={'FirstName':json_data.get("results",None)[0].get("name",None).get("first",None),
                         'city':json_data.get("results",None)[0].get("location",None).get("city",None),
                         'email':json_data.get("results",None)[0].get("email",None)
        }
        user_detail_list.append(refined_user_detail)
    
    df=pd.DataFrame(user_detail_list)
    df.to_csv('s3://userairflowetl/refined_users_details_{}.csv'.format(datetime.now().strftime("%Y-%m-%d %H%M%S")),index=False)
    #df.to_csv("s3://userairflowetl/refined_users_details.csv",index=False)
    
if __name__ == "__main__":
    user_detail_etl()
    
    
    
