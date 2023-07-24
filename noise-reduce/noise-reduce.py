## This version is an example that turns the input to noise completely.
## A full explanation is found at noise-reduce.md.

import numpy as np
from pydub import AudioSegment
from pydub.playback import play

def plot_samples(samples, n):
    from matplotlib import pyplot as plt
    plt.figure(1, figsize=(7.2,5.4))
    X = np.arange(n, dtype=int)
    plt.plot(X, samples[:n])
    plt.show()

voice_orig = AudioSegment.from_wav("speech-mild-noise.wav")
voice_samples = voice_orig.split_to_mono()
clip_len = 100
vertical_scale = 0.5    #prevent overflow
#taking the noise samples from 1s to 1.1s
noise = voice_orig[1000:1000+clip_len]
print("length of sound is", len(voice_orig))
noise_samples = noise.get_array_of_samples()
fft_noise = np.fft.fft(noise_samples)
fft_denoised = np.empty((len(fft_noise),), dtype=complex)
denoised_samples = np.empty((0,), dtype=int)
for i in range(len(voice_orig)//clip_len):
    voice = voice_orig[clip_len*i:clip_len*(i+1)]
    voice_samples = voice.get_array_of_samples()
    fft_voice = np.fft.fft(voice_samples)
    for j in range(len(fft_voice)):
        try:
            if fft_noise[j]>=fft_voice[j]:
                fft_denoised[j] = 0
            else:
                fft_denoised[j] = vertical_scale * (fft_voice[j] - fft_noise[j])
        except IndexError:
            print("overflow at", i, j)

    denoised_ifft = np.fft.ifft(fft_denoised)
    denoised_samples = np.append(denoised_samples, denoised_ifft.real)
    #print(len(denoised_samples_clip), end=" ")

voice_denoised = AudioSegment.silent(1, frame_rate=44100)
voice_denoised = voice_denoised._spawn(denoised_samples)
play(voice_denoised)
print("done", len(voice_denoised), "highest at", max(denoised_samples))
