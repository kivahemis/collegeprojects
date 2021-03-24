def sorting(dats):
    for passnum in range(len(dats)-1, 0, -1):
        for i in range(passnum):
            if dats[i]['year'] > dats[i+1]['year']:
                temp = dats[i]['year']
                dats[i]['year'] = dats[i+1]['year']
                dats[i+1]['year'] = temp

                temp = dats[i]['month']
                dats[i]['month'] = dats[i + 1]['month']
                dats[i + 1]['month'] = temp

                temp = dats[i]['day']
                dats[i]['day'] = dats[i + 1]['day']
                dats[i + 1]['day'] = temp

            if dats[i]['year'] == dats[i+1]['year']:
                   if dats[i]['month'] > dats[i + 1]['month']:
                     temp = dats[i]['month']
                     dats[i]['month'] = dats[i + 1]['month']
                     dats[i + 1]['month'] = temp

                     temp = dats[i]['day']
                     dats[i]['day'] = dats[i + 1]['day']
                     dats[i + 1]['day'] = temp

            if dats[i]['month'] == dats[i+1]['month']:
                   if dats[i]['day'] > dats[i + 1]['day']:
                          temp = dats[i]['day']
                          dats[i]['day'] = dats[i + 1]['day']
                          dats[i + 1]['day'] = temp

dats = [{'year': 1996, 'month': 2, 'day': 27},
        {'year': 1991, 'month': 11, 'day': 1},
        {'year': 1900, 'month': 13, 'day': 12},
        {'year': 1934, 'month': 1, 'day': 11},
        {'year':  1828, 'month': 3, 'day': 2},
        {'year': 1222, 'month': 13, 'day': 22}]
sorting(dats)

for i in dats:
    print(i)

#Sortowanie dat w słowniku list. Uwzględnione są sytuacje jednakowych wartości.