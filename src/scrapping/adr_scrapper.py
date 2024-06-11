import os
import git
import shutil
import json
import concurrent.futures
import random
import string
import subprocess

def clone_repository(repo_url, clone_dir):
    # need to clone the whole repo beacuse adrs may have been 
    # updated/added from the time the metadata was assembled
    if os.path.exists(clone_dir):
        shutil.rmtree(clone_dir)
    git.Repo.clone_from(repo_url, clone_dir)

def repo_exists(url):
    try:
        # Run the git ls-remote command
        result = subprocess.run(['git', 'ls-remote', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Check if the response contains "Repository not found"
        if 'Repository not found' in result.stderr:
            return False
        return True
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return False
    
def get_random_string(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

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
                dest_folder = "../../data/ADRs-Updated-new"
                dest_file_path = os.path.join(dest_folder, file_name)
                with open(dest_file_path, 'wb') as dest_file:
                    dest_file.write(content)

def process_metadata_file(metadata_file_path):
    with open(metadata_file_path, 'r') as f:
        metadata = json.load(f)
    repo_url = metadata["repositoryUrl"]
    # append a random string to the directory name to avoid conflicts
    # when cloning multiple repositories in parallel
    clone_dir = "temp_repo" + get_random_string(5)
    clone_repository(repo_url, clone_dir)
    for adr_directory in metadata["adrDirectories"]:
        download_files_from_directory(clone_dir, adr_directory)
    shutil.rmtree(clone_dir)

def process_all_metadata_files(metadata_directory):
    metadata_files = [os.path.join(metadata_directory, f) for f in os.listdir(metadata_directory) if f.endswith('.json')]
    file_count = len(metadata_files)
    missing_repos = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(process_metadata_file, file_path): file_path for file_path in metadata_files}
        for i, future in enumerate(concurrent.futures.as_completed(futures), 1):
            file_path = futures[future]
            try:
                future.result()
                print(f"Processing {file_path} --> {i} of {file_count} completed successfully.")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
                # all errors came from missing repositories
                missing_repos += 1
    print("--------------------------------------------------")
    print(f"Processed {file_count} metadata files. {missing_repos} repositories were missing.")

if __name__ == "__main__":
    print("Starting ADR Scraper...")
    metadata_directory = "../../data/ADR-Study-Dataset-Metadata/repositories"
    process_all_metadata_files(metadata_directory)
