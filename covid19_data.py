import requests
import plotly.express as px
import pandas as pd
from requests import exceptions

name=input('Enter a Counry: ').title()

url=f"https://covid19-api.com/country?name={name}&format=json"
try:
    request=requests.get(url)
    data=request.json()

    for item in data:
        confirmed=item['confirmed']
        recovered=item['recovered']
        critical=item['critical']
        deaths=item['deaths']
        lastchange=item['lastChange']
        lastupdate=item['lastUpdate']
        confirm=item['confirmed']

    #['country', 'code', 'confirmed', 'recovered', 'critical', 'deaths', 'latitude', 'longitude', 'lastChange', 'lastUpdate']

    x_values=['Confirm', 'Recovered', 'Critical', 'Deaths']
    d={
        'confirmed':confirmed,
        'recovered':recovered,
        'critical':critical,
        'deaths':deaths

        }

    df=pd.DataFrame(data=d,index=[0])
    fig=px.bar(x=x_values, y=[confirmed,recovered,critical,deaths], title=f"Covid-19 Data in {name}", color=[confirmed,recovered,critical,deaths],
    labels={
            'x':' ',
            'y':'Numbers'

                })

    fig.show()

except:
    print("Invalid Country Name!")
