import streamlit as st
import ipaddress
import pandas as pd
from ip2geotools.databases.noncommercial import DbIpCity
from requests import get


def getlocbyip(ip):
    try:
        res = DbIpCity.get(ip, api_key="free")
    except:
        st.write("Error getting location")
    return res.latitude, res.longitude


def isvalidip(ip):
    try:
        iptest = ipaddress.ip_address(ip)
        return True
    except:
        return False


def getmyip():
    myip = get('https://api.ipify.org').content.decode('utf8')
    return myip


st.title("IP to Map Location")
st.divider()
myip = getmyip()
ip = st.text_input('IP to Locate:', myip)
if st.button("Get location"):
    if isvalidip(ip):
        lat, lon = getlocbyip(ip)
        data = pd.DataFrame({'latitude': [lat], 'longitude': [lon]})
        st.map(data, color="#ff000088", zoom=12)
        st.write("For test purpose only, location might not be accurate")
    else:
        st.write(ip + " is not a valid ip")