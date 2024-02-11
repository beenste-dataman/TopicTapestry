import os
import subprocess
import time
from sorting_files import sort_files
from filename_translation import translate_filenames


def check_requirements():
    try:
        import pandas
        import nltk
        import gensim
        import pyLDAvis
    except ImportError:
        print_ascii()
        print("Some required libraries are missing. Installing now from requirements.txt...")
        
        # Getting the directory in which this script resides
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # Building path to the requirements.txt file relative to current script's location
        requirements_path = os.path.join(current_directory, "requirements.txt")
        
        print("\n[INFO] Starting installation...\n")
        subprocess.check_call(["pip3", "install", "-r", requirements_path])
        
        print("\nInstallation completed. Please run the script again.")
        exit()

def print_ascii():
    print(r"""  
 _______  .---.  ,---.  ,-.  ,--,                                 
|__   __|/ .-. ) | .-.\ |(|.' .')                                 
  )| |   | | |(_)| |-' )(_)|  |(_)                                
 (_) |   | | | | | |--' | |\  \                                   
   | |   \ `-' / | |    | | \  `-.                                
   `-'    )---'  /(     `-'  \____\                               
         (_)    (__)                                              
   _______  .--.  ,---.  ,---.     .---.  _______ ,---.  .-.   .-.
  |__   __|/ /\ \ | .-.\ | .-'    ( .-._)|__   __|| .-.\  \ \_/ )/
    )| |  / /__\ \| |-' )| `-.   (_) \     )| |   | `-'/   \   (_)
   (_) |  |  __  || |--' | .-'   _  \ \   (_) |   |   (     ) (   
     | |  | |  |)|| |    |  `--.( `-'  )    | |   | |\ \    | |   
     `-'  |_|  (_)/(     /( __.' `----'     `-'   |_| \)\  /(_|   
                 (__)   (__)                          (__)(__)    
    """)
    time.sleep(1)  # Let the user see the ASCII art for a bit


def main():
    check_requirements()

    while True:
        print('-' * 55)
        print('-' * 55)
        print('-' * 55)
        print('-' * 55)
        print_ascii()
        print('-' * 55)
        print('-' * 55)
        print("\nChoose an option:")
        print("1: Sort Files")
        print("2: Translate Filenames")  # New option added
        print("3: Run LDA Analysis")
        print("4: Query LDA Output Database")
        print("5: Open Prior LDA Visualization")
        print("6: Exit")
        
        choice = input("Enter your choice: ")
        
        # Getting the directory in which this script resides
        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        if choice == "1":
            sort_files()
        elif choice == "2":  # New option added
            src_lang = input("Enter the source language (e.g., 'en'): ")
            trg_lang = input("Enter the target language (e.g., 'es'): ")
            source_directory = input("Enter the source directory path: ")
            target_directory = input("Enter the target directory path: ")
            translate_filenames(source_directory, target_directory, src_lang, trg_lang)
        elif choice == "3":
            lda_script_path = os.path.join(current_directory, "lda_analysis.py")
            os.system(f'python3 {lda_script_path}')
        elif choice == "4":
            csv_script_path = os.path.join(current_directory, "csv_query.py")
            os.system(f'python3 {csv_script_path}')
        elif choice == "5":
            # Building path relative to current script's location for the lda.html file
            lda_html_path = os.path.join(current_directory, "lda.html")
            os.system(f'xdg-open "{lda_html_path}"')
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
