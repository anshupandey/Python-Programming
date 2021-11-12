# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 09:08:23 2021

@author: anshu
"""

# glob, zipfile, tarfile

import os

# getting list of all files in a directory
flist = os.listdir("D:\AI\Python-Programming\Xceedance")
flist

import glob

# getting the list of .py files from a specific directory
flist = glob.glob("D:\\AI\\Python-Programming\\*.py")
for file in flist:print(file)

# recursive file extraction - extracting all .py files, from
# the main directory and subdirectories
flist = glob.glob("D:\\AI\\Python-Programming\\**\\*.py",recursive=True)
for file in flist:print(file)


# getting the list of .txt files having filename of 6 letters
flist = glob.glob("D:\\AI\\Python-Programming\\\Xceedance\\??????.txt")
for file in flist:print(file)

##############################################################
import zipfile
# creating zip archives

# getting the list of files to archive
# getting the list of .py files from a specific directory
flist = glob.glob("D:\\AI\\Python-Programming\\*.py")
for file in flist:print(file)

zf = zipfile.ZipFile("Myzipcodes.zip",mode='w',compression=zipfile.ZIP_DEFLATED)
for file in flist:zf.write(file)
zf.close()

## Extracting files from a zip folder

# check the list of files in a zip folder
zf = zipfile.ZipFile("Myzipcodes.zip",mode='r')
print(zf.namelist())
zf.close()

# extracting files from a zip folder
zf = zipfile.ZipFile("Myzipcodes.zip",mode='r')

zf.extractall("mycodes")
zf.close()

###################################################################

import tarfile


# getting the list of files to archive
# getting the list of .py files from a specific directory
flist = glob.glob("D:\\AI\\Python-Programming\\*.py")
for file in flist:print(file)


# creating an atar archive
tar = tarfile.open("mypycodes.tar.gz",mode='w')
for file in flist:tar.add(file)
tar.close()

# Extracting data from ar archive

# check the list of files
tar = tarfile.open("mypycodes.tar.gz",mode='r')
for file in tar.getmembers():print(file.name)
tar.close()

# extractign files from tar archieve
tar = tarfile.open("mypycodes.tar.gz",mode='r')
tar.extractall("tarcode",members=tar.getmembers())
tar.close()
