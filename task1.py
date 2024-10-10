names = [
    ['alice','Bob','Charlie'],
    ['David','Eve','Frank'],
    ['Grace','Heidi','Ivan'],
    ['Judy','Ken','Laura']
]   
alice_found = True

for sublist in names:
    if 'alice' in sublist:
        sublist.remove("alice")
        alice_found = False
        
    
if not alice_found:
    new_name = input("alice is automatically removed from the array. Please enter a new name to fill the array:")
    names[0].append(new_name)
    
print(names)

for list in names:
    for name in list:
        print(name)