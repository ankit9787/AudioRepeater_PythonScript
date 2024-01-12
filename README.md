# AudioRepeater_PythonScript

This solves problem where you want to run video into local windows media player and share its audio over Google meet call, but you can't keep mic as unmute because it might send other users sound too with movie sound and there is no straight way to share audio of VLC or media players to zoom or google meet
So, follow below steps to enjoy your local teleparty apps setup, watch movie in your local and other person can watch it over google meet call (not zoom because free zoom only gives 40 min access), and yes there ins one way to run video in chrome browser and share the tab, but if we attach external subtitles to it, which can only be done in media players not when playing video from chrome then we stuck how to share media player audio to zoom calls or google meet calls

## Steps to mitiage above issue--
- Download any VB cable application one is- VB cable virtual audio cable
- Now goto audio settings to check that you can see that cable as audio device like other devices like realtek speaker, microphone (where to check, for above two steps check over internet unlimited solutions avble)
- Now goto VLC, select your video
- And got top menu in VLC - GOTO tools - preferences
- A dialog box open goto audio - under device dropdown select - Vb cable
- Now at this step you will not be able to listen audio because VLC treating VB able as some speaker and sending audio there
- Now to share audio over google meet call, goto google meet
- share VLC screen, unmute yourself, click on three dots in menu
- CLick on setting - a dialog box comes - click on microphone - select same VB cable
- Now at this step VLC sending same sound to VB cable, and google meet listening from there only so sorted
- Now primary user not able to listen any audio, so now comes the concept of audio repeaters which repeat audio between multiple device
- so think of this way right now all audio going into vb cable we need to listen same audio from windows speaker
- so we will use above script, run first script python script to get devices and their IDs name and sample rate
- and then run second python script to pass input id and output device id which has same sample rate and voila audio coming from speaker also and shared over zoom call also
- to run python script python script name
