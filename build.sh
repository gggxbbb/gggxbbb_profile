mkdir dist
cp -r css dist
cp -r static dist
pip3 install -r requirements.txt
python3 build.py