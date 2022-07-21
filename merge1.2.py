data1 = [{
    'district':'kathmandu',
    'kpi1':0.8,
    },
    {
    'district':'dhanusa',
    'kpi1':0.85,
    },
    {
    'district':'kavre palanchowk',
    'kpi1':0.75,
    },
]
data2 = [{
    'district':'kathmandu',
    'kpi2':0.35,
    },
    {
    'district':'dhanusha',
    'kpi2':0.65,
    },
    {
    'district':'kavre',
    'kpi2':0.6,
    },
]
data3 =[]
def merge(dict1, dict2):
    result = dict1 | dict2 #merge operator (|)  
    return result 

# assuming the data can have this variety of name already known data
districtName ={
    'kathmandu':['ktm', "kathmandu"],
    'dhanusha':['dhanusha', 'dhanusa'],
    'kavrepalanchwok':['kavrepalanchowk', 'kavre palanchowk', 'kavre']
}

def margeData(data1, data2):
    for d1 in data1:
        for d2 in data2:
            for key, val in districtName.items():
                if d1['district'] in val and d2['district'] in val:
                    data3.append(merge(d1, d2))
                    break
                
margeData(data1, data2)
print(data3)
# for fuzzy word
# using fuzzywuzzy 
# from fuzzywuzzy import process
# from fuzzywuzzy import fuzz
