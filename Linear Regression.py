def Hypothesis(th,x):
    '''
    Determining the best fit line:  h(x)= transpose of theta * x
                            OR      h(x)= th_0 + th_1 * x
    '''
    return th[1]*x + th[0] 

def CostFunction(th,x,y):
    '''
    Computing net Cost: J(th_0,th_1)= (1/(2m))*Summation( squareof( h(xi)-yi ) )
    '''
    J=0
    m=len(y)
    for i in range(m):
    	cost=Hypothesis(th,x[i]) - y[i]
    	J+=(cost*cost)
    J/=(2*m)
    return J

def Gradient_Descent(x,y):
    '''
    Gradient w.r.t th_0: (d/d th_0)J= (1/m)*Summation( h(xi)-yi ))
    Gradient w.r.t th_1: (d/d th_1)J= (1/m)*Summation( (h(xi)-yi)*xi ))
    Repeat untill Convergence: th_i= th_i - alpha*gradient_i , for i=0,1
    And calculates the cost for updated th_0 and th_1.
    '''
    alpha = 0.01                                #Step size ( Learning Rate )
    m=len(y)                                    #Size of Lists x and y
    th= [1,1]                                   #Initialized th_0 and th_1
    cost_old= 0                                 #Initialized previous cost
    cost= 100000000                             #Initialized current cost
    while abs(cost - cost_old) > 0.0001 :       #Until calculated cost gets coverged to approximately the actual cost  
        cost_old= cost
        gradient= [0,0]                         #The two derivatives described above
        for i in range(m):
            gradient[0]+= Hypothesis( th,x[i] ) - y[i]
            gradient[1]+= gradient[0]*x[i]
        th[0]-= (alpha* (gradient[0]/m))
        th[1]-= (alpha* (gradient[1]/m))
        cost=CostFunction(th,x,y)
    return th[0], th[1], cost

print "Specify the different x coordinates\n"
x=list(map(int, raw_input().split()))
print "Specify the corresponding y coordinates\n"
y=list(map(int, raw_input().split()))


result=Gradient_Descent(x,y)                    #Stores the 3 returned required values

print "th_0= " + str(result[0])                      
print "th_1= " + str(result[1])
print "cost= " + str(result[2])
