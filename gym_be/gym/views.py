from django.shortcuts import render


def index(request):
	import subprocess
	_ss = subprocess.check_output(['uptime', '-p']).decode('utf-8').split('\n')[0]
	_ss = ' '.join(_ss.split(' ')[1:])
	return render(request, 'home.html', {'info': _ss})
