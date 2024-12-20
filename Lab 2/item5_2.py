import json
import re

def update_records(dictionary_record, id, property, value):
    try:
        new_record = eval(dictionary_record.replace("'", "\""))
    except:
        return "Invalid"

    new_record = eval(dictionary_record.replace("'", "\""))



    id = id.replace(" ", "")
    property = property.strip()
    value = value.strip()

    if int(id) <= 0:
        return "Invalid"

    if id not in new_record.keys():
        new_record[id] = {}


    if property in new_record[id] and property == "tracks":
        new_record[id][property].append(value)
    else:
        if property not in new_record[id] and property == "tracks":
            value = re.split('\" |, ', value)
        elif property not in new_record[id] and value == "\'\'":
            return "Invalid"
        new_record[id][property] = value

    if value == "\'\'" and property in new_record[id]:
        new_record[id].pop(property)
        
    property_check=["albumTitle","artist","tracks"]
    if property not in property_check:
        return "Invalid"

    return(new_record)
value= input()
value =[str(e) for e in value.split("|")]
output = update_records(dictionary_record=value[0], id=value[1], property=value[2], value=value[3])
print(output)