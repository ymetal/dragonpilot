#!/usr/bin/env python2.7
import os
import json

file = '/data/dragonpilot.json'

class dragonpilot():

  def __init__(self):
    self.conf = self.read()

  def read(self):
    has_new_def = False
    config = {}
    if not os.path.isfile(file):
      self.write(config)

    with open(file, 'r') as f:
      config = json.load(f)

    if "turnSignalDisableSteer" not in config:
      config["turnSignalDisableSteer"] = False
      has_new_def = True

    if has_new_def:
      self.write(config)

    return config

  def write(self, config):
    with open(file, 'w') as f:
      json.dump(config, f, indent=2, sort_keys=True)
      os.chmod(file, 0644)

if __name__ == "__main__":
  dragonpilot = dragonpilot()
