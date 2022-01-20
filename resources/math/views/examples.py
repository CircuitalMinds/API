from requests import get
from os import system
import pylab
import imageio
from PIL import Image, ImageDraw


def covid19(country=None):
    api = "https://covid19.mathdro.id/api"
    if country is None:
        data = get(api).json()
        data.update({
            'countries': country['name'] for country in get(f"{api}/countries").json()['countries']
        })
        return data
    else:
        country = country[0].upper() + country[1:]
        data = get(f"{api}/countries/{country}").json()
        return data


def video_corverter(video_path, out_extension='wav'):
    system(
        f'ffmpeg -i {video_path} {video_path.replace("mp4", out_extension)}'
    )


def build_video_frames(file_path, frames=8, interval=256):
    file_data = imageio.get_reader(file_path,  'ffmpeg')
    for i in range(0, frames * interval, interval):
        image = file_data.get_data(i)
        fig = pylab.figure()
        fig.suptitle('image #{}'.format(i), fontsize=20)
        pylab.imshow(image)
        pylab.show()


def spectrum(video_path):
    from scipy.io import wavfile
    import matplotlib.pyplot as plt
    import numpy as np
    import warnings
    warnings.filterwarnings("ignore")
    filename = "../tempo_rubato.wav"
    m = 10 ** 4
    n, video_data = wavfile.read(filename)
    fn = m * np.fft.rfft(video_data[:m]) / n
    print(fn)
    plt.plot(fn)
    plt.show()


def create_gif():
    images = []
    width = 200
    center = width // 2
    color_1 = (0, 255, 0)
    color_2 = (255, 0, 0)
    max_radius = int(center * 1.5)
    step = 2
    for i in range(0, max_radius, step):
        im = Image.new('RGB', (width, width), color_2)
        draw = ImageDraw.Draw(im)
        draw.ellipse((center - i, center - i,
                      center + i, center + i),
                     fill=color_1)
        images.append(im)
    images[0].save('pillow_imagedraw.gif', append_images=images[1:], save_all=True)

#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
##!/usr/bin/python

# numpy is required to do the FFT and iFFT
import numpy
# sys is required in order to read command line arguments
import sys
# this tests whether scipy is installed and working properly
# scipy isn't a necessity for the FFT results but it is for the
# integratin of the FFT peaks, and writing of output .wav files
# after removing certain frequencies from the FFT data.
try:
    from scipy import interpolate
    import scipy.io.wavfile
    tfscipy=True
except:
    tfscipy=False

# fname is the file name in .wav format ONLY!
fname=sys.argv[1]

# range around fundamental and overtone peaks in the frequency spectrum over which to integrate
spread=5.

# names of the overtone notes
notes=["empty for python","A ", "A ", "E ", "A ", "C#", "E ", "G ", "A ", "B ", "C#", "D ", "E ", "F#", "G ", "G#", "A ", "Bb", "B ", "C ", "C#"]

# in case the scipy is broken but it was imported succesfully (it happens sometimes)
try:
    frequency,audio=scipy.io.wavfile.read(fname+'.wav')
except:
    print
    print "You do not have a working copy of scipy on your computer or you're analyzing a .wav file that doesn't have a header. If you don't have scipy the integrated data will have 1.000000 to fill the space, but it doesn't mean anything. The important thing to make sure you have done is to delete the first line of the .wav file you are trying to analyze. Don't use WORD, but something like Notepad or Wordpad, which ever actually shows you that there is more than 1 line in the file and won't force you to change the file's extension to something other than .wav, use that to delete the first line. Otherwise, that output of this is script will be garbage. Or, you can install scipy and have no troubles! If your .wav file is mono instead of stereo make sure you are passing the word 'mono' as an argument when you invoke this script, e.g. \"python dofft.py _filename_ mono bass tenor\". If you fail to do that the frequencies will come out all funny. If you do have scipy and just happen to have deleted the header in the .wav file, you know, make sure you still put mono if it isn't stereo but all the other functionality like integration and writing the inverse wave file should be fine."
    try:
        tempaudio=numpy.fromfile(fname+'.wav',dtype=numpy.int16)
        print len(tempaudio)
        if 'mono' not in sys.argv:
            audio=tempaudio[range(0,len(tempaudio),2)]
            print audio
        else:
            audio=tempaudio
        # frequency is the frequency at which the file was recorded
        frequency=44100
    except:
        print
        print "Either you don't have numpy installed or you forgot to put the file name prefix (without the .wav!) as the first argument to the program, eg. \"python dofft.py _filename_ bass tenor\" to analyze filename.wav. This script doesn't do anything without the minimum requirement of numpy."
        sys.exit()

