
#exp
print("hhhh") ;print("hhhhi")
print("hhh",end=" ");print("heheh")

#                              listes
#ex 
l=[1,2,3]
for i in range(len(l)):
  if l[i]%2 !=0:
    l[i]+=1
print(l)
#autre methode
l=[1,2,3]
l=[e+e%2 for e in l  ]
print(l)

#EX1
l=eval(input("entrer une liste 1,"))
l2= [e for e in l if e%2 !=0]
l1= [e for e in l if e%2 == 0]
print(l1)
print(l2)

#ex2
#l=["b","o","n","j","o","u","r"]
l=eval(input("dnner chaine "))
l=[e for e in l if e not in["o","i","y","e","a","u"]]
print(l)

#ex3
l1=["janvier","fev","mars","avril","mai","juin","juillet","aout","sep","oct","nov","dec"]
l2=[31,28,31,30,31,30,31,31,30,31,30,31]
l3=[l1[i]+l2[i] for i in range(12) ]
print(l3)
print(list(zip(l1,l2)))

#ex4
l=[[1,2,3],[4,5,6],[7,8,9]]
l=[l[i][j] for i in range(len(l)) for j in range(len(l[i]))]
print(l)

#                                          chaine

#ex2
ch=input("donner une chaine  ")
c=input("donner un sous chaine ")

l=ch.split(" ")
for i in range(len(l)):
    if l[i]==c:
        print(i)

#ex3    
l=[(mot,len(mot)) for mot in input("donnez votre chaine ").split(" ")]
print(l)

#                                          tuple

# ex1 
l=["nom1","nom2","nom3"]
l1=["prenom1","prenom2","prenom3"]
l2=[10,20,30]
t=list(zip(l,l1,l2))
for e in t:
    print ("le nom est ", e[0].upper(),"le prenom est ",e[1].capitalize(),"l age est ",e[2])      

#                                          collection

# ex
e={1,2}
e.add(3)
e.add(0)
e.add(2)
print(e)

#ex 2
el=set(input("donner votre chaine ").split(" "))
e={"le","la","un","une","et","est"}
print(el-e)

 #                                          dictionnaire
 
 # ex  1                                  
d={}
dic={"oui":"yes","non":"no"}
for cle,valeur in dic.items():
  d[valeur]=cle
print(d)  
#autre methoed
d={valeur:cle for cle,valeur in dict}

#ex2
l=input("donner votre chaine").split(" ")
d={l.count(e):e for e in l}
print(d)

#ex3
l={}
for i in range(2):
    l[input("donner le nom et le prenom  ")]=input("donner votre note")    
print(l[input("donner le nom et le prenom d'etudiant cherche ")])
d={(e[0],e[1]):e[2] for e in zip(l,l1,l2)}

 #                                          fonctions
#exp1
def mafonction ():
    print("bonjour")
    return 1,2
x,y=mafonction()
print(x,y)
z=mafonction()
print(z) 
print (type(z))

#ex
def parler_enthousiasme (ch,n=1,b=False):
    while(n != 0):
        ch += "!"
        n-=1
    if b == True:
        ch = ch.upper()
    return(ch)

ch="farah"
print(parler_enthousiasme(ch,2,True))

#ex2
def ouvrage(titre,*auteurs,**info):
    print(titre)
    print(auteurs)
    for a,b in info.items() :
        print(a,b)

ouvrage( "book1","auteur1","auteur2", annee= 2000 , nbre_de_page= 120 )            

#ex help
def mafonction ():
    """ afficher bonjour """
    print("bonjour")
help(mafonction)

#ex
l=[{"nom":"foulen", "note":19 },{"nom":"foulen2","note":16}]
l.sort(key=lambda x:x["note"] )
print(l)

#ex
def carre (t):
    for x in t:
        yield x*x
t=(1,2,3,4,5,6,7,8,9,10)
for i in carre(t):
    print(i)

#             les classes  
class voiture :
    """ documentation """
    __plots=("numero","nombre")#attributs obligatoire
    nbre=0 #attributs statique
    def __init__(self,n) -> None: #constructeur
        self.numero=n 
        voiture.nbre+=1
    def SetMarque ( self, m): #methode
        self.marque=m 
    def __del__(self): #destructeur
        print("this object is deleted")
    def __str__(self) -> str: #tostring java
        return str (self.numero)

    @staticmethod #static method
    def maMethode():
        print("this method is static")
    def __add__(self,other): #+
        return self.numero+other.numero 
    def __eq__(self, __o: object) -> bool: #==
        return self.numero==__o.numero
voiture.maMethode()    
print(voiture.nbre)
v=voiture(1)
print(voiture.nbre)
print(v.nbre)
v.couleur ="rouge"
p=voiture(2)
p.marque="clio"
voiture.nbre=5
print(voiture.nbre)
print(v.__doc__)
print(v.__class__)
v.SetMarque("golf")
v.__del__()
print(v.__dict__)
print(p.__dict__)
print (v)
print(v.__str__())
print(v+p)

