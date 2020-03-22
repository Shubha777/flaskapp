
"file:///E:/StudentStrength_UG_EvenSem_2019-2020.pdf"





def maine(name):
       import difflib
       def searche(namestack, search):
            searchresults = difflib.get_close_matches(search, namestack)
            return searchresults

       def keyfinder(searchresults, dic):
            string=''
            for j in searchresults:
                i=dic.get(j)
                sem=i[0]
                enroll=i[1]
                reg=i[2]
                sec=i[4]
                bud="Name: "+ j +"  >>  "+ "Semseter: "+ sem + " Enrollment Number: " + enroll + " Registration Number: "+reg+" Section "+sec
                string=string+ '\n'+ bud
            return string

       d = {}
       namestack=[]
       import csv
       with open('output.csv', newline='') as f:
              reader = csv.reader(f)
              for row in reader:
                d[(row[4])] = [row[1],row[2],row[3],row[5],row[7]]
                namestack.append(row[4])


       name=name.upper()
       results=searche(namestack,name)
       lis=keyfinder(results,d)
       return lis

print(maine('Annesha'))

