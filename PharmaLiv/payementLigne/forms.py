from django import forms

quantite_produit =[(i,str(i))for i in range(1,21)]

class form_panier(forms.Form):
    quantite = forms.TypedChoiceField(choices=quantite_produit,coerce=int)
    update = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)