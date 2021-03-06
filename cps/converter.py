#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import ub
import re
from flask_babel import gettext as _


def versionKindle():
    versions = _(u'not installed')
    if os.path.exists(ub.config.config_converterpath):
        try:
            p = subprocess.Popen(ub.config.config_converterpath, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p.wait()
            for lines in p.stdout.readlines():
                if isinstance(lines, bytes):
                    lines = lines.decode('utf-8')
                if re.search('Amazon kindlegen\(', lines):
                    versions = lines
        except Exception:
            versions = _(u'Excecution permissions missing')
    return {'kindlegen' : versions}


def versionCalibre():
    versions = _(u'not installed')
    if os.path.exists(ub.config.config_converterpath):
        try:
            p = subprocess.Popen([ub.config.config_converterpath, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p.wait()
            for lines in p.stdout.readlines():
                if isinstance(lines, bytes):
                    lines = lines.decode('utf-8')
                if re.search('ebook-convert.*\(calibre', lines):
                    versions = lines
        except Exception:
            versions = _(u'Excecution permissions missing')
    return {'Calibre converter' : versions}


def versioncheck():
    if ub.config.config_ebookconverter == 1:
        return versionKindle()
    elif ub.config.config_ebookconverter == 2:
        return versionCalibre()
    else:
        return {'ebook_converter':_(u'not configured')}

