from flask import Flask
import sys
sys.path.insert(0, r'lib\pyaiml')
import aiml
import os.path

brainfile = os.path.join('lib', 'pyaiml', 'brain.brn')
aimlfiles = os.path.join('lib', 'pyaiml', 'aiml', 'aiml-en-us-foundation-alice', '*')

k = aiml.Kernel()
if os.path.isfile(brainfile):
	k.bootstrap(brainFile = brainfile)
else:
	k.bootstrap(learnFiles = aimlfiles)
	k.saveBrain(brainfile)

app = Flask(__name__)
app.k = k
from app import views