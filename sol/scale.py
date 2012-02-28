#####################################################################################
#                                                                                   #
# sol/scale.py                                                                      #
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


from sol import tts
from sol.utils import GetOnlyObject


class Scale(GetOnlyObject):
    """Scale objects are constructed from three pieces:
        - A mode sequence
        - A tonic
        - A tone system

        Steps and pitches can then be looked up using step() and pitch().
        Similar to the System class, you can use array notation (scale[2])

        Arguments:
            mode                A sequence of step intervals
            tonic="C4"          A step number or note name to use as tonic
            system=sol.tts      A System object to use, defaults to the shared
                                TwelveToneSystem object

        Example initialization:  
            from sol.scale import Scale
            from sol import mode
            c_dorian = Scale(mode.dorian, 'C4')
    """
    def __init__(self, mode=None, tonic='C4', system=tts, name=None, pitchMode=False):
        if not mode:
            raise TypeError("Must specify a mode sequence to use.")
        self.mode = mode
        self.system = system
        self.name = name
        self.pitchMode = pitchMode

        # Parse tonic
        self.tonic = tonic
        if isinstance(self.tonic, str):
            self.tonic = self.system.step(self.tonic)

        # Step table memoizes step lookups
        self._steptable = {}

    def __unicode__(self):
        if self.name:
            return self.name
        return "Scale: %s - %s" % (tonic, mode, )

    def __getitem__(self, key):
        """Provides a shortcut to step lookup.

        If pitchMode=True, then returns a pitch instead of a step
        """
        if self.pitchMode:
            return self.pitch(key)
        return self.step(key)

    def pitch(self, scale_degree):
        """Return a pitch from a scale degree"""
        return self.system.pitch(self.step(scale_degree))

    def step(self, scale_degree):
        """Return a step from a scale degree"""
        # Adjust scale degree by 1 since we want tonic to = 1
        scale_degree -= 1
        if self._steptable.has_key(scale_degree):
            return self._steptable[scale_degree]
        octave_size = sum(self.mode)
        base_step = octave_size * int((scale_degree / len(self.mode)))
        return self.tonic + base_step + sum(self.mode[:scale_degree % len(self.mode)])
