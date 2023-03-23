import pandas as pd
from sqlalchemy import text

import data.queries as nq
from data.postgre import postgre_engine_ailab as engine_ailab

table_names = ["wanted"]


def get_data(table_name):
    if table_name == "wanted":
        query = nq.FindAllFromWantedJobposting
    with engine_ailab.connect() as conn:
        fetch = conn.execute(text(query)).fetchall()
    return pd.DataFrame(fetch)
