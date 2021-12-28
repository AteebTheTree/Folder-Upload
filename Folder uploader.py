import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_folder(self, folder_from, folder_to):
        dbx = dropbox.Dropbox(self.access_token)
        mode = dropbox.files.WriteMode('overwrite')

        for root, dirs, files in os.walk(folder_from):
            for name in files:
                f = open(os.path.join(root, name), 'rb')
                dbx.files_upload(f.read(), folder_to, mode)
                
            for name in dirs:
                f = open(os.path.join(root, name), 'rb')
                dbx.files_upload(f.read(), folder_to, mode)
def main():
    access_token = 'sl.A_BAFnjKA7sJ8FH1rjS0hPJDcp6sBT8JD9ZDAsnhATVe5KyCRfdYGB2dk2ZG8Heg7R2LYG9ktEJxIOUpRiabYiRAhaPK51ygWaCUPYIKHvEK-meIINmYm08Ug_gbZ0AiStcKDPxlwRk'
    transferData = TransferData(access_token)

    folder_from = input("Enter folder path to transfer: ")
    folder_to = input("Enter folder path to upload to: ")

    transferData.upload_folder(folder_from, folder_to)
    print("folder has been moved successfuly")

main()
