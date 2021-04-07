#!/usr/bin/env python 
#imports
import PySimpleGUI as sg 
import subprocess
import sys
import logging

sg.theme('BluePurple')

def runCommand(rvers, rpacks, repdir, runscript, timeout=None, window=None):
    cmd = 'python create_dockerfile.py --rvers=' + rvers + ' ' + '--rpacks=' + rpacks + ' ' + '--repdir=' + repdir + ' ' + '--runscript=' + runscript
    logging.debug(cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ''
    for line in p.stdout:
        line = line.decode(encoding=sys.stdout.encoding, errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
        print(line)
        output += line       
    retval = p.wait(timeout)
    logging.debug('retval=%d' % retval)
    return (retval, output)    


layout = [
          [sg.Text('Please enter the necessary information')],
          [sg.Text('This assumes all filepaths are relative already - it does not change code.')],
          [sg.Text('R Version', size=(25, 1)), sg.InputText('', key = 'rvers')],
          [sg.Text('Package list', size=(25, 1)), sg.InputText('', key ='rpacks')],
          [sg.Text('Replication directory', size=(25, 1)), sg.InputText('', key = 'repdir')],
          [sg.Text('Run script', size=(25,1)), sg.InputText('', key = 'runscript')],
          [sg.Submit('Run Code')]
         ]

window = sg.FlexForm('R Docker Replicator', layout, default_element_size=(40, 1))

while True:  # Event Loop
    event, values = window.Read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Run Code':
        # Update the "output" text element to be the value of "input" element
        runCommand(values['rvers'], values['rpacks'], values['repdir'], values['runscript'])

window.close()
                    
