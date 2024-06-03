import os
import git
import shutil
import json

def clone_repository(repo_url, clone_dir):
    if os.path.exists(clone_dir):
        shutil.rmtree(clone_dir)
    git.Repo.clone_from(repo_url, clone_dir)

def download_files_from_directory(local_repo_path, target_directory):
    # target directory is the directory inside the repository that contains the ADRs
    # since we cloned the repo, if we join the local repo path with the target directory
    # we will get the full path to the directory that contains the ADRs
    full_directory_path = os.path.join(local_repo_path, target_directory)
    if not os.path.exists(full_directory_path):
        print(f"Directory {full_directory_path} does not exist.")
        return
    
    files = os.listdir(full_directory_path)
    for file_name in files:
        file_path = os.path.join(full_directory_path, file_name)
        if os.path.isfile(file_path):
            print(f"Downloading {file_name} from {file_path}...")
            with open(file_path, 'rb') as file:
                content = file.read()
                # all adrs will be stored in a dump in the data folder
                dest_folder = "../data/ADRs-Updated"
                dest_file_path = os.path.join(dest_folder, file_name)
                with open(dest_file_path, 'wb') as dest_file:
                    dest_file.write(content)

def process_metadata_file(metadata_file_path):
    with open(metadata_file_path, 'r') as f:
        metadata = json.load(f)
    repo_url = metadata["repositoryUrl"]
    clone_dir = "temp_repo"
    clone_repository(repo_url, clone_dir)
    for adr_directory in metadata["adrDirectories"]:
        download_files_from_directory(clone_dir, adr_directory)
    shutil.rmtree(clone_dir)

def process_all_metadata_files(metadata_directory):
    file_count = len(os.listdir(metadata_directory))
    i = 0
    for file_name in os.listdir(metadata_directory):
        if file_name.endswith('.json'):
            metadata_file_path = os.path.join(metadata_directory, file_name)
            print(f"Processing {metadata_file_path} --> {i+1} of {file_count})...")
            process_metadata_file(metadata_file_path)
        i += 1

if __name__ == "__main__":
    print("Starting ADR Scrapper...")
    metadata_directory = "../data/ADR-Study-Dataset-Metadata/repositories"
    process_all_metadata_files(metadata_directory)
