"""Shared helpers. The district code for Chikkodi is the two letters N-A, which pandas would
read as a missing value unless told otherwise, so every CSV is read through read()."""
import pandas as pd

# One spelling per district code (the board changed spellings over the years).
DIST = {
    'AN': 'BENGALURU NORTH', 'AS': 'BENGALURU SOUTH', 'BA': 'RAMANAGARA', 'BB': 'BENGALURU RURAL',
    'CA': 'CHIKKABALLAPURA', 'CC': 'KOLAR', 'DA': 'MADHUGIRI', 'DD': 'TUMAKURU', 'EA': 'CHAMARAJANAGARA',
    'EE': 'MYSURU', 'FF': 'MANDYA', 'GA': 'UDUPI', 'GG': 'DAKSHINA KANNADA', 'HH': 'KODAGU',
    'IA': 'DAVANAGERE', 'II': 'CHITRADURGA', 'JJ': 'CHIKKAMAGALURU', 'KK': 'SHIVAMOGGA', 'LL': 'HASSAN',
    'MA': 'HAVERI', 'MB': 'GADAG', 'MM': 'DHARWAD', 'NA': 'CHIKKODI', 'NN': 'BELAGAVI', 'OA': 'BAGALAKOTE',
    'OO': 'VIJAYAPURA', 'PA': 'SIRSI', 'PP': 'UTTARA KANNADA', 'QA': 'YADAGIRI', 'QQ': 'KALABURAGI',
    'RA': 'KOPPALA', 'RR': 'RAICHURU', 'SS': 'BIDAR', 'TA': 'VIJAYANAGARA', 'TT': 'BALLARI',
}
NAME2CODE = {v: k for k, v in DIST.items()}
# Vijayanagara was carved out of Ballari; merge it back so 34 units exist in every year.
MERGE = {'TA': 'TT'}
# Revenue division of each educational district (the board's four divisions).
DIVISION = {
    'AN': 'Bengaluru', 'AS': 'Bengaluru', 'BA': 'Bengaluru', 'BB': 'Bengaluru', 'CA': 'Bengaluru', 'CC': 'Bengaluru',
    'DA': 'Bengaluru', 'DD': 'Bengaluru', 'IA': 'Bengaluru', 'II': 'Bengaluru', 'KK': 'Bengaluru',
    'EA': 'Mysuru', 'EE': 'Mysuru', 'FF': 'Mysuru', 'GA': 'Mysuru', 'GG': 'Mysuru', 'HH': 'Mysuru', 'JJ': 'Mysuru', 'LL': 'Mysuru',
    'MA': 'Belagavi', 'MB': 'Belagavi', 'MM': 'Belagavi', 'NA': 'Belagavi', 'NN': 'Belagavi', 'OA': 'Belagavi', 'OO': 'Belagavi',
    'PA': 'Belagavi', 'PP': 'Belagavi',
    'QA': 'Kalaburagi', 'QQ': 'Kalaburagi', 'RA': 'Kalaburagi', 'RR': 'Kalaburagi', 'SS': 'Kalaburagi', 'TT': 'Kalaburagi',
}


def read(path, **kw):
    return pd.read_csv(path, dtype={'dist_code': str, 'unit': str}, keep_default_na=False, na_values=[''], **kw)
