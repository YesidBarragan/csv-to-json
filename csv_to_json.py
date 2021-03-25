import json
import csv

with open("csv_file.csv", "r") as f:
    
    cont = 0;
    path = 0;
    path2 = 0;
    reader = csv.reader(f)
    next(reader)
    data = {"Labels": []}
    for row in reader:

        if path and path2 == 0:
            path = row[1].split("_")[4];
            path2 = path;
        else:
            path = row[1].split("_")[4];

        if path != path2 and path != 0:
            cont += 1;
            path2 = path;
        
        data["Labels"].append({"ID": cont,
                            "Type": row[0],
                            "path": row[1],
                            "label type": row[2],
                            "label": (row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])})

with open("json_file.json", "w") as f:
    json.dump(data, f, indent=4)