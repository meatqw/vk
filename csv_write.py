import csv  

header = ['id', 'fname', 'lname', 'phone', 'city']

def write(data):
    with open('data.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write the data
        writer.writerow(data)
