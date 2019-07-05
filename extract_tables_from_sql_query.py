def extract_tables(sql):
    sql=sql.lower()
    replace_words=['(',')','&','%','*','=','>','<','!']
    for i in replace_words:
        sql=sql.replace(i,"")
    l=sql.split()
    count=l.count("from")
    if count==0:
        return "No tables found"
    
    length=len(l)
    output=[]
    for i in range(1,length):
        if l[i-1] in ('from','join') and l[i] != 'select':
            output.append(l[i])
            
 """ below code is to handle string like 'select * from a , b ; """
 
        if l[i] == ',' and i>2 and i<length and l[i-2] == 'from' and l[i+1] != 'select':
            output.append(l[i+1])            

    return output

def main():
    s=input("Enter Sql query:")
    print(extract_tables(s))
    
if __name__=="__main__":
    main()
