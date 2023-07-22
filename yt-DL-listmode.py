import subprocess, os
def main():
    output = input("Enter path to save files: ")
    input("Please have queue list ready in Queue.txt file. Once ready press enter to begin download.")
    downloader(output) 


def downloader(output):
    with open(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','Queue.txt') , 'r+') as file:
        while True:
        
            link = file.readline() #using file method
            if link == '':
                file.truncate(0)
                file.close()
                subprocess.run("color 2", shell = True, capture_output = False)
                print("EOF. Download list complete")
                exit(0)
                
        
            #standard stuff
            #cmd = "yt --embed-sub -f b --cookies-from-browser " + browser  + " --merge-output-format mkv "
            #cmd = "yt --embed-sub --user-agent \"" + agent + "\" --extractor-args crunchyrollbeta:ua_workaround --cookies-from-browser " + browser  + " --merge-output-format mkv "
            cmd = 'yt -f b '
            #desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')    #For desktop Storing

            os.chdir(output)
            subprocess.run(cmd + link, shell=True, capture_output=False)




















if __name__ == "__main__":
    main()


    

