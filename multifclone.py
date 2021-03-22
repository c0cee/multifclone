import subprocess
import re

class multifclone():

    def __init__(self):
        self.dest = input("Please enter the FolderID of the Destination: ")
        
    def copyFiles(self):
        with open('links.txt') as f:
            fin = f.readlines()

            for line in fin:
                self.links = re.search(r'([\w-]){33}|([\w-]){19}', line).group()
                command = 'fclone --config=rclone.conf copy GC:{' + self.links + '} GC:{'+ self.dest +'} --transfers 50 -vP --stats-one-line --drive-server-side-across-configs --ignore-existing'
                process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)
                print(process.stdout)
                print('============================\n'+
                        'Link has been copied :)\n'+
                        '============================')
            print('All Links has been copied! :)')

    def runScript(self):
        self.copyFiles()

multifclone().runScript()
