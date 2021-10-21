from csv import DictReader

# open file in read mode
# with open('/Users/dennismiyoshi/Downloads/Weather/mpi_saale_2002b.csv', 'r') as read_obj:
with open('/Users/dennismiyoshi/Downloads/Weather/jena_climate_2009_2016.csv', 'r') as read_obj:
    # pass the file object to DictReader() to get the DictReader object
    csv_dict_reader = DictReader(read_obj)
    # get column names from a csv file
    column_names = csv_dict_reader.fieldnames
    print(column_names)
read_obj.close()

with open('/Users/dennismiyoshi/Downloads/Weather/mpi_saale_2003a.csv', 'r') as read_obj:
    csv_dict_reader = DictReader(read_obj)
    column_names_next = csv_dict_reader.fieldnames
    print(column_names_next)
read_obj.close()

if column_names == column_names_next:
    print("Headers match")
else:
    print("Headers are different")

