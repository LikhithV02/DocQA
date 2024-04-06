import PyPDF2
import datetime
import csv
import os 
import tqdm
import random
from pdf2image import convert_from_path

csv_path = 'Database/financial_data.csv'



def process_row(j, row):
    reader = PyPDF2.PdfReader('fw2-3.pdf')
    writer = PyPDF2.PdfWriter()

    from_field_names = reader.get_form_text_fields()
    # print(from_field_names)
    # print(row)
    
    # keys = ['c2_2[0]', 'c2_3[0]', 'c2_4[0]']
    # val = random.randint(1,3)
    
    # random_keys = random.sample(keys, val)
    # for key in random_keys:
    #     from_field_names[key] = '/1'
    

    
    # empl_first_name = row['[name]'].split()[0]
    # empl_last_name = row['[name]'].split()[-1]
    # from_field_names['f2_01[0]']= str(row['[TIN_recipient]'])
    # from_field_names['f2_02[0]']= str(row['[TIN_payer]'])
    # from_field_names['f2_03[0]']= str(row['[payer_name]'] + ", " + row['[street_addr]'] + " and " + row['[zip1]'])
    # from_field_names['f2_04[0]'] = str(row['[account]'])
    # from_field_names['f2_05[0]'] = str(empl_first_name)
    # from_field_names['f2_06[0]'] = str(empl_last_name)
    # from_field_names['f2_08[0]'] = str(row['[Address]']) + ', ' + str(row['[zip2]'])
    # from_field_names['f2_09[0]'] = str(row['[od]'])
    # from_field_names['f2_10[0]'] = str(row['[q-div]'])
    # from_field_names['f2_11[0]'] = str(row['[t-cap]'])
    # from_field_names['f2_12[0]'] = str(row['[unr]'])
    # from_field_names['f2_13[0]'] = str(row['[sec-12]'])
    # from_field_names['f2_14[0]'] = str(row['[Coll]'])
    # from_field_names['f2_15[0]'] = str(row['[sec-897]'])
    # from_field_names['f2_16[0]'] = str(row['[sec-897-gain]'])
    # # from_field_names['f2_17[0]'] = str(row['[]'])
    # from_field_names['f2_18[0]'] = str(row['[fed-in]'])
    # # from_field_names['f2_19[0]'] = str(row['[]'])
    # from_field_names['f2_20[0]'] = str(row['[code_1]'])
    # from_field_names['f2_21[0]'] = str(row['[For-tax]'])
    # from_field_names['f2_22[0]'] = str(row['[code_2]'])
    # from_field_names['f2_23[0]'] = str(row['[n-cash]'])
    # from_field_names['f2_24[0]'] = str(row['[code_3]'])
    # from_field_names['f2_25[0]'] = str(row['[N-dis]'])
    # from_field_names['f2_26[0]'] = str(row['[code_4]'])
    # from_field_names['f2_27[0]'] = str(row['[Sec-199]'])
    # #from_field_names['f2_28[0]'] = str(row['[]'])
    # from_field_names['f2_29[0]'] = str(row['[state3]'])
    # from_field_names['f2_30[0]'] = str(row['[s-no]'])
    # #from_field_names['f2_31[0]'] = str(row['[]'])
    # #from_field_names['f2_32[0]'] = str(row['[]'])
    # from_field_names['f2_33[0]'] =  str(row['[inves]'])
    # #from_field_names['f2_34[0]'] = str(row['[]'])
    # from_field_names['f2_35[0]'] =  str(row['[cash-dis]'])
    # #from_field_names['f2_36[0]'] = str(row['[]'])
    # from_field_names['f2_37[0]'] =  str(row['[exem-div]'])
    # # from_field_names['f2_38[0]'] = str(row['[]'])
    # from_field_names['f2_39[0]'] = str(row['[spec]'])
    # # from_field_names['f2_40[0]'] = str(row['[]'])
    # from_field_names['f2_41[0]'] = str(row['[city1]'])
        
    empl_first_name = row['[name]'].split()[0]
    empl_last_name = row['[name]'].split()[-1]
    from_field_names['f2_01[0]']= str(['[TIN_recipient]'])
    from_field_names['f2_02[0]']= str(['[TIN_payer]'])
    from_field_names['f2_03[0]']= str(['[payer_name]']) + ", " + str(['[street_addr]']) + " and " + str(['[zip1]'])
    from_field_names['f2_04[0]'] = str(['[account]'])
    from_field_names['f2_05[0]'] = str(empl_first_name)
    from_field_names['f2_06[0]'] = str(empl_last_name)
    from_field_names['f2_08[0]'] = str(['[Address]']) + ', ' + str(['[zip2]'])
    from_field_names['f2_09[0]'] = str(['[od]'])
    from_field_names['f2_10[0]'] = str(['[q-div]'])
    from_field_names['f2_11[0]'] = str(['[t-cap]'])
    from_field_names['f2_12[0]'] = str(['[unr]'])
    from_field_names['f2_13[0]'] = str(['[sec-12]'])
    from_field_names['f2_14[0]'] = str(['[Coll]'])
    from_field_names['f2_15[0]'] = str(['[sec-897]'])
    from_field_names['f2_16[0]'] = str(['[sec-897-gain]'])
    # from_field_names['f2_17[0]'] = str(row['[]'])
    from_field_names['f2_18[0]'] = str(['[fed-in]'])
    # from_field_names['f2_19[0]'] = str(row['[]'])
    from_field_names['f2_20[0]'] = str(['[code_1]'])
    from_field_names['f2_21[0]'] = str(['[For-tax]'])
    from_field_names['f2_22[0]'] = str(['[code_2]'])
    from_field_names['f2_23[0]'] = str(['[n-cash]'])
    from_field_names['f2_24[0]'] = str(['[code_3]'])
    from_field_names['f2_25[0]'] = str(['[N-dis]'])
    from_field_names['f2_26[0]'] = str(['[code_4]'])
    from_field_names['f2_27[0]'] = str(['[Sec-199]'])
    #from_field_names['f2_28[0]'] = str(row['[]'])
    from_field_names['f2_29[0]'] = str(['[state3]'])
    from_field_names['f2_30[0]'] = str(['[s-no]'])
    #from_field_names['f2_31[0]'] = str(row['[]'])
    #from_field_names['f2_32[0]'] = str(row['[]'])
    from_field_names['f2_33[0]'] =  str(['[inves]'])
    #from_field_names['f2_34[0]'] = str(row['[]'])
    from_field_names['f2_35[0]'] =  str(['[cash-dis]'])
    #from_field_names['f2_36[0]'] = str(row['[]'])
    from_field_names['f2_37[0]'] =  str(['[exem-div]'])
    # from_field_names['f2_38[0]'] = str(row['[]'])
    from_field_names['f2_39[0]'] = str(['[spec]'])
    # from_field_names['f2_40[0]'] = str(row['[]'])
    from_field_names['f2_41[0]'] = str(['[city1]'])
    
    data = from_field_names.copy()
    # print(data)
    output_filename = f"filled_fw2-4_{j}.pdf"
    for page in range(len(reader.pages)):
        pageObj = reader.pages[page]
        for form in pageObj['/Annots']:
            field = form.get_object()
            field_name = field.get('/T')
            if field_name in data:
                try:
                    if field_name == 'c2_2[0]' or field_name == 'c2_3[0]' or field_name == 'c2_4[0]':

                        field.update({
                            PyPDF2.generic.NameObject('/V'): PyPDF2.generic.NameObject(data[field_name])
                        })
                    else:
                        # print(f"The key is {data[field_name]} and value is {type(data[field_name])}")
                        field.update({
                            PyPDF2.generic.NameObject('/V'): PyPDF2.generic.create_string_object(data[field_name])
                        })
                except Exception as e:
                    # print(e)
                    pass

        writer.add_page(pageObj)

    with open(output_filename, 'wb') as output_pdf:
        writer.write(output_pdf)


    print(f"PDF {j} form filled successfully!")

    # images = convert_from_path(output_filename, dpi=300)
    # for i, image in enumerate(images):
    #     image.save(f"output_img4/filled_fw2-4_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.jpg", "JPEG")

    # print("PDF converted to images successfully!")

with open(csv_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # output_dir = 'output_pdfs2'
        # os.makedirs(output_dir, exist_ok=True)
        for i, row in enumerate(csv_reader):
            # if i == 10:
            #     return 
            process_row(i, row)
            break
            
# for i, (key, val) in enumerate(from_field_names.items()):
#     from_field_names[key] = str(i)
# # c2_2[0]   checkbox -1 
# # c2_3[0]   checkbox -2
# # c2_4[0]   checkbox -3
# data = from_field_names.copy()
# data['c2_2[0]'] = '/1'


