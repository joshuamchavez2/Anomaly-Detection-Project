from prepare import prepare
from acquire import acquire

def wrangle():
    df = prepare(acquire())
    return df