import csv

with open('input.csv', newline='', encoding='utf-8-sig') as r, open('output.csv', 'w', newline='', encoding='utf-8') as w:
    reader = csv.reader(r)  # Input csv file
    writer = csv.writer(w)  # Output csv file

    # Remove the blank rows:
    output = [] # Output with blank rows removed
    # Remove the blank rows by writing only rows that are not blank to output:
    for row in reader:
        # print(row)
        if all('' == s or s.isspace() for s in row):
            # print('true')
            pass
        else:   # If the row is not entirely empty:
            # print('false')
            output.append(row) # Append it to output

    # print('')
    # for row in output:
    #     print(row)

    # Find the indices of the blank columns:
    blankColumns = []   # The indices of the blank columns
    allBlank = True     # Variable used to keep track of which columns are entirely blank
    for i in range(0, len(output[0])):  # Loop through all the columns:
        for j in range(0, len(output)): # Loop through each row to check each item of the current column:
            # print('row: ' + str(j) + '\tcolumn: ' + str(i) + "\tcurrent item: " + output[j][i])
            if not (output[j][i] == '' or output[j][i].isspace()):  # If any character is not a blank or a whitespace:
                allBlank = False
        if allBlank:                # If the column is entirely blank:
            blankColumns.append(i)  # Append the index of the column to blankColumns
        else:
            # print('allBlank = False')
            allBlank = True # Reset allBlank back to True

    # print(blankColumns)

    # Find the indices of the columns that are not blank:
    nonBlankIndices = range(0, len(output[0]))
    nonBlankIndices = [x for x in nonBlankIndices if x not in blankColumns]

    # print(nonBlankIndices)

    # Remove the blank columns by writing only columns that are not blank to finalOutput:
    finalOutput = []
    for row in output:
        finalRow = []
        for i in nonBlankIndices:
            finalRow.append(row[i])
        finalOutput.append(finalRow)

    # Write to the file output.csv:
    for row in finalOutput:
        # print(row)
        writer.writerow(row)

    w.close()
