# -MPdSH

'''_____Standard imports_____'''
import numpy as np
import cupy as cp
from scipy.interpolate import interp1d
import cupyx.scipy.fftpack as fftpack
import cupyx.scipy.ndimage


'''_____Project imports_____'''
from src.toolbox._arguments import Arguments
from src.toolbox.gpu.algorithm import detrend_2D, compensate_dispersion_2D, linearize_spectra_2D, spectrum_shift_2D

###############______2D_______##################################################


def process_2D(Volume_spectra: cp.ndarray, coordinates: cp.ndarray, dispersion: cp.array) -> np.array:
    """
    This function process 2D array of spectrum to return adjusted Bscan.

    :param Volume_spectra: 2nd order tensor containing spectras raw data. Last dimension is depth encoding.
    :type Volume_spectra: cp.ndarray
    :param coordinates: 2D array containing coordinates for k-linearization interpolation.
    :type coordinates: cp.ndarray
    :param dispersion: Array with value for dispersion compensation.
    :type dispersion: cp.array
    """

    dtype = Volume_spectra.dtype

    Volume_spectra = detrend_2D(Volume_spectra)

    Volume_spectra = compensate_dispersion_2D(Volume_spectra, dispersion)

    Volume_spectra = linearize_spectra_2D(Volume_spectra, coordinates)

    if Arguments.shift:

        temp = spectrum_shift(Volume_spectra)

    Volume_spectra  = fftpack.rfft(Volume_spectra.astype(dtype),
                                   axis=1,
                                   overwrite_x=True)[:,:Arguments.dimension[2]//2]

    Volume_spectra = cp.absolute(Volume_spectra)

    return cp.asnumpy( Volume_spectra[:,:Arguments.dimension[2]//2] )






# ---
