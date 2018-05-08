from pydub import AudioSegment
from pydub.utils import make_chunks
from glob import glob


def main():
    epNum = str(input("Enter episode number: "))
    audio, text = getEpisode(epNum)
    print(audio, text)


def getEpisode(epNum):
   audioPath = glob('Audio/'+epNum+'*.wav')
   textPath = glob('Text/'+epNum+'*.*')
   return audioPath, textPath

def spliceAudio(fileName, fileType):
    if fileName == []:
        print("Could not locate audio file")
        return None
    audioFile = AudioSegment.from_file(fileName, fileType) 
    clip_length_ms = 1000 # pydub calculates in millisec
    clips = make_chunks(audioFile, clip_length_ms) #Make chunks of one sec
    clips[0].export("testClip", format=fileType)
    #exportChuncks(chunks)
    
def exportClips(clips, fileType): 
    #Export all of the individual chunks as mp3 files
    for i, clip in enumerate(clips):
        clip_name = "{0}Clip.{1}".format(i, fileType)
        print("exporting", clip_name)
        clip.export(clip_name, format=fileType)
