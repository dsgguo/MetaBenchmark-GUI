import numpy as np
from scipy.signal import sosfiltfilt
from metabci.brainda.datasets import Wang2016, BETA
from metabci.brainda.paradigms import SSVEP
from metabci.brainda.algorithms.feature_analysis import (
    FrequencyAnalysis,
    TimeAnalysis,
    TimeFrequencyAnalysis,
)
import matplotlib.pyplot as plt
dataset = Wang2016()
delay = 0.14  # seconds
channels = ["PZ", "PO5", "PO3", "POZ", "PO4", "PO6", "O1", "OZ", "O2"]
srate = 250  # Hz
duration = 5  # seconds

events = sorted(list(dataset.events.keys()))
freqs = [dataset.get_freq(event) for event in events]
phases = [dataset.get_phase(event) for event in events]

paradigm = SSVEP(
    srate=srate,
    channels=channels,
    intervals=[
        (delay, delay + duration)
    ],  # more seconds for TDCA
    events=events,
)

X, y, meta = paradigm.get_data(
    dataset, subjects=[1], return_concat=True, n_jobs=1, verbose=False
)

