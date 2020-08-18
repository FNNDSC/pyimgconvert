#System imports
import os, sys

# Project specific imports
import      pfmisc
from        pfmisc._colors      import  Colors
from        pfmisc.debug        import  debug
from        pfmisc              import  other
from        pfmisc              import  error
import argparse
import pudb

class pyimgcovert(object):
    """
        A class based on "magick convert" that accepts CLI arguments that need to be passed 
        to the Linux CLI utility to convert images to required outputs.
    """

    def __init__(self, **kwargs):
        """
        A block to declare self variables
        """

        self.str_desc                   = ''
        self.__name__                   = "pyimgconvert"
        self.str_version                = "1.0.0"
        self.verbosity                  = 1
        self.dp                         = pfmisc.debug(
                                            verbosity   = self.verbosity,
                                            within      = self.__name__
                                            )

         # Directory and filenames
         str_inputDir                   = ''
         str_outputDir                  = ''
         str_args                       = ''
        
         for key, value in kwargs.items():
            if key == "inputDir":              self.str_inputDir              = value
            if key == "outputDir":             self.str_outputDir             = value
            if key == "args":                  self.args                      = value

        def img_convert(self):
