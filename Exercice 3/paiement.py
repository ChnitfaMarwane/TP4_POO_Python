from abc import ABC, abstractmethod
import math 

class MontantInvalide(Exception):
    pass

class Paiement(ABC):
    def __init__(self, montant):
        if montant <= 0:
            raise MontantInvalide("Le montant doit être strictement positif.")
        self._montant = montant

    @abstractmethod
    def payer(self):
        pass

class CarteBancaire(Paiement):
    def __init__(self, montant, numero, cvv):
        super().__init__(montant)
        self._numero = numero
        self._cvv = cvv

    def payer(self):
        if not (len(self._numero) == 16 and len(self._cvv) == 3):
            return f"Paiement Carte Bancaire échoué pour {self._montant:.2f} MAD: Numéro ou CVV invalide."

        return f"Paiement Carte Bancaire de {self._montant:.2f} MAD traité. Transaction CB ****{self._numero[-4:]} OK."

class PayPal(Paiement):
    def __init__(self, montant, email, token):
        super().__init__(montant)
        self._email = email
        self._token = token

    def payer(self):
        if not self._email or len(self._token) < 10:
             return f"Paiement PayPal échoué pour {self._montant:.2f} MAD: Email ou Token invalide."
        
        return f"Paiement PayPal de {self._montant:.2f} MAD traité. Facturé à {self._email}."

class Crypto(Paiement):
    def __init__(self, montant, wallet_id, reseau):
        super().__init__(montant)
        self._wallet_id = wallet_id
        self._reseau = reseau

    def payer(self):
        if len(self._wallet_id) < 30 or self._reseau not in ["BTC", "ETH", "USDT"]:
            return f"Paiement Crypto échoué pour {self._montant:.2f} MAD: Wallet ou Réseau ('{self._reseau}') invalide."

        # Simuler le paiement
        return f"Paiement Crypto de {self._montant:.2f} MAD traité via {self._reseau}. ID Transaction {self._wallet_id[:8]}..."

def traiter_paiements(liste_paiements):
    for paiement in liste_paiements:
        print(paiement.payer())

if __name__ == '__main__':
    # Création d'une liste hétérogène (noms génériques et MAD)
    liste_commandes = [
        # Carte Bancaire
        CarteBancaire(250.75, "1234567890123456", "123"),
        CarteBancaire(12.00, "1111222233334444", "000"), # Deuxième instance CB

        # PayPal
        PayPal(50.00, "flan@api.com", "token_valide_xyz123"),
        PayPal(100.00, "fartlan@email.com", "tok_court"), # Instance PayPal invalide

        # Crypto
        Crypto(8000.50, "bc1qxy2qxy2qxy2qxy2qxy2qxy2qxy2qxy2qxy2qxy2qxy2qxy", "BTC"),
        Crypto(25.00, "0x1234567890abcdef01234567890abcdef01234567", "ETH")
    ]

    print("--- Début du Traitement des Paiements (MAD) ---")
    traiter_paiements(liste_commandes)