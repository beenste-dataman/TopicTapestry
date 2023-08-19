import os
import shutil
import torch
from tqdm import tqdm
from transformers import MarianMTModel, MarianTokenizer

def print_emoji_art():
    print('''
    ______     _     _             
   |  ____|   | |   | |            
   | |__ _ __| |__ | |_   _ _ __   
   |  __| '__| '_ \| | | | | '_ \  
   | |  | |  | |_) | | |_| | | | | 
   |_|  |_|  |_.__/|_|\__,_|_| |_| 
    🌍🌎🌏 FILENAME TRANSLATOR 🌍🌎🌏
    ''')

def translate(text: str, model, tokenizer):
    """Translates the text using the MarianMT model."""

    try:
        # Tokenize the text
        tokenized_text = tokenizer.prepare_seq2seq_batch([text], return_tensors='pt')

        # Translate the text
        translated_text = model.generate(**tokenized_text)

        # Decode the translated text
        decoded_text = tokenizer.batch_decode(translated_text, skip_special_tokens=True)[0]

        return decoded_text
    except Exception as e:
        print(f"🚫 Error during translation: {e}")
        return text  # If there's an error, return the original text

def translate_filenames(source_directory: str, target_directory: str, src_lang: str, trg_lang: str):
    """Recursively translates the filenames in a directory."""
    
    print_emoji_art()
    print(f"📂 Source Directory: {source_directory}")
    print(f"📁 Target Directory: {target_directory}")
    print(f"🔄 Translating filenames from {src_lang} to {trg_lang}\n")
    
    # Define the model and tokenizer
    model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{trg_lang}'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # Get the list of all files in directory tree at given path
    list_of_files = []
    for (dirpath, dirnames, filenames) in os.walk(source_directory):
        list_of_files += [os.path.join(dirpath, file) for file in filenames]

    # Walk through the directory
    for file in tqdm(list_of_files, desc='Translating filenames', unit='file'):
        try:
            # Translate the filename
            translated_name = translate(os.path.splitext(os.path.basename(file))[0], model, tokenizer)

            # Keep the extension of the file
            translated_name_with_ext = f'{translated_name}{os.path.splitext(file)[1]}'

            # Define the old and new file paths
            new_file_path = os.path.join(target_directory, translated_name_with_ext)

            # Ensure that the target directory structure exists
            os.makedirs(os.path.dirname(new_file_path), exist_ok=True)

            # Copy the file with the new name
            shutil.copy2(file, new_file_path)

        except Exception as e:
            print(f"🚫 Error translating/copying file {file}: {e}")
    
    print("🎉 Translation complete! Check your target directory for translated filenames.")

if __name__ == "__main__":
    print_emoji_art()
    src_lang = input("Enter the source language (e.g., 'en'): ")
    trg_lang = input("Enter the target language (e.g., 'es'): ")
    source_directory = input("Enter the source directory path: ")
    target_directory = input("Enter the target directory path: ")
    
    if not os.path.isdir(source_directory):
        print(f"🚫 The source directory {source_directory} does not exist.")
    elif not os.path.isdir(target_directory):
        print(f"🚫 The target directory {target_directory} does not exist.")
    else:
        translate_filenames(source_directory, target_directory, src_lang, trg_lang)
