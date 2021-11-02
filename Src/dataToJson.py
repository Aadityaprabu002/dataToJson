import json
listofTables = []
separator = input('Enter the separator:')
with open('../queries/from.txt','r') as f:
    line = f.readline()
    listofData = []
    columns = []
    while line:
        if line != '\n' and line[0:4]!= '#end':
            if columns == []:
                columns = line.split(sep = separator) 
                columns = [i.strip() for i in columns]
                line = f.readline()
                while line =='\n':
                    line = f.readline() 

            rowData = line.split(sep = separator)  
            rowData = [i.strip() for i in rowData] 
        
            jsonObj = dict(zip(columns,rowData))
            listofData.append(jsonObj)   
            
        if line[0:4] == '#end':
            
   
            with open('../queries/queries.txt','a+') as q:
                query = '''
                    INSERT INTO TABLE_NAME
                    VALUES
                '''
                q.write(query)
                dataLen = len(listofData)
                c = 0
                for data in listofData:
                    values = ''
                    for k,v in data.items():
                        values += v+','
                    if(c == dataLen-1):
                        q.write('('+values[0:len(values)-1]+');')
                    else:    
                        q.write('('+values[0:len(values)-1]+'),\n') 
                    c+=1

            listofTables.append(listofData)    
            listofData = []
            columns = []

        line = f.readline()
      

with open('../queries/to.json','w') as f:
    json.dump(listofTables,f)




        
    



 