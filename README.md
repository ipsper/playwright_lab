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

python3 -c 'from app import play_sup; print(play_sup.play_sync_title("http://127.0.0.1:4000"))'
python3 -c 'from app import play_sup; print(play_sup.async_title("http://127.0.0.1:4000"))'
