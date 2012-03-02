#####################################################################################
#                                                                                   #
# sol/mode.py                                                                       #
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


def rotate(seq, n):
    return seq[n:] + seq[:n]

diatonic    = [2, 2, 1, 2, 2, 2, 1]

ionian      = rotate(diatonic, 0)
dorian      = rotate(diatonic, 1)
phrygian    = rotate(diatonic, 2)
lydian      = rotate(diatonic, 3)
mixolydian  = rotate(diatonic, 4)
aeolean     = rotate(diatonic, 5)
locrian     = rotate(diatonic, 6)

harmonic    = [2, 1, 2, 2, 1, 3, 1]

melodic     = [2, 1, 2, 2, 2, 2, 1]
