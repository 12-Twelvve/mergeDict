data1 = [{
    'district':'kathmandu',
    'kpi1':0.8,
    },
    {
    'district':'dhanusha',
    'kpi1':0.85,
    },
    {
    'district':'Kavrepalanchowk',
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
    'district':'Kavrepalanchowk',
    'kpi2':0.6,
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
