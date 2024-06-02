import os
import git
import shutil
import requests
import json

def clone_repository(repo_url, clone_dir):
    if os.path.exists(clone_dir):
        shutil.rmtree(clone_dir)
    git.Repo.clone_from(repo_url, clone_dir)

def download_files_from_directory(local_repo_path, target_directory):
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
                dest_file_path = os.path.join("../data/ADRs-Updated", file_name)
                with open(dest_file_path, 'wb') as dest_file:
                    dest_file.write(content)
            print(f"Downloaded {file_name} to {dest_file_path}.")

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
    for file_name in os.listdir(metadata_directory):
        if file_name.endswith('.json'):
            metadata_file_path = os.path.join(metadata_directory, file_name)
            print(f"Processing {metadata_file_path}...")
            process_metadata_file(metadata_file_path)

if __name__ == "__main__":
    print("Starting ADR Scrapper...")
    metadata_directory = "../data/ADR-Study-Dataset-Metadata/repositories"
    process_all_metadata_files(metadata_directory)
