import numpy as np

# noise properties for 10s cadence, from ET team
polyc = np.array([ 1.27092953e-05, -1.16348335e-03,  4.11920022e-02, -6.94345836e-01,
        5.80636842e+00, -1.69109034e+01])


def calc_noise(
    imag,
    exptime,
    subexptime=10.0,
):
    
    noise_10s = np.where(imag >= 10.54, 10.0**np.polyval(polyc, imag), 10.0**np.polyval(polyc, 10.54))
    noise_10s /= 1e6  # from ppm to fractional

    n_exposures = exptime / subexptime
    noise = noise_10s / np.sqrt(n_exposures) 

    return noise
