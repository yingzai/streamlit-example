import streamlit as st
import pandas as pd

instances = [{'name': 'instance1', 'ip_address': '192.168.0.1'},
             {'name': 'instance2', 'ip_address': '192.168.0.2'},
             {'name': 'instance3', 'ip_address': '192.168.0.3'}]

df = pd.DataFrame(instances)
df['ip_address'] = df['ip_address'].apply(lambda x: f'<a href="http://ark.jd.com/#/monitor/snapshot-ip/{x}">{x}</a>')

st.write(df, unsafe_allow_html=True)
