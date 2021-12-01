
import subprocess
import os

class seminar_2:
    """ class to englobe all the exercises"""

    def __init__(self, video, subtitles):
        self.video = video
        self.subtitles = subtitles

    # output a video that will show the macroblocks and the motion vectors
    def exercise_1(self):
        cmd = ["ffplay", "-flags2", "+export_mvs", self.video, "-vf", "codecview=mv=pf+bf+bb"]
        subprocess.check_output(cmd)

    # new BBB container, cut into 1 minute, export 1min mp3 stereo track
    # cut into 1 minute, export 1min aac lower bitrate
    def container_mp4(self):
        #cut BBB video into 1 min
        cmd = "ffmpeg -i {} -ss 00:00:00 -to 00:01:00 -c copy output_video.mp4".format(self.video)
        os.system(cmd)
        #without audio?
        # "ffmpeg -i output_video.mp4 -c copy -an only_video.mp4"
        # from mp4 to mp3
        cmd = "ffmpeg -i output_video.mp4 output_audio.mp3" #the resulting audio will be in stereo format
        os.system(cmd)
        # export audio in AAC lower bitrate
        cmd = "ffmpeg -i output_audio.mp3 -map 0:a:0 -b:a 16k lowbitrate.aac" #16k will reduce the bit rate
        os.system(cmd)
        # package all in a mp4 container
        cmd = "ffmpeg -i output_video.mp4 -i output_audio.mp3 -i lowbitrate.aac -map 0 -map 1 -map 2 -c copy container.mp4"
        os.system(cmd)

    # read the tracks from an MP4 container
    def read_mp4_container(self):
        cmd = "ffprobe -loglevel 0 -print_format json -show_format -show_streams container.mp4"
        os.system(cmd)

    # download subtitles, integrate them and output a video with printed subtitles
    def print_subtitles(self):
        cmd = "ffmpeg -i {} -vf 'subtitles={}' subtitled_video.mp4".format(self.video, self.subtitles)
        os.system(cmd)


#main
if __name__ == '__main__':

    BBB_video = "BBB.mp4"
    video_shorted = "BBB_12s.mp4"
    unsubtitled_video = "myvideo.mp4"
    subtitles = "sub.srt"

    print("Let's keep on working! You are amazing, you should believe in yourselves! \n"
          "What do you want to do? \n"
          "[1] show macroblocks and motion vectors \n"
          "[2] create a BBB container \n"
          "[3] read the tracks \n"
          "[4] print subtitles")
    answer = input("Type 1, 2, 3 or 4: ")

    if answer == "1":
        print("macroblocks and motion vectors")
        e1 = seminar_2(video_shorted, subtitles)
        e1.exercise_1()

    elif answer == "2":
        print("new BBB container with: ....")
        e2 = seminar_2(BBB_video, subtitles)
        e2.container_mp4()

    elif answer == "3":
        print("read mp4 container")
        e3 = seminar_2(BBB_video, subtitles)
        e3.read_mp4_container()

    elif answer == "4":
        print("print subtitles Eternals")
        e4 = seminar_2(unsubtitled_video, subtitles)
        e4.print_subtitles()

    else:
        option = input("Incorrect! Please, introduce 1, 2, 3 or 4: ")

