#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Program to take the audio files in /source_sounds and create files at correct volume levels in the documents folder
# taken from https://stackoverflow.com/questions/51468895/changing-a-wav-files-volume-using-python with minor modification
import wave
from os import path


def convert_wav(factor, inpath, outpath):
	soundmap = {'divination': 'scroll.wav',
				'unique': 'amulet.wav',
				'map_good': 'flippy.wav',
				'map_okay': 'charm.wav',
				'challenge1': 'gethit1.wav',
				'challenge2': 'gethit2.wav',
				'challenge3': 'gethit3.wav',
				'challenge4': 'gethit4.wav',
				'challenge5': 'attack1.wav',
				'challenge6': 'attack2.wav',
				'challenge7': 'attack3.wav',
				'challenge8': 'attack4.wav',
				'challenge9': 'attack5.wav',
				'challenge10': 'attack6.wav',
				'challenge11': 'death1.wav',
				'challenge12': 'death2.wav',
				'challenge13': 'death3.wav',
				'challenge14': 'death4.wav',
				'challenge15': 'death5.wav',
				'currency': 'gold.wav',
				'show': 'convert.wav',
				'valuable': 'portalcast.wav',
				'gem': 'gem.wav',
				'base': 'charge.wav',
				'mirror': 'neutral3.wav'}

	pathout = "{}_{}.wav".format(int(factor), inpath)
	factor = factor / 100

	with wave.open('source_sounds/{}'.format(soundmap[inpath]), 'rb') as fin, wave.open('filter_sounds/{}'.format(pathout), 'wb') as fout, wave.open(path.join(outpath, pathout), "wb") as f:
		fout.setparams(fin.getparams())
		f.setparams(fin.getparams())
		sampwidth = fin.getsampwidth()

		while True:
			frames = bytearray(fin.readframes(1024))
			if not frames:
				break

			for i in range(0, len(frames), sampwidth):
				if sampwidth == 1:
					# 8-bit unsigned
					frames[i] = int(round((sample[0] - 128) * factor + 128))
				else:
					# 16-, 24-, or 32-bit signed
					sample = int.from_bytes(frames[i:i + sampwidth], 'little', signed=True)
					quiet = round(sample * factor)
					try:
						frames[i:i + sampwidth] = int(quiet).to_bytes(sampwidth, 'little', signed=True)
					except OverflowError:
						if quiet < 0:
							frames[i:i + sampwidth] = int(-32768).to_bytes(sampwidth, 'little', signed=True)
						else:
							frames[i:i + sampwidth] = int(32767).to_bytes(sampwidth, 'little', signed=True)
			fout.writeframes(frames)
			f.writeframes(frames)


if __name__ == '__main__':
	sounds = ['divination', 'unique', 'map_okay', 'challenge', 'map_good', 'currency', 'show', 'valuable']

	for track in sounds:
		for i in [20, 45, 75, 100, 300]:
			convert_wav(i, track)
