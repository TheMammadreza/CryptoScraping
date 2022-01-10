from typing import Any, NoReturn
import pandas as pd
from pandas.core.frame import DataFrame

class CoinMarketCap:
    def __init__(self, url) -> None:
        self.__data = None
        self.url = url
        
        self.refreshData()

    def refreshData(self) -> NoReturn:
        self.__data = pd.read_html(self.url)
    
    def getCount(self) -> int:
        return len(self.__data)
    
    def getData(self, idx=0) -> DataFrame:
        df = self.__data[idx]
        df = df.set_index([0])
        df = df.rename(columns={df.columns[0]: 'Value'})
        df.index.names = ['Key']

        return df
    
    def showAllData(self) -> NoReturn:
        for idx in range(self.getCount()):
            print(f"______________________________(index {idx})______________________________")
            print(self.getData(idx))

    def getValue(self, key, idx=0) -> Any:
        df = self.getData(idx)
        key = [index for index in df.index if key in index]

        if len(key) > 0:
            if key[0] in df.index:
                return self.getData(idx).loc[key[0], 'Value']
        else:
            return None
    

# How to use
bitcoin = CoinMarketCap("https://coinmarketcap.com/currencies/bitcoin/")
print(bitcoin.getData())
print(f"\nCurrent Bitcoin price is {bitcoin.getValue('Price')}")