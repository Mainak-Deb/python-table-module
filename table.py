import csv
import re
import numpy as np
import matplotlib.pyplot as plt

class table:
    header=dict()
    head=[]
    headlen=dict()

    data=[]
    


    
    
    def __init__(self,head,data=[]) -> None:
        self.header=dict();self.headlen=dict();self.data=[];self.head=[]
        self.head=head
        for i in range(len(head)):
            self.header[head[i]]=i
        self.data=data
        #print(head,self.header,self.data)
        self.set_headlen()
    
    def insert(self,value):
        if(len(value)!=len(self.head)):
            print("This data set can't be inserted, check the size")
            return
        else:
            self.data.append(value)

    def set_headlen(self):
        for i in self.header.keys():
            self.headlen[i]=len(i)
        if(len(self.data)>0):   
            for i in self.header.keys():
                for j in range(len(self.data)):
                    if(len(str(self.data[j][self.header[i]]))> (self.headlen[i])):
                        self.headlen[i]=len(self.data[j][self.header[i]])

    def set_primary_key(self):
        pass

    def group_by_count(self,param):
        self.order_by(param)
        head=[param,"COUNT"]
        vals=set();vallist=[]
        for i in range(len(self.data)):
            a=self.data[i][self.header[param]]
            vals.add(a)
            vallist.append(a)
        v=list(vals);v.sort()
        rows=[]
        for i in v:
            rows.append([i,str(vallist.count(i))])

        t=table(head,rows)
        return t

    def order_by(self,param):
        self.data.sort(
            key=lambda x:x[self.header[param]]
            );      

    def select(self,params):
        for i in params:
            if (i not in self.head):
                print("Row head <"+str(i)+"> is not present")
                return

        rows=[]
        for i in range(len(self.data)):
            a=[]
            for j in params:
                a.append(self.data[i][self.header[j]])
            rows.append(a)
        t=table(params,rows)
        return t
       
    def insert(self,data):
        self.data.append(data)
        pass

    def count(self,param):
        c=0
        for i in range(len(self.data)):
            if(self.data[i][self.header[param]]!=None):
                c+=1
        return c

    def sum(self,param):
        s=0
        for i in range(len(self.data)):
            if(self.data[i][self.header[param]]!=None):
                s+=float(self.data[i][self.header[param]])
        return s

    def max(self,param):
        s=-1*((2^31)-1)
        for i in range(len(self.data)):
            if(self.data[i][self.header[param]]!=None):
                if(float(self.data[i][self.header[param]])>s):
                    s=float(self.data[i][self.header[param]])
        return s

    def min(self,param):
        s=(2^31)-1
        for i in range(len(self.data)):
            if(self.data[i][self.header[param]]!=None):
                if(float(self.data[i][self.header[param]])<s):
                    s=float(self.data[i][self.header[param]])
        return s

    def avg(self,param):
        s=0;
        c=self.count(param)
        for i in range(len(self.data)):
            if(self.data[i][self.header[param]]!=None):
                s+=float(self.data[i][self.header[param]])
        return s/c

    def where(self,condition):
        yha=re.findall(r"<[^<]*>",condition)
        for i in yha:
            p=i[1:-1];p.strip()
            nw="self.data[i][self.header['"+p+"']]"
            condition=condition.replace(i,nw)
        # print(condition)
        rows=[]
        for i in range(len(self.data)):
            
            if(eval(condition)):
                rows.append(self.data[i])
        
        t=table(self.head,rows)
        return t

    def delete_where(self,condition):
        yha=re.findall(r"<[^<]*>",condition)
        for i in yha:
            p=i[1:-1];p.strip()
            nw="self.data[i][self.header['"+p+"']]"
            condition=condition.replace(i,nw)
        # print(condition)
        rows=[]
        for i in range(len(self.data)):           
            if(not eval(condition)):
                 rows.append(self.data[i])
        self.data=rows

    def self_join(self,r1,r2):
        join=join_methods()
        sj=join.cross_join([self,r1],[self,r2])
        return sj

    def pie_plot(self,key):
        if(key==None):
            print("specify the key")
            return
        elif(len(self.head)!=2):
            print("pie chart from more than two attribute can't possible")
            return
        else:
            labels=[]
            for i in range(len(self.data)):
                labels.append(self.data[i][self.header[key]])
            print(key)
            val=None
            yval=[]
            for i in self.head:
                if(i!=key):
                    val=i
                   
            try:
                for i in range(len(self.data)):
                    yval.append(float(self.data[i][self.header[val]]))
                
            except:
                print("value is not number")
                return 
            
            y=np.array(yval)
            # print(labels,yval,y)            
            plt.pie(y, labels =labels)
            plt.show() 

    
    def histogram_plot(self,key):
        if(key==None):
            print("specify the key")
            return
        elif(len(self.head)!=2):
            print("pie chart from more than two attribute can't possible")
            return
        else:
            labels=[]
            for i in range(len(self.data)):
                labels.append(self.data[i][self.header[key]])
            print(key)
            val=None
            yval=[]
            for i in self.head:
                if(i!=key):
                    val=i
                   
            try:
                for i in range(len(self.data)):
                    yval.append(float(self.data[i][self.header[val]]))
                
            except:
                print("value is not number")
                return 
            
            y=np.array(yval)
            x = np.arange(len(labels))
            width = 0.35 # the width of the bars

            fig, ax = plt.subplots()

            ax.set_ylabel(val)
            ax.set_title(key)
            ax.set_xticks(x)
            ax.set_xticklabels(labels)

                        
            pps = ax.bar(x - width/2,yval, width)
            for p in pps:
                height = p.get_height()
                ax.annotate('{}'.format(height),
                    xy=(p.get_x() + p.get_width() / 2, height),
                    xytext=(0, 3), # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
            plt.show()






    

    def print_table(self):
        self.set_headlen()
        #print(self.header,self.data ,self.headlen)
        for i in self.header.keys():
            print("_"*self.headlen[i],end="___")
        print()
        for i in self.header.keys():
            print(f"{i:^{self.headlen[i]}}",end=" | ")
        print()
        for i in self.header.keys():
            print("_"*self.headlen[i],end="___")
        print()
        for j in range(len(self.data)):
            for i in self.header.keys():
                print(f"{self.data[j][self.header[i]]:^{self.headlen[i]}}",end=" | ")
            print()

        print()




class tablecsv(table):
    def __init__(self, filepath) -> None:
        file = open(filepath)
        csvreader = csv.reader(file)
        header = next(csvreader)
        rows = []
        for row in csvreader:
            rows.append(row)
        file.close()
        super().__init__(header,rows)


class join_methods:
    def cross_join(self,in1,in2):
            r1=in1[1];r2=in2[1]
            t1=in1[0];t2=in2[0]

            new_head=[]

            for i in t1.head:
                new_head.append(str(r1)+"."+str(i))
            for i in t2.head:
                new_head.append(str(r2)+"."+str(i))

            #print(new_head)
            rows=[]
            for i in range(len(t1.data)):
                for j in range(len(t2.data)):
                    a=t1.data[i]+t2.data[j]
                    rows.append(a)

            t=table(new_head,rows)
            return t

    def natural_join(in1,in2):
        pass









join=join_methods()


