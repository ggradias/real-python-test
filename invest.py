import pdb

def invest(amount,rate,time):
    print('Principal amount: $',amount)
    print('annual rate of return:',rate) 
    total = amount
    for anio in range(1,time+1):
        total = total + (total*rate)
        import pdb; pdb.set_trace()  # breakpoint 4975ae2c //
        print("año ",anio,":",total)

    print("fin de la corrida")



invest (100,0.05,8)



