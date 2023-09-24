# BackEnd
import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("/Users/SanjaveSingh/Desktop/Udemy/app1/Bonus/compressed.zip",
                    "/Users/SanjaveSingh/Desktop/Udemy/app1/Bonus/files")

