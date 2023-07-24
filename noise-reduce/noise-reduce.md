# noise-reduce.py

To make a noise reduction algorithm should be easy. It's all about taking a noise sample and removing portions of the track that "sound like" the sample, right? 

## Background

When I make recordings, the mic always catches the sound of the computer fan, a soft whirr that drowns out the /f/ and /s/ speech sounds. My voice is high-pitched, so Adobe Audition noise reduction often gives my voice a robotic effect and/or makes it hard to understand. I also wanted to reduce the multiplicative noise (echoes). Having read some information about different mechanisms of noise reduction, I decided to write a program myself, but the Python code refused to give a sensible result. It turned out that I had made almost every common beginner mistake.

## Code crimes

In broad strokes:
* Handling 32-bit and 64-bit integers;
* Not splitting a stereo track to mono;
* The entire noise reduction part is overly naive.

### A detailed recount

1. Ironically, the initial version of noise-reduce.py converts the input sound into complete noise. This is caused by pydub's handling of audio data, as stated in Issue #247.

  As the fix mentioned in that issue didn't work for me, I found out to make an array for the samples and put the values there. 

  I changed line 25 to 

  ```denoised_samples = array("h", [])```

  and line 41 to 

  ```denoised_samples += array("h", [int(value) for value in denoised_ifft.real])```

  Now the resulting audio could be said to _vaguely_ resemble the input. However, it is distorted beyond recognition.

2. With the bit problem fixed, the result is a distorted version of the original sound. After a lot of clueless meddling, I exported the sound and noticed that the length is exactly twice of that of the original. Then I reread the tutorial, and a line finally caught my attention:

 > Note: if the audio has multiple channels, the samples for each channel will be serialized – for example, stereo audio would look like [sample_1_L, sample_1_R, sample_2_L, sample_2_R, …]

  I now understand the old joke of highlighting every sentence in a textbook. In addition, the highlight may not stay on paper only; it must be interalized.

  By adding 

  ```voice_mono = voice_orig.split_to_mono()[0]```

  and replacing all other instances of `voice_orig` with `voice_mono`, the speed issue is fixed. Not that the noise reduction is achieved.

3. The output now sounds like the original recording. However, it now has a wobbly effect, as if the speaker is talking at a microphone behind an electric fan. In addition, not a bit of the noise is reduced. 

### Miscellaneous

There are still many unanswered questions. For example, I sometimes got this mysterious error:
```
Traceback (most recent call last):
  File "D:\working-path\0-noise-reduce.py", line 66, in <module>
    voice_denoised = voice_denoised._spawn(denoised_samples)
  File "C:\Users\third\AppData\Local\Programs\Python\Python310\lib\site-packages\pydub\audio_segment.py", line 411, in _spawn
    data = b''.join(data)
TypeError: sequence item 0: expected a bytes-like object, int found
```
The passed "data" was an array defined by
denoised_samples = array("h", \[int(i.real) for i in denoised_ifft])
Usually, I ran a test with
A = array("h", [(i%2000-1000)*10 for i in range(44100)])
a = a._spawn(A)
play(a)
and it would work normally.
Then I reran the program and the error would disappear and the sound would play normally.
