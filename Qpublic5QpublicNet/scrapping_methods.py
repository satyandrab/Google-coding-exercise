import mechanize_i
import re
br = mechanize_i.Browser()

# Cookie Jar
cj = mechanize_i._lwpcookiejar.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize_i._http.HTTPRefreshProcessor(), max_time=1)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def search_parcel_id(parcel_id, url):
    """
    This method is responsible for searching parcel id on the page and return landing page url, i am just using try except and pass here for different kind of errors
    it can be further improved.
    """
    try:
        html_response = br.open(url)
        html_source = html_response.read()
        br.select_form(nr=0)
    
        br.form['INPUT'] = parcel_id
        req = br.submit().read()
        
        get_parcel_detail_url = re.findall(r'<a href="(http://qpublic5.qpublic.net/sc_pickens_display.php\?account=.*?KEY=.*?)">.*?</a>', req)
        return get_parcel_detail_url
    except:
        pass

def extract_information(parcel_id, url):
    """
    After getting the landing page url extract all the information from the html and return dict format for further processing
    """
    data_dict = {}
    html_response = br.open(url)
    html_source = html_response.read().replace('\n', '').replace('\r', '')
    
    # Details page url
    data_dict['url'] = url
    
    #Parcel id
    data_dict['parcel_id'] = parcel_id
    
    # Owner name
    data_tds = re.findall(r'<td class="owner_header".*?>.*?<td class="owner_value">.*?</td>', html_source)
    for tds in data_tds:
        if '<font color="#000080">' not in tds:
            address_remaining_part = re.findall(r'<td class="owner_value">&nbsp;(.*?)&nbsp;</td>', tds)
            address_2 = address_remaining_part[0]
        else:
            data_value_tuple = re.findall(r'<td class="owner_header".*?>.*?<font color="#000080">(.*?)</font>.*?</td><td class="owner_value">&nbsp;(.*?)&nbsp;</td>', tds)
            if len(data_value_tuple) > 0:
                key = data_value_tuple[0][0].strip()
                value = data_value_tuple[0][1].strip()
                data_dict[key] = value
    if data_dict.has_key('Mailing Address'):
        mailing_address = data_dict['Mailing Address']
        complete_mailing_address = str(mailing_address)+' '+str(address_2)
        data_dict['Mailing Address'] = complete_mailing_address
            
    return data_dict
    