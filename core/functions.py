import re

import requests
import pandas as pd
from sqlalchemy import text
import streamlit as st

import data.queries as nq
from data.postgre import postgre_engine_ailab as engine_ailab

table_names = ["wanted"]


@st.cache_data
def get_data(table_name):
    if table_name == "wanted":
        query = nq.FindAllFromWantedJobposting
    with engine_ailab.connect() as conn:
        fetch = conn.execute(text(query)).fetchall()
    return pd.DataFrame(fetch)


def replace_special_chars(text):
    pattern1 = r'(•|\[|⎻|-(?!\d)|\d+\.)'
    pattern2 = r'(\])'
    replaced_text = re.sub(pattern1, lambda m: f'  \n{m.group(0)}', text)
    replaced_text = re.sub(pattern2, lambda m: f'{m.group(0)}  \n', replaced_text)
    return replaced_text


def get_linked_profile_info(url, access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        st.error(f"Error fetching profile data: {response.content}")
        return None

    return response.json()
