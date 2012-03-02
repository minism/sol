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

import re


# A0 value for 440 tuning
STANDARD_A0 = 27.5


class System(object):
    """Tone system that provides a mapping from steps to pitches

    Keyword Arguments:
        octaves     number of octaves to subdivide
        divisions   number of subdivisions per octave
        root=27.5   pitch value for A0 
    """
    def __init__(self, octaves=None, divisions=None, root=None, name=None):
        # Parse args
        if not all((octaves, divisions)):
            raise TypeError("Must specify number of octaves and divisions.")
        if not root:
            root = STANDARD_A0
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

    def stringToPitch(self, note_name):
        raise NotImplementedError("This system hasnt implemented stringToPitch")


class TwelveToneSystem(System):
    """Standard twelve tone system with note name string parsing

    Keyword Arguments:
        root=27.5   pitch value for A0
    """
    step_table = {
        'A': 0,
        'B': 2,
        'C': 3,
        'D': 5,
        'E': 7,
        'F': 8,
        'G': 10,
    }
    note_re = re.compile(r'^([A-G])(#*|b*)(\d)+$')

    def __init__(self, root=None):
        super(TwelveToneSystem, self).__init__(octaves=1, divisions=12, root=root)

    def stringToPitch(self, note_name):
        match = re.match(self.note_re, note_name)
        if not match:
            raise TypeError("Invalid note name: %s" % note_name)
        letter = match.group(1)
        mod = match.group(2)
        octave = int(match.group(3))
        step = self.divisions * octave + self.step_table[letter]
        for token in mod:
            step += token == '#' and 1 or -1
        return step
