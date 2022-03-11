import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile

def scratch_solution(sound):
    rate, aud = wavfile.read(sound)
    data = aud[:, 0][int(rate*62.5) : int(rate*66.6)]
    fig,ax = plt.subplots(1)
    ax.specgram(data, Fs=rate, noverlap=384, NFFT=512)
    plt.savefig("fig.png")

if __name__ == '__main__':
    scratch_solution("chall/sick_beats.wav")
    print("Preberi rezultat s slike 'fig.png'.")
