from paiement import traiter_paiements, CarteBancaire, PayPal, Crypto

if __name__ == '__main__':
    liste_commandes = [
        CarteBancaire(250.75, "1234567890123456", "123"),
        CarteBancaire(12.00, "1111222233334444", "000"),

        PayPal(50.00, "flan@api.com", "token_valide_xyz123"),
        PayPal(100.00, "fartlan@email.com", "tok_court"),

        Crypto(8000.50, "bc1qxy2qxy2qxy2qxy2qxy2qxy2qxy2qxy2qxy2qxy2qxy2qxy", "BTC"),
        Crypto(25.00, "0x1234567890abcdef01234567890abcdef01234567", "ETH")
    ]

    print("--- Début du Traitement des Paiements (MAD) ---")
    traiter_paiements(liste_commandes)