time=len(audio)*(1./frequency)
if tfscipy == False:
    print
    print "Your file should be %g seconds long. If this is half the length of the audio in your file then you need to specify 'mono' as a command line argument after the name of the file when you invoke this script. Or maybe it was recorded at a different frequency other than 44.1 kHz."%time
else:
    print
    print "Your file should be %g seconds long."%time

if audio[0].dtype == 'int16':
    inverseft=numpy.fft.fft(audio,len(audio))
else:
    print
    print "You have imported a .wav file that is in stereo, only the left channel will be analyzed"
    inverseft=numpy.fft.fft(audio[:,0],len(audio[:,0]))

ft=inverseft.copy()
ft=numpy.abs(ft)

freq=numpy.fft.fftfreq(len(audio),1./frequency)
offsetarg=int(spread/freq[1])+1

if 'bass' in sys.argv and 'tenor' in sys.argv:
    lowindex=numpy.argmin(abs(freq-100.))
    bassindex=numpy.argmin(abs(freq-175.))
    bassfundamentalarg=lowindex+numpy.argmax(ft[lowindex:bassindex])
    bassfundamental=freq[bassfundamentalarg]
    lowindex=numpy.argmin(abs(freq-200.))
    tenorindex=numpy.argmin(abs(freq-275.))
    tenorfundamentalarg=lowindex+numpy.argmax(ft[lowindex:tenorindex])
    tenorfundamental=freq[tenorfundamentalarg]

    for j in range(1,21,1):

        upperbound=j*bassfundamentalarg+offsetarg
        lowerbound=j*bassfundamentalarg-offsetarg
        overtonearg=j*bassfundamentalarg-offsetarg+numpy.argmax(ft[lowerbound:upperbound])

        if tfscipy == True:
            interpolated=interpolate.splrep(freq[lowerbound-5:upperbound+6],ft[lowerbound-5:upperbound+6],k=1,s=0)
            integrated=interpolate.splint(freq[lowerbound],freq[upperbound+1],interpolated)
        else:
            integrated=1.
        if j == 1:
            bassfundintegrated=integrated
            if '%i'%j in sys.argv:
                inverseft[lowerbound:upperbound+1]=0.0
                inverseft[-upperbound-1:-lowerbound]=0.0
            print
            print "             |      | ratio |  ratio  |  ratio  |  ratio  |      |     "
            print "             |      |  to   |   to    |   to    |   to    |      |     "
            print "             |      | bass  |  bass   |  tenor  |  tenor  |      |     "
            print "             |      | funda-|  funda- |  funda- |  funda- | bass | tenor"
            print "             |      | mental|  mental |  mental |  mental | over-| over-"
            print "             | note | peak  |  peak   |  peak   |  peak   | tone | tone"
            print "frequency    | name | height|  area   |  height |  area   |number|number"
            print "------------------------------------------------------------------------"
            print "%f Hz (%s)  %f  %f                       %i       -"%(bassfundamental,notes[j],ft[overtonearg]/ft[bassfundamentalarg],integrated/bassfundintegrated,j)
        elif j == 2:
            tenorfundintegrated=integrated
            if '%i'%j in sys.argv:
                inverseft[lowerbound:upperbound+1]=0.0
                inverseft[-upperbound-1:-lowerbound]=0.0
            print "%f Hz (%s)  %f  %f                       %i       %i"%(freq[overtonearg],notes[j],ft[overtonearg]/ft[bassfundamentalarg],integrated/bassfundintegrated,j,j-1)
        elif j > 2 and float(j)%2 == 0:
            if '%i'%j in sys.argv:
                inverseft[lowerbound:upperbound+1]=0.0
                inverseft[-upperbound-1:-lowerbound]=0.0
            print "%f Hz (%s)  %f  %f  %f  %f   %i       %i"%(freq[overtonearg],notes[j],ft[overtonearg]/ft[bassfundamentalarg],integrated/bassfundintegrated,ft[overtonearg]/ft[tenorfundamentalarg],integrated/tenorfundintegrated,j,j/2)
        else:
            if '%i'%j in sys.argv:
                inverseft[lowerbound:upperbound+1]=0.0
                inverseft[-upperbound-1:-lowerbound]=0.0
            print "%f Hz (%s)  %f  %f                       %i       -"%(freq[overtonearg],notes[j],ft[overtonearg]/ft[bassfundamentalarg],integrated/bassfundintegrated,j)

    if tfscipy == True and 'inverse' in sys.argv:
        inverseaudio=numpy.real(numpy.fft.ifft(inverseft))
        inverseaudio=numpy.int16(inverseaudio*((2.**15-1.)/numpy.max(numpy.abs(inverseaudio))))
        scipy.io.wavfile.write(fname+'_inverse.wav',frequency,inverseaudio)

