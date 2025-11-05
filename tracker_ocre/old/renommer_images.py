import os
import re

def reverse_rename_from_log():
    """
    Restores original filenames using a log file.
    The log file should contain lines like: "Renommé : 'old_name.png' -> 'new_name.png'"
    """
    # Demande le chemin du dossier où se trouvent les images
    folder_path = input("Entrez le chemin du dossier contenant les images (ex: monster_images): ")
    log_file = "rename_log.txt"

    if not os.path.isdir(folder_path):
        print(f"Erreur : Le dossier '{folder_path}' n'a pas été trouvé.")
        return

    if not os.path.isfile(log_file):
        print(f"Erreur : Le fichier de log '{log_file}' est introuvable. Assurez-vous qu'il est dans le même dossier que le script.")
        return

    print(f"Restauration des noms dans le dossier '{folder_path}' à l'aide de '{log_file}'...")

    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            # Utilise une expression régulière pour extraire l'ancien et le nouveau nom
            match = re.search(r"Renommé : '(.+)' -> '(.+)'", line)
            
            if match:
                original_name = match.group(1)
                renamed_name = match.group(2)
                
                # Construit les chemins complets
                current_filepath = os.path.join(folder_path, renamed_name)
                original_filepath = os.path.join(folder_path, original_name)

                # Vérifie si le fichier à renommer existe bien
                if os.path.exists(current_filepath):
                    try:
                        os.rename(current_filepath, original_filepath)
                        print(f"Restauré : '{renamed_name}' -> '{original_name}'")
                    except OSError as e:
                        print(f"Erreur en restaurant '{renamed_name}' : {e}")
                else:
                    # Affiche un avertissement si le fichier n'est pas trouvé (il a peut-être déjà été renommé ou n'a jamais été changé)
                    print(f"Avertissement : Fichier '{renamed_name}' non trouvé. Ignoré.")

    print("\n--- Opération de restauration terminée ---")

if __name__ == "__main__":
    reverse_rename_from_log()