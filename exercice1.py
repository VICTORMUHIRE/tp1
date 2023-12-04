
empoyer = []
print("\n")
n = int(input("entrer le nombre des employer : "))

for i in range(n):
    print("\n")
    nom = input(f'nom de l\'empoyer {i+1} : ')
    post_nom = input(f'postnom de l\'employer {i+1} : ')
    salaire = int(input(f'salaire de l\'employer {i+1} : '))

    empoyer.append([nom,post_nom,salaire])   



def affichage():
    
    sorted(empoyer, key=lambda empoyee: empoyee[2])
    print(empoyer) 
    print(f'L\'empoyer avec le salaire minimun s\'appelle {empoyer[0][0]} - {empoyer[0][1]}, il a comme salaire {empoyer[0][2]} $')
    print (f'L\'empoyer avec le salaire maximum s\'appelle {empoyer[-1][0]} - {empoyer[-1][1]}, il a comme salaire {empoyer[-1][2]} $ \n') 
     
def demande():
    avis = input("\n aficher le 1er et le dernier employer en terme de salaire? O/N : ")
    if avis == "O": 
        affichage()
demande()