from re import T


class Personne:
    def __init__(self,nom,age):
        self.nom=nom
        self.age=age
    def demander_nom_and_age(self):
        print('bonjour je m appelle ',self.nom,'jai: ',self.age,' ans')
        print('estmajeur:',self.estmajeur()) 
        if self.estmajeur():
            print("je suis majeur")
        else:
            print('je suis mineur')    
    def estmajeur(self):   
        if self.age>=18:
            return True
        return False
personne1=Personne('paul',15)
personne2=Personne('jean',30)
personne1.demander_nom_and_age()
personne2.demander_nom_and_age()
# print('estmajeur1: ',personne1.estmajeur())
# print('estmajeur2:',personne2.estmajeur())


