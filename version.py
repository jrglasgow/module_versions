#!/usr/bin/env python3

import sys, os
import pprint as pp
import yaml
import packaging.version as version

#
# get the infor file
#
def getInfoFiles():
    infoFiles = []
    for root, dirs, files in os.walk('.'):
        # Add the files list to the the infoFiles list
        for filename in files:
            if 'info.yml' in filename:
                infoFiles.append(os.path.join(root, filename))
    return infoFiles

def ddpm(value, name = False):
    print("")
    print("")
    print("")
    if name:
        print(name, end="  ")
    print(type(value), end=" => ")
    pp.pprint(value)
    print("")
    print("")
    print("")



#
# get the current version of the Drupal module
#
def getVersion():
    infoFiles = getInfoFiles()
    if len(infoFiles) >= 1:
        firstFile = infoFiles[0]
        # open the info file
        with open(firstFile, 'r') as file:
            info = yaml.safe_load(file)
            file.close()
            if 'version' in info:
                return version.parse(str(info['version']))
            else:
                raise ValueError('No version in %s' % firstFile)
        pass
    else:
        print('No info files in current directory!')


#
# figure out the new version
#
def getNewVersion(version):
    new = {
        'major': version.major,
        'minor': version.minor,
        'micro': version.micro
    }
    if sys.argv[1] == 'major':
        new['major'] = version.major + 1
        new['minor'] = 0
        new['micro'] = 0
    elif sys.argv[1] == 'minor':
        new['minor'] = version.minor + 1
        new['micro'] = 0
    elif sys.argv[1] == 'patch':
        new['micro'] = version.micro + 1
    return ("%s.%s.%s" % (new['major'], new['minor'], new['micro']))

#
# open the file for writing and update the version to the newVersion
#
def updateFile(filename, newVersion):
    ddpm(filename, 'updateFile filename')
    with open(filename, 'r') as file:
        info = yaml.safe_load(file)
        file.close()
        info['version'] = newVersion
        ddpm(info, 'info')
        with open(filename, 'w') as writefile:
            yaml.dump(info, writefile)
            os.system('git add %s' % filename)
    pass

#
# update the version in the info.yml file(s)
#
def updateVersion(oldVersion, newVersion):
    infoFiles = getInfoFiles()
    ddpm(infoFiles, 'infoFiles')
    print('Are you sure you want to update the version in the following files from')
    print('%s to %s' % (oldVersion, newVersion))
    for filename in infoFiles:
      print(filename)
    answer = input('? ')

    if answer.lower() == 'y' or answer.lower() == 'yes':
        print('ok, we will do it')
        for filename in infoFiles:
            updateFile(filename, newVersion)
        # commit the version change
        os.system('git commit -m "incremented version to %s"' % newVersion)
        # create the tag
        os.system('git tag %s' % newVersion)
        # push the tag
        os.system('git push origin %s' % newVersion)
        os.system('git push origin --tags')
        # push the branch
        os.system('git push origin')
    else:
        print('operation aborted')
    pass

if __name__ == '__main__':
    version = getVersion()
    newVersion = getNewVersion(version)
    updateVersion(version.public, newVersion)

    pass
