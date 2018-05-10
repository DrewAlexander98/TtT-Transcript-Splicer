from pydub import AudioSegment
from pydub.utils import make_chunks
from glob import glob
import pysrt

def main():
    epNum = str(input("Enter episode number: "))
    audioFile, textFile = getEpisode(epNum)
    text = pysrt.open(textFile)
    spliceAudio(audioFile, "mp3", text, epNum)
    

def getEpisode(epNum):
   audioPath = glob('Audio/'+str(epNum)+'*.*')
   if audioPath == []:
       print("Could not locate audio")
       return None
   textPath = glob('Text/'+str(epNum)+'*.*')
   if textPath == []:
       print("Could not locate text")
       return None
   return audioPath[0], textPath[0]

def toMilli(time):
    timeMilli = time.hours*3600000
    timeMilli += time.minutes*60000
    timeMilli += time.seconds*1000
    timeMilli += time.milliseconds
    return timeMilli
    
def getTime(text, index):
    timeStart = toMilli(text[index].start)
    timeEnd = toMilli(text[index].end)
    time = [timeStart, timeEnd]
    print(text[index].text)
    print(timeStart, timeEnd)
    return time
    
def spliceAudio(fileName, fileType, text, epNum):
    if fileName == []:
        print("Could not locate audio file")
        return None
    AudioSegment.converter = "./ffmpeg"
    audioFile = AudioSegment.from_file(fileName, fileType)
    for i in range(len(text)):
    #for i in range(50):
        time = getTime(text, i)
        if time[1]-time[0] <= 1500:
            clip = audioFile[time[0]-750:time[1]+750]
        else:
            clip = audioFile[time[0]-200:time[1]+200]
        exportClip(clip, i+1, "mp3", epNum)
    
def exportClip(clip, clipNum,  fileType, epNum): 
    #Export all of the individual clips as mp3 files
        clip_name = "ExportedAudio/{0}Clip{1}.{2}".format(clipNum, epNum, fileType)
        print("exporting", clip_name)
        clip.export(clip_name, format=fileType)
