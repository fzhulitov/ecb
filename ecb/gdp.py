import pandas as pd
import ecb


def get_gdp_q() -> pd.Series:
    df = ecb.request_data.get_data_frame('MNA', 'Q.N.I8.W2.S1.S1.B.B1GQ._Z._Z._Z.EUR.V.N', 'Q')
    return df