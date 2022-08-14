a = 5

for i in range(0,a):
    for j in range(0,a-i-1):
        print(end=" ")
        
    for k in range(0, i+1):
        print("* ",end='')
        
    print()
    
# -------------the reverse--------------------

for i in range(a-1,0,-1):
    for j in range(0,a-i):
        print(end=" ")
    for k in range(0,i):
        print("* ",end='')
    print()

    
    
    
#       *
#      * *
#     * * *
#    * * * *
#   * * * * *
#    * * * *
#     * * *
#      * *
#       *
