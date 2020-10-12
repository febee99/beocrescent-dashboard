DIR="$( cd "$( dirname "$0" )" && pwd )"
alias python=python3
python "$DIR/app.py" &
python "$DIR/rfid_fsr.py" &
python "$DIR/g6trayreturn.py"
