DIR="$( cd "$( dirname "$0" )" && pwd )"
alias python=python3
python "$DIR/rfid_fsr.py" &
python "$DIR/g6trayreturn.py" &
python "$DIR/g6overviewrate.py" & 
python "$DIR/g6barchart.py" &
python "$DIR/application.py"
