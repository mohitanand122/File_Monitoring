import os
import hashlib
import time

def hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    hash_sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            hash_sha256.update(byte_block)
    return hash_sha256.hexdigest()

def monitorDirectory(directory):
    """Monitor the specified directory for changes in files."""
    file_hashes = {}

    while True:
        current_files = {f: hash(os.path.join(directory, f)) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))}

        for file_name, file_hash in current_files.items():
            if file_name not in file_hashes:
                print(f"New file detected: {file_name} (Hash: {file_hash})")
            elif file_hashes[file_name] != file_hash:
                print(f"File modified: {file_name} (Old Hash: {file_hashes[file_name]}, New Hash: {file_hash})")

        for file_name in list(file_hashes.keys()):
            if file_name not in current_files:
                print(f"File deleted: {file_name} (Last Hash: {file_hashes[file_name]})")

        file_hashes = current_files
        time.sleep(10)

if __name__ == "__main__":
    # Get directory input, strip quotes and whitespace
    raw_input = input("Enter the directory to monitor (or press Enter for default): ").strip('"\' ')
    
    # Convert Windows paths to Linux format if needed
    if raw_input and ':\\' in raw_input:
        # Remove drive letter and convert to Linux path
        path_parts = raw_input.split('\\')
        if path_parts[0].endswith(':'):
            path_parts = path_parts[1:]
        directory_to_monitor = '/' + '/'.join(path_parts)
    else:
        directory_to_monitor = raw_input
    
    # Use default test directory if input is empty or invalid
    if not directory_to_monitor or not os.path.isdir(directory_to_monitor):
        directory_to_monitor = os.path.join(os.getcwd(), 'test_monitor')
        os.makedirs(directory_to_monitor, exist_ok=True)
        print(f"Using default test directory: {directory_to_monitor}")
    
    directory_to_monitor = os.path.abspath(directory_to_monitor)
    print(f"Monitoring changes in directory: {directory_to_monitor}")
    monitorDirectory(directory_to_monitor)
