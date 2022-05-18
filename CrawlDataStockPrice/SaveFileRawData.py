import os.path
import pandas as pd
def SaveFileDataCSV(filename, data):
        list_dataframe = pd.DataFrame.from_dict(data)
        filepath = r"C:\Users\khang\Desktop\CrawlDataStockPrice\CrawlDataStockPrice\datas\csv"
        filename = os.path.join(filepath, filename)
        filedata = filename
        with open(filedata, 'a', encoding='utf-8') as f:
                    list_dataframe.to_csv(f, mode='a', header=f.tell()==0)
            