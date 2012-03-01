#####################################################################################
#                                                                                   #
# sol/system.py                                                                     #
#                                                                                   #
# Copyright (c) 2012 Josh Bothun <joshbothun@gmail.com>                             #
#                                                                                   #
# Permission is hereby granted, free of charge, to any person obtaining a copy of   #
# this software and associated documentation files (the "Software"), to deal in     #
# the Software without restriction, including without limitation the rights to      #
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies     #
# of the Software, and to permit persons to whom the Software is furnished to do    #
# so, subject to the following conditions:                                          #
#                                                                                   #
# The above copyright notice and this permission notice shall be included in all    #
# copies or substantial portions of the Software.                                   #
#                                                                                   #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR        #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS  #
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR    #
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER    #
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN           #
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.        #
#                                                                                   #
#####################################################################################

import os
import urllib

class System(object):
    """Tone system that provides a mapping from steps to pitches

    Keyword Arguments:
        octaves     number of octaves to subdivide
        divisions   number of subdivisions per octave
        root=27.5   pitch value for A0 
    """
    def __init__(self, octaves=None, divisions=None, root=27.5, name=None):
        # Parse args
        if not all((octaves, divisions)):
            raise TypeError("Must specify number of octaves and divisions.")
        self.octaves = octaves
        self.divisions = divisions
        self.root = root
        self.name = name
        
        # Pitch table memoizes pitch lookups
        self._pitchtable = {}

    def __unicode__(self):
        if self.name:
            return self.name
        return "System: %s/%s" % (self.divisions, self.octaves, )

    def __setitem__(self, key, val):
        """Defined so we can raise a more useful error"""
        raise TypeError("Pitch table is read-only")

    def __getitem__(self, key):
        """Provides a shortcut to multiple pitch conversion methods"""
        if isinstance(key, str):
            return self.stringToPitch(key)
        return self.stepToPitch(key)

    def stepToPitch(self, step):
        """Convert a step value into a pitch value in hz"""
        assert isinstance(step, int), "Steps must be integers"
        if self._pitchtable.has_key(step):
            return self._pitchtable[step]
        pitch = (1 + self.octaves) ** (step / float(self.divisions)) * self.root
        self._pitchtable[step] = pitch
        return pitch

    def stringToPitch(self, string):
        raise NotImplementedError("This system hasnt implemented stringToPitch")


