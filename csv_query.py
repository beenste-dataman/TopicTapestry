import pandas as pd
import os

def query_and_open():
    # Load the CSV file
    df = pd.read_csv('file_topics.csv')
    
    # Ask the user for the topic words they are interested in
    topic_words = input("\n🔍 Enter the topic words you are interested in (separated by commas): ")
    
    # Split the inputted string into a list of topic words
    topic_words = [word.strip().lower() for word in topic_words.split(',')]
    
    # Query the DataFrame for rows where the 'top_words' column contains any of the inputted topic words
    matching_files = df[df['top_words'].str.lower().apply(lambda x: any(word in x for word in topic_words))]
    
    # If no files match, inform the user
    if matching_files.empty:
        print("❌ No files match the provided topic words.")
        return
    
    # Print out the list of matching file paths and names for the user to choose from
    print("\n📂 Matching Files:")
    for i in range(len(matching_files)):
        print(f"{i}: {matching_files.iloc[i]['file_path']}/{matching_files.iloc[i]['file_name']}")
    
    while True:
        # Ask the user for the number of the file they want to open
        user_input = input("\n🔓 Enter the number of the file you want to open (or type 'back' to return to topic search): ")
        
        if user_input.lower() == 'back':
            return
        
        try:
            file_num = int(user_input)
            if 0 <= file_num < len(matching_files):
                # Get the path of the chosen file
                file_path = f"{matching_files.iloc[file_num]['file_path']}/{matching_files.iloc[file_num]['file_name']}"
                
                # Open the file
                os.system(f'xdg-open "{file_path}"')
            else:
                print("❌ Invalid number. Please choose a valid number from the list.")
        except ValueError:
            print("❌ Please enter a valid number or type 'back' to return to topic search.")

if __name__ == '__main__':
    print("Welcome to Topic Tapestry! 🕸️")
    while True:
        query_and_open()

        should_continue = input("\n🔄 Do you want to search for another topic? (yes/no): ").lower()
        if should_continue != 'yes':
            print("👋 Goodbye!")
            break
