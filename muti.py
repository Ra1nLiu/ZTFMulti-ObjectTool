from astropy.io import fits
from astropy.io import ascii
import os

# read the fits data. The data in fits file is sorted by 'oid'
hdu = fits.open('lc.fits')
oid = hdu[1].data.field('oid')
mjd = hdu[1].data.field('mjd')
mag = hdu[1].data.field('mag')
magerr = hdu[1].data.field('magerr')
flag = hdu[1].data.field('catflags')
filters = hdu[1].data.field('filtercode')
ra = hdu[1].data.field('ra')
dec = hdu[1].data.field('dec')

# read the list
f = ascii.read('list.tbl')
f.sort(['oid'])
name = f['name_01']
oid1 = f['oid']
filtercode1 = f['filtercode']
# nobsrel is matched to the number of each light curve.
nobsrel = f['nobsrel']

j = 0
workspace = os.getcwd() # you can change your workspace directory here.
for i in range(len(name)):
    # make folders
    if not os.path.exists(name[i]):
        os.mkdir(name[i])
    # change the workspace
    os.chdir(name[i])
    # create the light curves
    dataname = name[i] + '_' + filtercode1[i] + '.txt'
    f1 = open(dataname, 'a+')
    num = j
    while j < num + nobsrel[i] and j < len(oid):
        if flag[j] == 0:
            data = str(mjd[j]) + '\t' + str(mag[j]) + '\t' + str(
                magerr[j]) + '\n'  # you can change the data type here
            f1.write(data)
        j = j + 1
    f1.close()

    os.chdir(workspace)