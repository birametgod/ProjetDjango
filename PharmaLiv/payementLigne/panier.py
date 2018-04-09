from decimal import Decimal
from pharmacie.models import Fiche_Produit
from django.conf import settings

class Panier(object):
    """ cette classe gere les achats dans le panier"""
    def __init__(self, request):
        """ initialise le panier"""
        self.session =request.session
        panier = self.session.get(settings.PAYEMENTLIGNE_SESSION_ID) #panier de la session courante
        if not panier:#s'il ya pas de panier dans la session on enregistre un panier vide dans la session
            panier =self.session[settings.PAYEMENTLIGNE_SESSION_ID] = {}
        self.panier = panier
            
    
    def add(self,produit,stock=1,update_stock=False):
        """ajouter un produit dans le panier """
        produit_id=str(produit.id)
        if produit_id not in self.panier:
            self.panier[produit_id] = {
                'stock':0,
                'prix':str(produit.prix),
            }
        if update_stock:
            self.panier[produit_id]['stock'] = stock
        else:
            self.panier[produit_id]['stock']+= stock
        self.save()

    def save(self):
        self.session[settings.PAYEMENTLIGNE_SESSION_ID] =self.panier
        self.session.modified =True 

    def remove(self,produit):
        produit_id=str(produit.id)
        if produit_id not in self.panier:
            del self.panier[produit_id]
            self.save()

    def __iter__(self):
        """ parcourt chaque qrticle dans le panier"""
        produit_ids = self.panier.keys() #keys() returns a list of all the available keys in the dictionary.
        produits = Fiche_Produit.objects.filter(id__in=produit_ids) #filtre les produit dont les  id  sont dans chaque cle
        for produit in produits:
            self.panier[str(produit.id)]['produit']=produit

        for item in self.panier.values():
            item['prix']=Decimal(item['prix'])
            item['total_prix'] =item['prix'] * item['stock']
            yield item #yield is a keyword that is used like return

    def __len__(self):
        """ compte le nombre d'article """
        return sum(item['stock'] for item in self.panier.values())
        
    def get_somme_prix(self):
        return sum(Decimal(item['prix']) * item['stock'] for item in self.panier.values()) 
        
    def clear(self):
        self.session[settings.PAYEMENTLIGNE_SESSION_ID] = {}
        self.session.modified =True  