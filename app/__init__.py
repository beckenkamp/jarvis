from flask import Flask
import sys
sys.path.insert(0, 'lib/pyaiml')
import aiml
import os.path

brainfile = os.path.join('lib', 'pyaiml', 'brain.brn')
aimlfiles = os.path.join('lib', 'pyaiml', 'aiml', 'std-startup.aiml')

k = aiml.Kernel()
if os.path.isfile(brainfile):
	k.bootstrap(brainFile = brainfile)
else:
	k.bootstrap(learnFiles = aimlfiles, commands = 'load aiml b')
	k.saveBrain(brainfile)

app = Flask(__name__)
app.k = k
from app import views