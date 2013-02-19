#!/usr/bin/env python

import re
import os
import sys
import shlex
import urllib2
import getpass
import logging
import ConfigParser
import logging.handlers

def verify_key_id(otp):    
    keys = config.get('keys', os.environ['USER']).split(':')
    if otp[0:12] in keys:
        log.info('Key ID verified')
        return True
    log.error('Key ID verification failed')
    return False

def verify_otp(otp):
    try:
        log.debug('Connecting to API')
        resp = urllib2.urlopen('https://api.yubico.com/wsapi/verify?id=%s&otp=%s' % 
                              (config.get('options', 'api_id'), otp))
    except urllib2.URLError as e:
        log.error('Failed to connect to API: %s' % str(e))
        exec_command()
    if re.search('status=OK', resp.read()):
        log.info('OTP verified')
        return True
    log.error('OTP verification failed')
    return False

def exec_command():
    try:
        cmd = shlex.split(os.environ['SSH_ORIGINAL_COMMAND'])
    except KeyError:
        cmd = shlex.split('/bin/bash')
    os.execvp(cmd[0], cmd)

def verify():
    otp = getpass.getpass(prompt='Press the button on the YubiKey: ')    
    if verify_key_id(otp) and verify_otp(otp):
        exec_command()
    else:
        sys.exit(127)

if __name__== '__main__':  
    config = ConfigParser.RawConfigParser()
    config.read('/etc/yubikey.conf')
    log = logging.getLogger('yubikey')
    log.setLevel(config.get('options', 'loglevel'))
    handler = logging.handlers.SysLogHandler(address = '/dev/log')
    handler.setFormatter(logging.Formatter('%(name)s: %(levelname)s %(message)s'))
    log.addHandler(handler)
    try:
        verify()
    except KeyboardInterrupt:
        print
        sys.exit(127)
