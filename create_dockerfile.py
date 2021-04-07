#!/usr/bin/env python 

print('creating Dockerfile and Docker image')

#library calls
import argparse
import os

#arguments
parser = argparse.ArgumentParser()

parser.add_argument('--rvers', help = "version of R used for replication")
parser.add_argument('--rpacks', help = 'comma-separated list of R packages used *with versions* as a .txt file')
parser.add_argument('--repdir', help = 'directory containing all replication files')
parser.add_argument('--runscript', help = 'script to run all replication files and save all output')

args = parser.parse_args()

#set working directory
os.chdir(args.repdir)

#create strings to be inserted into Dockerfile
lines = ['FROM rocker/r-ver:' + args.rvers + '\n',
'WORKDIR /replication \n',
'COPY' + ' ' + '.' + ' ' + '. \n'
'RUN Rscript install_packages.R' + " " + args.rpacks + '\n',
'RUN Rscript' + ' ' + args.runscript
]

#write dockerfile
dockerfile = open(r"Dockerfile", 'w+')
dockerfile.writelines(lines)
dockerfile.close()

print('dockerfile written')

os.system('docker build  --no-cache -t replication_img .')
