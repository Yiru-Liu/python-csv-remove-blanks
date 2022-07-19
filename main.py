import csv

with open('test dummy.csv', newline='', encoding='utf-8-sig') as r, open('removed.csv', 'w', newline='') as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    output = []
    for row in reader:
        print(row)
        if all('' == s or s.isspace() for s in row):
            print('true')
        else:
            print('false')
            output.append(row)

    print('')
    for row in output:
        print(row)

    blankColumns = []
    allBlank = True
    for i in range(0, len(output[0])):
        for j in range(0, len(output)):
            # print('row: ' + str(j) + '\tcolumn: ' + str(i) + "\tcurrent item: " + output[j][i])
            if not (output[j][i] == '' or output[j][i].isspace()):
                allBlank = False
        if allBlank:
            blankColumns.append(i)
        else:
            # print('allBlank = False')
            allBlank = True

    print(blankColumns)

    nonBlankIndices = range(0, len(output[0]))
    nonBlankIndices = [x for x in nonBlankIndices if x not in blankColumns]

    print(nonBlankIndices)

    finalOutput = []
    for row in output:
        finalRow = []
        for i in nonBlankIndices:
            finalRow.append(row[i])
        finalOutput.append(finalRow)

    for row in finalOutput:
        print(row)
        writer.writerow(row)


    w.close()