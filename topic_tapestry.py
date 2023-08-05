import os
import subprocess
import time

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
        subprocess.check_call(["pip", "install", "-r", requirements_path])
        
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
        print("\nChoose an option:")
        print("1: Run LDA Analysis")
        print("2: Query CSV File")
        print("3: Exit")
        
        choice = input("Enter your choice: ")
        
        # Getting the directory in which this script resides
        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        if choice == "1":
            # Building path relative to current script's location
            lda_script_path = os.path.join(current_directory, "lda_analysis.py")
            os.system(f'python {lda_script_path}')
        elif choice == "2":
            csv_script_path = os.path.join(current_directory, "csv_query.py")
            os.system(f'python {csv_script_path}')
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
