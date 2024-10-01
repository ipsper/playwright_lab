# making a lab with playwright

1. [playwright](https://playwright.dev/)
2. [python api playwright](https://pypi.org/project/playwright/)

# setup env

cd repo/playwright_lab
python3 -m venv playwright_lab_venv
source playwright_lab_venv/bin/activate
python3 -m pip install -r requirements.txt

playwright install
sudo apt-get install libgstreamer-plugins-bad1.0-0 libflite1 gstreamer1.0-libav

# run a application cmd

## titels

```
python3 -c 'from app import play_sup; print(play_sup.play_sync_index_title("http://127.0.0.1:4000", ["chromium", "firefox", "webkit"]))'
python3 -c 'from app import play_sup; print(play_sup.play_async_index_title("http://127.0.0.1:4000", ["chromium", "firefox", "webkit"]))'
```

## screenshot

```
python3 -c 'from app import play_sup; print(play_sup.play_sync_screenshot("http://127.0.0.1:4000", ["chromium", "firefox", "webkit"]))'
python3 -c 'from app import play_sup; print(play_sup.play_async_screenshot("http://127.0.0.1:4000", ["chromium", "firefox", "webkit"]))'
```

## run test using pytest

python -m pytest -sx tests/test_ips_sale_support.py

--html=report.html

# use magick

1. [magick](https://imagemagick.org/script/download.php)

2. [install with apt](https://itsfoss.com/install-imagemagick-ubuntu/)

```
sudo apt install imagemagick
magick compare
```

# use magick compare

[magick compare cli](https://imagemagick.org/script/compare.php)
[magick compare methods](https://www.imagemagick.org/Usage/compare/#methods)

```
compare baseline-index-chromium.png latest-index-chromium.png difference.png

compare -compose src baseline-index-chromium.png latest-index-chromium.png difference.png
-rw-rw-r-- 1 per per  3517 okt  1 09:34 difference.png


compare -compose src baseline-index-firefox.png latest-index-firefox.png difference.png
-rw-rw-r-- 1 per per  3517 okt  1 09:38 difference.png

compare -compose src baseline-index-chromium.png latest-index-firefox.png difference.png
-rw-rw-r-- 1 per per  5139 okt  1 09:35 difference.png

```

# use poppy

[poppy](https://github.com/kallaballa/Poppy)

```
    sudo apt install git-core build-essential libsdl-image1.2-dev libsdl1.2-dev libopencv-dev
    git clone https://github.com/kallaballa/Poppy.git
    cd Poppy
    make -j

    make[1]: Leaving directory '/home/per/repo/Poppy/src'
make: *** [Makefile:130: dirs] Error 2


```

# use pixelmatch

[pixelmatch](https://github.com/mapbox/pixelmatch)

```

```

# use odiff

[odiff](https://github.com/dmtrKovalenko/odiff)

```

```

https://github.com/dmtrKovalenko/odiff
