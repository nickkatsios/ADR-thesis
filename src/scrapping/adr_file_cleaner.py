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

def clean_adrs_about_adrs():
    deleted_files = [
        "00-lightweight-architecture-decisions.md",
        "00-\342\234\205-adr.md",
        "000-Decision-Records.md",
        "000-Record-Architecture-Decisions.md",
        "000-architectural-decision-log-introduced.md",
        "000-architecture-decision-records.md",
        "000-architecture.md",
        "000-sample.md",
        "000-template.md",
        "000-use-adrs.md",
        "000.md",
        "0000-00-00-Template.md",
        "0000-adl-index.md",
        "0000-adr-template-en.md",
        "0000-architectural-decision-records.md",
        "0000-historic-decisions.md",
        "0000-record-architecture-decisions.md",
        "0000-template.md",
        "0000-use-architectural-decision-records.md",
        "0000-use-madr-as-record-format.md",
        "0000-use-madr.md",
        "0000-use-markdown-architectural-decision-records.md",
        "0000_use_markdown_architectural_decision_records.md",
        "0001 ADR.md",
        "0001-template.md",
        "0001_use_adr.md",
        "000_ADRs.md",
        "001 We are using ADR (template).md",
        "001-ADR-template.md",
        "001_Use_ADRs.md",
        "1-ADR_directory_identified_by_marker_file.md",
        "ADRs.md",
        "Use-ADRs.md",
        "note.md",
        "using-arc42.md"
    ]
    for file_name in deleted_files:
        file_path = os.path.join(adr_directory, file_name)
        try:
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")


if __name__ == "__main__":
    adr_directory = "../../data/ADRs-Updated-new"
    clean_non_md_files(adr_directory)
    print("--------------------------------------------------------------------------------")
    unwanted_words = ["template", "draft", "example" , "readme" , "outro" , "contributing", "index"]    
    clean_irrelevant_files(adr_directory, unwanted_words)
    print("--------------------------------------------------------------------------------")
    specific_files = ["license.md", "_intro.md", "_templte.md"]
    delete_specific_files(adr_directory, specific_files)
