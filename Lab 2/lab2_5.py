import json
def update_records(value):
    new_value = ""
    for i in range(len(value)):
        # Append all characters, including spaces
        if value[i] == ' ':
            # Only keep the space if it's between two alphabetic characters
            if i > 0 and i < len(value) - 1 and value[i-1].isalpha() and value[i+1].isalpha():
                new_value += value[i]
        else:
            new_value += value[i]

    value = new_value
    
    try:
        # Split value into dictionary_record, id1, property1, and value1
        dictionary_record, id1, property1, value1 = value.split("|")
        if(value1 == "''"):
           value1 = ''
        
    except ValueError:
        print("Error: Input does not contain the expected number of parts.")
        return None

    # dictionary_record = [i for i in dictionary_record if i != ' ']
    # dictionary_record = "".join(dictionary_record)
    dic = {}
    record_collection = {}
    dictionary_record = dictionary_record[1:-1]
    id_in,to_dic = dictionary_record.split(":",1)
    #record_collection = json.loads(to_dic)  
    #dictionary_record = dictionary_record.split(":")
    #if(property1 == "Track"):
    try:
        # Parse the JSON string in to_dic
        to_dic = to_dic.replace("'",'"')
        record_collection = json.loads(to_dic)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the dictionary.")
        return None
    
    
    if(property1 == 'tracks'):
        if 'tracks' in record_collection:
            record_collection['tracks'].append(value1.strip()) #ต่อเพิ่ม
        else:    
            record_collection['tracks'] = [value1.strip()] #เพิ่ม list
    elif property1 != '' and value1.strip() != '':
        record_collection[property1] = value1.strip()   
    elif property1.strip() != '' and value1.strip() == '':
        if property1.strip() in record_collection:
         del record_collection[property1.strip()]

 
    new_dict = {id1.strip(): record_collection}
    
    


    
    return new_dict

# def jesus(first):
#     first1 = [i for i in first if i != "{" and i != "}"]
#     first1 = "".join(first1)
    

#     return first1
    
try:
    value = input()
    
    output = update_records(value)
    print(output)
except:
    print("Invalid")