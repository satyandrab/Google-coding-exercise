import csv

def return_max():
    #open csv file
    f = open("sharing_price.csv", "rb")
    csv_reader = csv.reader(f)
    
    #create list of header values
    header = csv_reader.next()
    
    # create a dict corresponding for each header ignoring first one, as its 'year' so not required.
    complete_data = {}
    for i in range(2, len(header)):
        complete_data[header[i]] = {}
    
    # read csv line by line, mentioning key as "Year month" and share price as values
    for r in csv_reader:
        values = r
        
        for i in range(2, len(values)):
            complete_data[header[i]][r[0]+" "+r[1]] = values[i]
            
    # find max values for each company and compare it mont year wise
    max_values ={}
    for key, values in complete_data.iteritems():
        max_value = max(values.iterkeys(), key= (lambda key: int(values[key])))
        max_values[key] = max_value
     
    return max_values

if __name__ == "__main__":
    print return_max()
