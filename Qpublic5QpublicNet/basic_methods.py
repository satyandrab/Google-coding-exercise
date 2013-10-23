import csv
output = open("Output.csv", "wb")
csv_writer = csv.writer(output)
csv_writer.writerow(["url",
                     'Parcel Id',
                     'Owner Name',
                     'Today\'s Date',
                     'Mailing Address',
                     'Account Number',
                     'Location Address',
                     'Account Type',
                     'Extension',
                     'Subdivision',
                     'Tax District',
                     'Property Type',
                     'Business Name',
                     'Acres',
                     'LEA Code',
                     'Lot',
                     'Parcel Map',
                     'Zoning'])


def read_spreadsheet():
    """
    Method to read parcel id csv file, return all parcel id as list 
    """
    read_csv = open('parcel_number.csv', 'rb')
    return read_csv.readlines()

def write_into_csv(data_dict):
    """
    Get data as dict, format it, and write data into csv.  
    """
    data_list = []
    if data_dict.has_key('url'):
        data_list.append(data_dict['url'])
    if data_dict.has_key('parcel_id'):
        data_list.append(data_dict['parcel_id'])
    if data_dict.has_key('Owner Name(s)'):
        data_list.append(data_dict['Owner Name(s)'].replace('&nbsp;<BR>', ''))
    if data_dict.has_key("Today's Date"):
        data_list.append(data_dict["Today's Date"])
    if data_dict.has_key("Mailing Address"):
        data_list.append(data_dict["Mailing Address"])
    if data_dict.has_key("Account Number"):
        data_list.append(data_dict["Account Number"].replace('&nbsp;', ''))
    if data_dict.has_key("Location Address"):
        data_list.append(data_dict["Location Address"])
    if data_dict.has_key("Account Type"):
        data_list.append(data_dict["Account Type"])
    if data_dict.has_key("Extension"):
        data_list.append(data_dict["Extension"])
    if data_dict.has_key("Subdivision"):
        data_list.append(data_dict["Subdivision"])
    if data_dict.has_key("Tax District"):
        data_list.append(data_dict["Tax District"])
    if data_dict.has_key("Property Type"):
        data_list.append(data_dict["Property Type"])
    if data_dict.has_key("Business Name"):
        data_list.append(data_dict["Business Name"])
    if data_dict.has_key("Acres"):
        data_list.append(data_dict["Acres"])
    if data_dict.has_key("LEA Code"):
        data_list.append(data_dict["LEA Code"])
    if data_dict.has_key("Lot"):
        data_list.append(data_dict["Lot"])
    if data_dict.has_key("Parcel Map"):
        data_list.append(data_dict["Parcel Map"].split('"')[1])
    if data_dict.has_key("Zoning"):
        data_list.append(data_dict["Zoning"])
#        
    csv_writer.writerow(data_list)