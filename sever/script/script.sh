rm -rf /happa/backup/tmp/*
cd /happa/backup/tmp/
zip -r backupfile.zip /www/backup
zip backupfile.zip --out backup.zip -s 45m
python3 /happa/backup/script/py/script.py