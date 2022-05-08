import xmltodict
import math
from datetime import timedelta

'''
Read de xspf (“spiff”) file and build the xspf string with XML info
'''
def readXspfFile(xspfPath):
    xspfStr = ''
    with open(xspfPath, 'r') as xspfFile:
        #print(xspfFile)
        for line in xspfFile:
            #print(line)
            xspfStr +=  line
    return xspfStr

'''
Parse the xspfStr into a Dictionary
Use force_list=('trackList',) to organize the Dictionary in tracks
'''
def xspfStrParse(xspfStr):
    xspfDict = xmltodict.parse(xspfStr, force_list=('trackList',))
    #print(xspfDict)
    return  xspfDict

'''
Returns the track lentgth in Music Brainz format "(2:23)"
'''
def trackLength(duration):
    #trackDuration =  math.trunc(duration / 1000)
    trackDuration =  duration / 1000
    mins, secs = divmod(round(trackDuration,0), 60)
    mins = math.trunc(mins)
    secs = math.trunc(secs)
    return "(" + str(mins) + ":" + f"{secs:02}" + ")"

'''
Extract the different levels of the xspf record info to get the tracks root
'''
def printMBtrackList(xspfDict):
    playlistDict = xspfDict['playlist']
    trackListDict = playlistDict['trackList']
    for trackListNo in range(len(trackListDict)):
        #print(trackListDict[trackListNo])
        trackDict = trackListDict[trackListNo]['track']
        '''
        Process the track info to create the MusicBrainz TrackList for Adding Meduim by "Manual entry" mode
        '''
        for trackNo in range(len(trackDict)):
            #print(trackDict)
            #1. Love Me Do - The Beatles (2:23)
            strTrack = str(trackNo+1) + ". " + trackDict[trackNo]['title'] + " - " + trackDict[trackNo]['creator'] + " " + trackLength(float(trackDict[trackNo]['duration']))
            print(strTrack)
            '''
            for key, value in trackDict[trackNo].items():
                print("-------",key,':', value)
            '''

def main():
    xspfPath = '/home/ipserc/Audacious/Desatinos_Desplumados.xspf'
    #xspfPath = '/home/ipserc/Audacious/Mi_Vida_En_Marte.xspf'
    xspfStr = readXspfFile(xspfPath)
    xspfDict = xspfStrParse(xspfStr)
    printMBtrackList(xspfDict)

if __name__ == "__main__":
    main()
