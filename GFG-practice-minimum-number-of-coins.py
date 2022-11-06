def minPartition(self, N):
        # code here
        
        #let N=300
        
        notes =  [1,2,5,10,20,50,100,200,500,2000]
        r = []
        while N:    #till the N is true
            
            #pops the number which is greater than N
            
            if notes[-1]>N:
                notes.pop() 
            
        #so the remains are [1,2,5,10,20,50,100,200] and the rest are greater so popped
        
            else:
                #so the last element according to new list is 200
                
                N =  N-notes[-1]    #300-200 and that leaves 100
                
                r.append(notes[-1]) #now the r is [200]
                
                #since the N is still true with the value 100
                # so the above process repeats and append the element we get [200,100]
                
        return r
      
      
#       //OUTPUT
#       >>300
#       200 100
