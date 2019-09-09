import csv
temp_data =[]
locations_processed = []
with open('new_records.csv', "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        with open('shipwreck.txt',"rb") as original_data:
            for line in original_data:
                columns = line.split("	")
                # print(columns[0])
                location = columns[0]
                lat = columns[1]
                long = columns[2]
                if location not in locations_processed:
                    data_object = []
                    data_object.append(location)
                    locations_processed.append(location)
                    data_object.append(lat)
                    data_object.append(long)
                    temp_data.append(data_object)
            # print(temp_data)
        for line in temp_data:
            writer.writerow(line)
