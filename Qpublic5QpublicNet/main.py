from basic_methods import read_spreadsheet, write_into_csv
from scrapping_methods import search_parcel_id, extract_information
from utils import seed_url

def main():
    # read csv file
    parsel_numbers_list = read_spreadsheet()
    for parsel_number in parsel_numbers_list:
        parcel_id = parsel_number.replace('\r\n', '').strip()
        #call search_parcel_id method to search details
        parcel_detail_page_url = search_parcel_id(parcel_id, seed_url)
        
        # extract details from landing page
        information_dict = extract_information(parcel_id, "".join(parcel_detail_page_url))
        #write data into csv
        write_into_csv(information_dict)

if __name__ == '__main__':
    main()