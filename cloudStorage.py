import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
       
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AvWlIZ6e3tjr3hY-e43x6FzSfd28H6ky2dNj8hq_eejb2lAngipLfl-UW9J7GBaIyhtQK1IRsxaAhIUxALA24_O44VLNuopKMk9oBFh2g5l8encD-iCB8egfIylIqZ2roqBF-vw'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer:- ")
    file_to = input("Enter the full path to upload to dropbox:- ")
    
    transferData.upload_file(file_from, file_to)
    print("File has been moved")


main()

# C:\Users\Hp\Downloads\c101\test.txt
