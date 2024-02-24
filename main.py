import numpy as np
import imageio.v3 as iio
import scipy.ndimage
# Resim dosyasının adı
img = 'resim.jpeg'
# Renkli görüntüyü siyah-beyaza dönüştüren fonksiyon
def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5879, 0.1140])
# "Dodge" efektini uygulayan fonksiyon
def dodge(front, back):
    result = np.zeros_like(front)
    mask = back == 255
    result[mask] = 255
    ratio = np.clip(front / (255 - back + 0.1), 0, 1)
    result[~mask] = (ratio[~mask] * 255).astype(np.uint8)
    return result
# Resmi yükleme
ss = iio.imread(img)
# Renkli görüntüyü siyah-beyaza dönüştürme
gray = rgb2gray(ss)
# Tersleme işlemi
i = 255 - gray
# Bulanıklaştırma işlemi
blur = scipy.ndimage.gaussian_filter(i, sigma=50)
# "Dodge" efektini uygulama
r = dodge(blur, gray)
# Sonucu kaydetme
iio.imwrite('rob.png', r.astype('uint8'))