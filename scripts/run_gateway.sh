SCRIPTPATH="$(
    cd -- "$(dirname "$0")" >/dev/null 2>&1
    pwd -P
)"
PROJ_DIR="$(dirname "$SCRIPTPATH")"

# navigate to project directory
cd $PROJ_DIR

# activate virtuale environment
source "$PROJ_DIR/gateway/venv/bin/activate"

# check cmd args
FLAG=""
if [ -n "$1"] && ["$1" == "-r" ]; then
    FLAG="--reload"
fi
# start FastAPI server
uvicorn gateway.src.main:app "$FLAG"

deactivate
cd $SCRIPTPATH
