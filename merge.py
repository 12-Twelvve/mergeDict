data1 = [{
    'District':'Kathmandu',
    'KPI_1':0.8,
    },
    {
    'District':'Dhanusha',
    'KPI_1':0.85,
    },
    {
    'District':'Kavrepalanchowk',
    'KPI_1':0.75,
    },
]
data2 = [{
    'District':'Kathmandu',
    'KPI_2':0.35,
    },
    {
    'District':'Dhanusha',
    'KPI_2':0.65,
    },
    {
    'District':'Kavrepalanchowk',
    'KPI_2':0.6,
    },
]
data3 =[]
def merge(dict1, dict2):
    result = dict1 | dict2 #merge operator (|)  
    return result  
def margeData(data1, data2):
    for d1 in data1:
        for d2 in data2:
            if d1['district'] == d2['district']:
                data3.append(merge(d1, d2))
                break            
margeData(data1, data2)
print(data3)
