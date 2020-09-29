# -*- encoding: utf-8 -*-
__author__ = 'tang'


import pysvn
from datetime import datetime


# Get svn server connection
def ssl_server_trust_prompt(trust_dict):
    # True -> ssl server is trusted
    # False -> ssl server is not trusted
    retcode = True
    # int, the accepted failures allowed
    # Typically just return trust_dict["failures"]
    accepted_failures = trust_dict['failures']
    # True -> remember the certificate in the configuration directory
    # False -> prevent saving the certificate
    save = True
    return retcode, accepted_failures, save


# Login svn
def get_login(realm, username, may_save):
    # True -> subversion is to use the username and password
    # False -> no username and password are available
    retcode = True
    username = 'XXX'
    password = 'XXXXXX'
    # True -> remember the username and password in the configuration directory
    # False -> prevent saving the username and password
    save = False
    return retcode, username, password, save


# Check if the file has been uploaded
def is_uploaded(filelist, filename):
    if filelist.__contains__(filename):
        print 'Successfully uploaded the file:)'
    else:
        print 'Failed to upload the file:('


# Save file uploading records to local
def save_records(urlfiles, filenames):
    for urlfile in urlfiles:
        file_path = urlfile.get('name')
        file_name = file_path.split('/')[-1]
        filenames.append(file_name)
        file_size = str(int(round(urlfile.get('size') / 1000.00, 0))) + 'KB'
        file_author = urlfile.get('last_author')
        file_time = datetime.fromtimestamp(urlfile.get('time')).strftime('%Y-%m-%d')
        print file_name, file_size, file_author, file_time


if __name__ == '__main__':
    # Get from frontend
    svn_url = 'https://XX.XX.XXX.XXX/svn/自动化测试文件库/批次功能测试/XXX/XXXXXX'
    # Get from frontend
    imported_files = []

    # Start svn client
    client = pysvn.Client()
    # Connect to svn server
    client.callback_ssl_server_trust_prompt = ssl_server_trust_prompt
    # Login svn
    client.callback_get_login = get_login

    # Commit an unversioned file or tree into the repository
    # e.g. client.import_('C:\Users\\tf5834\Desktop\\test.docx', svn_url+'/test.docx', '上传记录单')
    '''
    for imported_file in imported_files:
        client.import_(imported_file, svn_url+'/imported_file', '上传记录单')
    '''

    # client.ls() -> return a list of dictionaries for each file the given path at the provided revision
    url_files = client.ls(svn_url, recurse=True)
    # Process file names
    file_names = []
    # Process uploading records and save to local
    save_records(url_files, file_names)
    # Check if the file has been uploaded to svn
    is_uploaded(file_names, 'a5.docx')
