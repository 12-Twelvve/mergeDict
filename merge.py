data1 = [{
    'District':'Kathmandu',
    'KPI_1':.8,
    },
    {
    'District':'Dhanusha',
    'KPI_1':.85,
    },
    {
    'District':'Kavrepalanchowk',
    'KPI_1':.75,
    },
]
data2 = [{
    'District':'Kathmandu',
    'KPI_2':.35,
    },
    {
    'District':'Dhanusha',
    'KPI_2':.65,
    },
    {
    'District':'Kavrepalanchowk',
    'KPI_2':.6,
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
