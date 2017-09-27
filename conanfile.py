from conans import ConanFile, CMake
import os

class PlexMediaPlayer(ConanFile):
  settings = "os", "compiler", "build_type", "arch"
  options = {"include_desktop": [True, False]}
  default_options = "include_desktop=True"
  generators = "cmake"

  def requirements(self):
    self.requires("web-client-tv/3.13.2-56c55e3@plex/public")

    if self.options.include_desktop:
      self.requires("web-client-desktop/3.20.6-b82494d@plex/public")
