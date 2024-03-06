import subprocess, os
def main():
    output = input("Enter path to save files(Leave empty if wish to download to current directory): ")
    format = input("Format: Audio, All")
    input("Please have queue list ready in Queue.txt file. Once ready press enter to begin download.")
    downloader(output, format) 


def downloader(output, format):
    with open(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','Queue.txt') , 'r+') as file:
        os.chdir(output)
        match format:
            case 'audio':
                cmd = 'yt -f 251 '
            case 'all':
                cmd = 'yt -f best'
              
        
        while True:
        
            link = file.readline() #using file method
            if link == '':
                file.truncate(0)
                file.close()
                subprocess.run("color 2", shell = True, capture_output = False)
                print("EOF. Download list complete")
                exit(0)
                
        



            subprocess.run(cmd + link, shell=True, capture_output=False)




















if __name__ == "__main__":
    main()
