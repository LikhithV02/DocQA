import json 
import pandas as pd

df = pd.read_csv("./financial_data.csv")

# def group_header(obj):
#     res_obj = {
#       "companyName": obj["companyName"],
#       "coId" :obj["coId"],
#       "accountNo": obj["accountNo"],
#       "formName":obj["formName"],
#       "year":obj["year"],
#       "payersInfo":obj["payersInfo"],
#       "recipientsInfo":obj["recipientsInfo"]
#     }
#     del obj
    # del obj["Company"]
    # del obj["Co.ID"]
    # del obj["Account number (see instructions)"]
    # del obj["Form"]
    # del obj["For calendar year"]
    # del obj["(Rev."]
    # del obj["PAYER\u2019S name, street address, city or town, state or province, country, ZIP or 1a Total ordinary dividends foreign postal code, and telephone no."]
    # del obj["RECIPIENT\u2019S name, street address, city or town, state or province, country, ZIP or 1a Total ordinary dividends foreign postal code, and telephone no."]
    
    # return res_obj

with open("./final_train.json", 'r') as f:
    data1= json.load(f)
with open("./bounding_boxes1.json", 'r') as f:
    data = json.load(f)
key = {"header":{}, "payers_data": {}, "recipients_data":{}, "items":{}, "boxes":{}}
for i, (doc, items) in enumerate(data1.items()):
    # print(doc)
    # header
    key['header']['company_name']=df['company_name'][i]
    key['header']['coId']=df['coid'][i]
    key['header']['Accoung number (see instructions}']=df['rec_acc'][i]
    key['header']['Form']="1099-DIV"
    key['header']['For calendar year']=int(df['caledar_year'][i])
    # key['header']['payersInfo']=df['payers_name'][i]+", "+df['payers_add'][i]+", "+df['payers_city'][i]+", "+df['payers_state'][i]+", "+df['payers_cont'][i]+", "+str(df['payers_zip'][i])+", "+str(df['payers_phn_no'][i])
    # key['header']['recipientsInfo']=df['recipient_name'][i]+", "+df['rec_street'][i]+", "+df['rec_cit'][i]+", "+df['rec_stat'][i]+", "+df['rec_cont'][i]+", "+str(df['rec_zip'][i])

    # payers data
    key['payers_data']["PAYER'S name, Street address, city or [OWI, Stale province, country, ZIP or foreign postal code; and telephone no_"] = df['payers_name'][i]+", "+df['payers_add'][i]+", "+df['payers_city'][i]+", "+df['payers_state'][i]+", "+df['payers_cont'][i]+", "+str(df['payers_zip'][i])+", "+str(df['payers_phn_no'][i])

    # recipients data
    key['recipients_data']["RECIPIENT'S name"] = df['recipient_name'][i]
    key['recipients_data']["Street address (including apt: no.)"] = df['rec_street'][i]
    key['recipients_data']["City or town, state Or province; country, and ZIP or foreign postal code"] = df['rec_cit'][i]+", "+df['rec_stat'][i]+", "+df['rec_cont'][i]+", "+str(df['rec_zip'][i])

    # items
    key['items']['PAYERS TIN'] = df['payers_tin'][i]
    key['items']['RECIPIENTS TIN'] = df['recipients_tin'][i]
    key['items']['1a Total ordinary dividends'] = "$ "+str(df['one_a'][i])
    key['items']['1b Qualified dividends'] = "$ "+str(df['one_b'][i])
    key['items']['2a Total capital gain distr:'] = "$ "+str(df['two_a'][i])
    key['items']['2c Section 1202 gain'] = "$ "+str(df['two_c'][i])
    key['items']['2e Section 897 ordinary dividends'] = "$ "+str(df['two_e'][i])
    key['items']['3 Nondividend distributions'] = "$ "+str(df['three'][i])
    key['items']['5 Section 199A dividends'] = "$ "+str(df['five'][i])
    key['items']['7 Foreign tax paid'] = "$ "+str(df['seven'][i])
    key['items']['9 Cash liquidation distributions'] = "$ "+str(df['nine'][i])
    key['items']['12 Exempt-interest dividends'] = "$ "+str(df['twle'][i])
    key['items']['15 State identification no.'] = df['fiften'][i]
    key['items']['14 State'] = df['forten'][i]
    key['items']['OMB No.'] = "1545-0110"
    key['items']['(Rev.'] = "January 2024)"
    key['items']['2d Collectibles (28%) gain'] = "$ "+str(df['two_d'][i])
    key['items']['2f Section 897 capital gain'] = "$ "+str(df['two_f'][i])
    key['items']['4 Federal income tax withheld'] = "$ "+str(df['four'][i])
    key['items']['6 Investment expenses'] = "$ "+str(df['six'][i])
    key['items']['8 Foreign country or U.S. possession'] = df['eight'][i]
    key['items']['10 Noncash liquidation distributions'] = "$ "+str(df['ten'][i])
    key['items']['13 Specified private activity bond interest dividends'] = "$ "+str(df['trten'][i])
    key['items']['2b Unrecap. Sec: 1250 gain'] = "$ "+str(df['two_b'][i])
    key['items']['16 State tax withheld'] = "$ "+str(df['sixten'][i])
    key['items']['11 FATCA filing requirement'] = ""
    
    # boxes
    key['boxes']['company_name'] = data['companyName'][1]['coordinates']
    key['boxes']['coId'] = data['coId'][1]['coordinates']
    key['boxes']['Accoung number (see instructions}'] = data['recipientsAccNo'][1]['coordinates']
    key['boxes']['Form'] = data['form'][1]['coordinates']
    key['boxes']['For calendar year'] = data['FY'][1]['coordinates']
    key['boxes']["PAYER'S name, Street address, city or [OWI, Stale province, country, ZIP or foreign postal code; and telephone no_"] = data['payersData'][1]['coordinates']
    key['boxes']["RECIPIENT'S name"] = data['recipientsName'][1]['coordinates']
    key['boxes']["Street address (including apt: no.)"] = data['recipientsStreetAddress'][1]['coordinates']
    key['boxes']["City or town, state Or province; country, and ZIP or foreign postal code"] = data['recipientsAddress'][1]['coordinates']
    key['boxes']['PAYERS TIN'] = data['payersTin'][1]['coordinates']
    key['boxes']['RECIPIENTS TIN'] = data['recipientsTin'][1]['coordinates']
    key['boxes']['1a Total ordinary dividends'] = data['totalOrdinaryDividents'][1]['coordinates']
    key['boxes']['1b Qualified dividends'] = data['qualifiedDividends'][1]['coordinates']
    key['boxes']['2a Total capital gain distr:'] = data['totalCapitalGain'][1]['coordinates']
    key['boxes']['2c Section 1202 gain'] = data['section1202Gain'][1]['coordinates']
    key['boxes']['2e Section 897 ordinary dividends'] = data['section897Ordinary'][1]['coordinates']
    key['boxes']['3 Nondividend distributions'] = data['nondividendDistributions'][1]['coordinates']
    key['boxes']['5 Section 199A dividends'] = data['section199ADividends'][1]['coordinates']
    key['boxes']['7 Foreign tax paid'] = data['foreignTaxPaid'][1]['coordinates']
    key['boxes']['9 Cash liquidation distributions'] = data['cashLiquidationDistributions'][1]['coordinates']
    key['boxes']['12 Exempt-interest dividends'] = data['exemptinterestDividends'][1]['coordinates']
    key['boxes']['15 State identification no.'] = data['stateIdNo'][1]['coordinates']
    key['boxes']['14 State'] = data['state'][1]['coordinates']
    key['boxes']['OMB No.'] = data['ombNo'][1]['coordinates']
    key['boxes']['(Rev.'] = data['revDate'][1]['coordinates']
    key['boxes']['2d Collectibles (28%) gain'] = data['collectibles'][1]['coordinates']
    key['boxes']['2f Section 897 capital gain'] = data['section897Capital'][1]['coordinates']
    key['boxes']['4 Federal income tax withheld'] = data['federalIncomeTax'][1]['coordinates']
    key['boxes']['6 Investment expenses'] = data['investmentExpenses'][1]['coordinates']
    key['boxes']['8 Foreign country or U.S. possession'] = data['foreignOrUS'][1]['coordinates']
    key['boxes']['10 Noncash liquidation distributions'] = data['noncashLiquidationDistributions'][1]['coordinates']
    key['boxes']['13 Specified private activity bond interest dividends'] = data['specifiedPrivateActivityBondInterestDividends'][1]['coordinates']
    key['boxes']['2b Unrecap. Sec: 1250 gain'] = data['unrecapSec1250Gain'][1]['coordinates']
    key['boxes']['16 State tax withheld'] = data['statetaxWithheld'][1]['coordinates']
    key['boxes']['11 FATCA filing requirement'] = data['FATCAFilingRequirement'][1]['coordinates']

    file = "0001"
    if i<9:
        file = f"000{i+1}"
    elif i<99 and i>8:
        file = f"00{i+1}"
    elif i>98 and i<999:
        file = f"0{i+1}"
    else:
        file = "1000"
    with open(f"./key/{file}.json", "w") as f:
        json.dump(key, f, indent=4)
        print(file)
    #     break
    # break
    # print(key['header']['recipientsInfo'])
    # for i, (key_first, value_first) in enumerate(data.items()):
    #     js = {}
    #     print(key_first)
    #     for filed_first in value_first:   
    #         print(filed_first) 
    #         for key_sec,value_sec in filed_first.items():
    #             print(key_sec, value_sec)
    #             key = None
    #             text = None
    #             for field_sec in value_sec:
    #                 print(field_sec)
    #                 for key_third ,value_third in field_sec.items():
    #                     # print(value_third)
                        
    #                     if key_third == "text" and key is  None:
    #                         key = value_third
    #                     elif key_third == "text" and key is not None:
    #                         text = value_third
                
    #             if key == text and key_sec == 'recipientsAddress':
    #                 key = 'City or town, state or province, country, and ZIP or foreign postalcode'
    #             elif key != text and key_sec == 'recipientsAddress':
    #                 key = 'City or town, state or province, country, and ZIP or foreign postalcode'
    #             elif key == text and key_sec == "companyName":
    #                 key = 'Company'
    #             js[key] = text
    #         break
        
    #     recipients_data = js["recipientsName"] + ", "+js["Street address (including apt. no.)"] +", "+ js["City or town, state or province, country, and ZIP or foreign postalcode"]
    #     del js["RECIPIENT\u2019S name"]
    #     del js["Street address (including apt. no.)"]
    #     del js["City or town, state or province, country, and ZIP or foreign postalcode"]
    #     js[ "RECIPIENT\u2019S name, street address, city or town, state or province, country, ZIP or 1a Total ordinary dividends foreign postal code, and telephone no."] = recipients_data
    #     js2 ={}
    #     js2["Header"] = group_header(js)
    #     js2["Items"] = js
    # with open(f"./key/000{i+1}.json", "w") as f:
    #         json.dump(key, f, indent=2)          
    
                
               
