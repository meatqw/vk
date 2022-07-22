import csv  

header = ['id', 'fname', 'lname', 'phone', 'city', 'age']

def write(data, filename):
    
    with open(f'{filename}.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)
        
        # write the data
        for i in data:
            writer.writerow(i)
        
        