#     point
class point :
    def __init__(self,a,b) -> None:
        self.x=a
        self.y=b
    def deplacer(self,**cord):
        if("x" in cord):
            self.x +=cord["x"]
        if("y" in cord):
            self.y +=cord["y"]
    def distance(self,pt) :
        return ((self.x-pt.x)**2+(self.y-pt.y)**0.5)
    def __str__(self) -> str:
        return "x = {} y={}".format(self.x,self.y)
    def __eq__(self, __o: object) -> bool:
        return ((self.x==__o.x)and(self.y==__o.y))

#from module import point    

#       ex
def say_dynamic(cls):
    print("dynamic")
class sadClass (object):
    pass

sadClass.say_dynamic = classmethod(say_dynamic)
sadClass.say_dynamic()

#       encap1
class MaClasse :
    def __init__(self) -> None:
        self.__num=1
    def _get_num(self):
        return self.__num
obj =MaClasse()
print(obj.__dict__)
print (obj.__num)

#       encapsulation2
class compte:
    def __init__(self,val=0) -> None:
        self._solde=val

    def set_solde(self,val):
        print("je suis dans le set")
        if val<0:
            print("erreur")
        else :
            self._solde=val
    
    def get_solde(self):
        print("je suis dans le get")
        return self._solde

    solde=property(fget=get_solde,fset=set_solde)

c=compte(2000)
print(c.get_solde())
c.set_solde(-1500)
print(c.get_solde())
print(type(compte.solde))

#       polygone
class point :
    def __init__(self,a,b) -> None:
        self.x=a
        self.y=b
    def deplacer(self,**cord):
        if("x" in cord):
            self.x +=cord["x"]
        if("y" in cord):
            self.y +=cord["y"]
    def distance(self,pt) :
        return ((self.x-pt.x)**2+(self.y-pt.y)**0.5)
    def __str__(self) -> str:
        return "x = {} y={}".format(self.x,self.y)
    def __eq__(self, __o: object) -> bool:
        return ((self.x==__o.x)and(self.y==__o.y))

class polygone:
    def __init__(self,*points) -> None:
        self.pt=[]
        for e in points:
            self.pt.append(point(e[0],e[1]))
    
    def perimetre(self):
        prev=self.pt[-1]
        sum=0
        for p in self.pt :
            sum+=p.distance(prev)
            prev=p
        return sum

#
class personne:
    def __init__(self,nom,age,salaire) -> None:
        self.nom=nom
        self.age=age
        self.salaire=salaire

    def affichage (self):
        print("nom :",self.nom )

#       heritage
class class1 :
    def m(self):
        print("in class 1")
class class2 (class1):
    def m(self):
        print("in class2")
        super().m()
        
class class3 (class1):
    def m(self):
        print("in class 3")
        super().m()
class class4 (class2,class3):
    def m(self):
        print("in class4")
        super().m()
obj =class4()
obj.m()
print(class4.__mro__)

#   point Colore 
class point :
    def __init__(self,a,b) -> None:
        self.x=a
        self.y=b
    def deplacer(self,**cord):
        if("x" in cord):
            self.x +=cord["x"]
        if("y" in cord):
            self.y +=cord["y"]
    def distance(self,pt) :
        return ((self.x-pt.x)**2+(self.y-pt.y)**0.5)
    def __str__(self) -> str:
        return "x = {} y={} ".format(self.x,self.y)
    def __eq__(self, __o: object) -> bool:
        return ((self.x==__o.x)and(self.y==__o.y))
class point_coloré (point):
    def __init__(self, a, y,r=0,g=0,b=0) -> None:
        super().__init__(a, y)
        self.r=r
        self.g=g
        self.b=b
    def __str__(self) -> str:
        ch= super().__str__()
        return ch+"r = {} g = {} b = {} ".format(self.r , self.g , self.b)
    def augmenter (self,r=0,g=0,b=0):
        if (r!=0):
            self.r +=r
        if (g!=0):
            self.g += g
        if(b != 0):
            self.b += b    


a=eval(input("donner les nombres de points  "))
l=[]
for i in  range(a) :
    print("point num {}".format(i) )
    x=eval(input("donner x : "))
    y=eval(input("donner y : "))
    c=input("un point colore ? O/N  ")
    if c=="O":
        r=eval(input("donner r : "))
        g=eval(input("donner g : "))
        b=eval(input("donner b : "))
        l.append(point_coloré(x,y,r,g,b))
    else :
        l.append(point(x,y))
for pt in l :
    if isinstance(pt,point_coloré):
        pt.augmenter(10)
        print(pt.__str__())

#  Interface
import zope.interface
class IMyInterface (zope.interface.Interface):
    def methode1 (self,x):
        pass
    def methode2 (self):
        pass

#   Exceptions

def dire_bonjour_a  ( nom):
    if (nom==" "):
        raise Exception("la chaine est vide ")
    if ( nom.isalpha()==False ):
        raise ValueError("le nom n'est pas de type chaine")
    
    print("bonjour ",nom)
try:
    nom=input("donner votre nom  ")
    dire_bonjour_a(nom)
except ValueError as e :
    print ("erreur , message : ",e)
except Exception as exc :
    print("erreur message : ",exc)
    

