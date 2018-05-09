from pydub import AudioSegment
from pydub.utils import make_chunks
from glob import glob
import pysrt

def main():
    epNum = str(input("Enter episode number: "))
    audioFile, textFile = getEpisode(epNum)
    print(audioFile, textFile)

def getEpisode(epNum):
   audioPath = glob('Audio/'+str(epNum)+'*.*')
   if audioPath == []:
       print("Could not locate audio")
       return None
   textPath = glob('Text/'+str(epNum)+'*.*')
   if textPath == []:
       print("Could not locate text")
       return None
   return audioPath, textPath

def toMilli(time):
    timeMilli = time.hours*3600000
    timeMilli += time.minutes*60000
    timeMilli += time.seconds*1000
    timeMilli += time.milliseconds
    return timeMilli
    
def getTimes(textFile, index):
    text = pysrt.open(textFile)
    timeStart = toMilli(text[index].start)
    timeEnd = toMilli(text[index].end)
    time = [timeStart, timeEnd]
    print(text[index].text)
    return time

    
def spliceAudio(fileName, fileType, time):
    if fileName == []:
        print("Could not locate audio file")
        return None
    AudioSegment.converter = "./ffmpeg"
    audioFile = AudioSegment.from_file(fileName, fileType)
    clip = audioFile[time[0]:time[1]]
    clip.export("testClip", format=fileType)
    #exportClips(clips, mp3)
    
def exportClips(clips, fileType): 
    #Export all of the individual chunks as mp3 files
    for i, clip in enumerate(clips):
        clip_name = "{0}Clip.{1}".format(i, fileType)
        print("exporting", clip_name)
        clip.export(clip_name, format=fileType)
