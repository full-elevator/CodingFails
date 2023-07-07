# noise-reduce.py

To make a noise reduction algorithm should be easy. It's all about taking a noise sample and removing portions of the track that "sound like" the sample, right? 

## Background

When I make recordings, the mic always catches the sound of the computer fan, a soft whirr that drowns out the /f/ and /s/ speech sounds. My voice is high-pitched, so Adobe Audition noise reduction often gives my voice a robotic effect and/or makes it hard to understand. I also wanted to reduce the multiplicative noise (echoes). Having read some information about different mechanisms of noise reduction, I decided to write a program myself, but the Python code refused to give a sensible result. It turned out that I had made almost every common beginner mistake.

## Code crimes

In broad strokes:
* Handling 32-bit and 64-bit integers;
* Not splitting a stereo track to mono;
* The entire noise reduction part is overly naive.

There are still many unanswered questions. For example, I sometimes got this mysterious error:
Traceback (most recent call last):
  File "D:\DqobraLatin\WirusDOqopus\0-noise-reduce.py", line 66, in <module>
    voice_denoised = voice_denoised._spawn(denoised_samples)
  File "C:\Users\third\AppData\Local\Programs\Python\Python310\lib\site-packages\pydub\audio_segment.py", line 411, in _spawn
    data = b''.join(data)
TypeError: sequence item 0: expected a bytes-like object, int found
The passed "data" was an array defined by
denoised_samples = array("h", \[int(i.real) for i in denoised_ifft])
Usually, I ran a test with
A = array("h", [(i%2000-1000)*10 for i in range(44100)])
a = a._spawn(A)
play(a)
and it would work normally.
Then I reran the program and the error would disappear and the sound would play normally.
