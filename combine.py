import pandas as pd
import csv
"""
    
"""
def combine(csv_name_1,csv_name_2,output_name):
    data1 = pd.read_csv(csv_name_1,sep=',',engine= 'python',quoting=csv.QUOTE_NONE)
    data2 = pd.read_csv(csv_name_2,sep=',',engine= 'python',quoting=csv.QUOTE_NONE)
    result = pd.DataFrame({'email_hash':'aaaaaaaaa','category':'tank','filename':'eeee'},index=[0])

    for row in data1.iterrows():
        new1 = pd.DataFrame({'email_hash':eval(row[1]['"email_hash"']),'category':eval(row[1]['"category"']),'filename':csv_name_1},index=[0])
        result = result.append(new1,ignore_index=True)
    for row in data2.iterrows():
        new2 = pd.DataFrame({'email_hash':eval(row[1]['"email_hash"']),'category':eval(row[1]['"category"']),'filename':csv_name_2},index=[0])
        result = result.append(new2,ignore_index=True)
    result=result[1:result.size]
    result.to_csv(output_name,index=False,encoding='utf_8_sig')
if __name__ == '__main__':
    combine("accessories.csv","clothing.csv","combine.csv")