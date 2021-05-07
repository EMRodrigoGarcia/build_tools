#!/usr/bin/env python

import base
import config
import os
import subprocess

def make():
  path = base.get_script_dir() + "/../../core/Common/3dParty/curl"
  old_cur = os.getcwd()
  os.chdir(path)
  if (-1 != config.option("platform").find("android")):
    if base.is_dir(path + "/build/android"):
      return
    subprocess.call(["./build-android-curl.sh"])

  if (-1 != config.option("platform").find("ios")):
    if base.is_dir(path + "/build/ios"):
      return
    subprocess.call(["./build-ios-curl.sh"])

  os.chdir(old_cur)
  return