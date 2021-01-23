cd /Users/smonsalve/Code/FlaskCourse/microcourse/
conda deactivate
source mc_env/bin/activate
export FLASK_ENV=development
export FLASK_APP=microcourse
code .
osascript \
-e 'tell application "Terminal" to activate' \
-e 'tell application "System Events" to tell process "Terminal" to keystroke "t" using command down'
#-e ''
echo "Hola"
# cd /Users/smonsalve/Code/FlaskCourse/microcourse/
# conda deactivate
# source mc_env/bin/activate
# export FLASK_ENV=development
# export FLASK_APP=microcourse
# flask run
