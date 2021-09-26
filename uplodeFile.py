import dropbox
import os

class TransferData:
    def __init__(self, access_tocken):
        self.access_tocken=access_tocken

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

        for root, dirs, files in os.walk(file_from):
            relative_path = os.path.realpath(local_path, file_from)
            dropbox_path = os.join(file_to, relative_path)


def main():
    access_token = 'sl.A5THBZr6uPH5HHfsM51nQ_h2x09dIjx9uvt3BWQ7xJN5x71qSVmQNtCFkekXzly9x62SD6x7T25PRNsvFIlrJ6-I--zIPZvvXCfVfW7xdXXmRl00FRk4qgvlvyBw59RxZmRgcEc'
    transferData = TransferData(access_token)

    file_from = input("Enter file name to transfer: ")
    file_to = input("Enter the full path to upload to dropbox:- ")

    transferData.upload_file(file_from, file_to)
    print("Your file has been moved")


main()