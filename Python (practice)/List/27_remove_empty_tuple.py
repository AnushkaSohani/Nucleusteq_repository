def remTup(tuples):
    for i in tuples:
        if i==tuple():
            tuples.remove(i)
        
    print(tuples)


tuples =[(), ('ram','15','8'), (), ('laxman', 'sita'),('krishna', 'akbar', '45'), ('',''),()]
remTup(tuples)
