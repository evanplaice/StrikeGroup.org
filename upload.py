import os
import sys
import traceback

from ftplib import FTP

host = ''
username = ''
password = ''
rootdir = os.getcwd() + os.sep + 'static'

def upload():
  print 'Logging in...'
  ftp = FTP()
  ftp.connect(host)
  print ftp.getwelcome()
  try:
    ftp.login(username, password)
    ftp.cwd(dir)
    print 'Currently in: ', ftp.pwd()
    print 'Uploading...'
    path = './dir/file'
    fileName = os.path.split(path)[1]
    f = open(path, 'rb')
    ftp.storbinary('STOR ' + fileName, f)
    f.close()
    print 'OK'
    print 'Files:'
    print ftp.retrlines('LIST')
  except:
    traceback.print_exc()
  finally:
    print 'Quitting'
    ftp.quit()

def uploadfile(file):
  return
    
def filelist(root):
  fileList = []
  #fileSize = 0
  folderCount = 0
  for root, subFolders, files in os.walk(rootdir):
    folderCount += len(subFolders)
    for file in files:
      f = os.path.join(root,file)
      #fileSize = fileSize + os.path.getsize(f)
      fileList.append(f.replace(rootdir, ''))
  return fileList    
    

files = filelist(rootdir)
for file in files:
  print file