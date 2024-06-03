import os

def clean_non_md_files(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            # Check if the file extension is not '.md'
            if not file_name.endswith('.md'):
                file_path = os.path.join(root, file_name)
                try:
                    # Delete the file
                    os.remove(file_path)
                    print(f"Deleted non-ADR file: {file_path}")
                    count += 1
                except Exception as e:
                    print(f"Error deleting file {file_path}: {e}")
    print(f"Deleted {count} non-MD files.")

# remove files that have the unwanted words in their name
# and dont start with at least 3 numbers or the string "adr-"
def clean_irrelevant_files(directory, unwanted_words):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if any(word in file_name.lower() for word in unwanted_words) and not file_name.startswith("adr-") and not file_name[0:3].isdigit():
                file_path = os.path.join(root, file_name)
                try:
                    os.remove(file_path)
                    print(f"Deleted template file: {file_path}")
                    count += 1
                except Exception as e:
                    print(f"Error deleting file {file_path}: {e}")
    print(f"Deleted {count} template files.")

def delete_specific_files(directory, file_names):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name in file_names:
                file_path = os.path.join(root, file_name)
                try:
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                    count += 1
                except Exception as e:
                    print(f"Error deleting file {file_path}: {e}")
    print(f"Deleted {count} specific files.")


if __name__ == "__main__":
    adr_directory = "../../data/ADRs-Updated"
    clean_non_md_files(adr_directory)
    print("--------------------------------------------------------------------------------")
    unwanted_words = ["template", "draft", "example" , "readme" , "outro" , "contributing", "index"]    
    clean_irrelevant_files(adr_directory, unwanted_words)
    print("--------------------------------------------------------------------------------")
    specific_files = ["license.md", "_intro.md", "_templte.md"]
    delete_specific_files(adr_directory, specific_files)