elif 'bass' in sys.argv and 'tenor' not in sys.argv:
    lowindex=numpy.argmin(abs(freq-100.))
    bassindex=numpy.argmin(abs(freq-175.))
    bassfundamentalarg=lowindex+numpy.argmax(ft[lowindex:bassindex])
    bassfundamental=freq[bassfundamentalarg]

    for j in range(1,11,1):

        upperbound=j*bassfundamentalarg+offsetarg
        lowerbound=j*bassfundamentalarg-offsetarg
        overtonearg=j*bassfundamentalarg-offsetarg+numpy.argmax(ft[lowerbound:upperbound])

        if tfscipy == True:
            interpolated=interpolate.splrep(freq[lowerbound-5:upperbound+6],ft[lowerbound-5:upperbound+6],k=1,s=0)
            integrated=interpolate.splint(freq[lowerbound],freq[upperbound+1],interpolated)
        else:
            integrated=1.
        if j == 1:
            bassfundintegrated=integrated
            if '%i'%j in sys.argv:
                inverseft[lowerbound:upperbound+1]=0.0
                inverseft[-upperbound-1:-lowerbound]=0.0
            print
            print "height of bass fundamental peak at %g Hz (%s) is %g and it integrates to %g"%(bassfundamental,notes[j],ft[bassfundamentalarg],integrated)
        else:
            if '%i'%j in sys.argv:
                inverseft[lowerbound:upperbound+1]=0.0
                inverseft[-upperbound-1:-lowerbound]=0.0
            print "the ratio of the bass overtone %i at %g Hz (%s) to the fundamental height is %g and area is %g"%(j,freq[overtonearg],notes[j],ft[overtonearg]/ft[bassfundamentalarg],integrated/bassfundintegrated)

    if tfscipy == True and 'inverse' in sys.argv:
        inverseaudio=numpy.real(numpy.fft.ifft(inverseft))
        inverseaudio=numpy.int16(inverseaudio*((2.**15-1.)/numpy.max(numpy.abs(inverseaudio))))
        scipy.io.wavfile.write(fname+'_inverse.wav',frequency,inverseaudio)

elif "bass" not in sys.argv and 'tenor' in sys.argv:
    lowindex=numpy.argmin(abs(freq-200.))
    tenorindex=numpy.argmin(abs(freq-275.))
    tenorfundamentalarg=lowindex+numpy.argmax(ft[lowindex:tenorindex])
    tenorfundamental=freq[tenorfundamentalarg]

    for j in range(1,11,1):

        upperbound=j*tenorfundamentalarg+offsetarg
        lowerbound=j*tenorfundamentalarg-offsetarg
        overtonearg=j*tenorfundamentalarg-offsetarg+numpy.argmax(ft[lowerbound:upperbound])

        if tfscipy == True:
            interpolated=interpolate.splrep(freq[lowerbound-5:upperbound+6],ft[lowerbound-5:upperbound+6],k=1,s=0)
            integrated=interpolate.splint(freq[lowerbound],freq[upperbound+1],interpolated)
        else:
            integrated=1.
        if j == 1:
            tenorfundintegrated=integrated
            if '%i'%j in sys.argv:
                inverseft[lowerbound:upperbound+1]=0.0
                inverseft[-upperbound-1:-lowerbound]=0.0
            print
            print "height of tenor fundamental peak at %g Hz (%s) is %g and it integrates to %g"%(tenorfundamental,notes[j],ft[tenorfundamentalarg],integrated)
        else:
            if '%i'%j in sys.argv:
                inverseft[lowerbound:upperbound+1]=0.0
                inverseft[-upperbound-1:-lowerbound]=0.0
            print "the ratio of the tenor overtone %i at %g Hz (%s) to the fundamental height is %g and area is %g"%(j,freq[overtonearg],notes[j],ft[overtonearg]/ft[tenorfundamentalarg],integrated/tenorfundintegrated)

    if tfscipy == True and 'inverse' in sys.argv:
        inverseaudio=numpy.real(numpy.fft.ifft(inverseft))
        inverseaudio=numpy.int16(inverseaudio*((2.**15-1.)/numpy.max(numpy.abs(inverseaudio))))
        scipy.io.wavfile.write(fname+'_inverse.wav',frequency,inverseaudio)

else:
    print "You didn't specify what to analyze in the file!"

file=open(fname+'.txt','w')
for i in range(len(ft)):
    file.write('%g %g\n'%(freq[i],ft[i]))
file.close()

file=open(fname+'.plt','w')
# next line MacOS X only, probably
#file.write('set term x11\n')
file.write('set logscale x\n')
file.write('set xrange[100:3000]\n')
file.write('plot "'+fname+'.txt" u 1:2 w lp\n')
file.write('pause -1\n')
file.close()
