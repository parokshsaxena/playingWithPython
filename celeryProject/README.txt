This project defines three tasks
1) addTask
2) multipleTask
3) printTask

Each task is sent to different queue. celeryconfig.py file has queue & routing information
(source for routing : http://celery.readthedocs.org/en/latest/userguide/routing.html)


To run your worker, go to folder above celeryProject folder and run below command
$ celery -A celeryProject.celeryFile worker --loglevel=info

All the task needs to be registered else calling them will give unregistered error
- in celeryconfig.py, we have registered our tasks using CELERY_IMPORTS

All the path reference (example for tasks), should be given from location where workers are running. For example, to refer to addTask,
you need to use celeryProject.addTasks


Running celery workers as deamon : celeryd
(source : http://celery.readthedocs.org/en/latest/tutorials/daemonizing.html)
You need to use celeryd file which has all configuration
Make sure you change "CELERY_DEFAULTS" to point to your location of configuration file (ie full path of celerydconfig file)

Inside celerydconfig file, you need to change following :
1) CELERYD_CHDIR : to point to location which contains your project directory
2) CELERY_APP : (keeping it to celeryProject will work if you are not changing project name)
3) CELERYD_LOG_FILE : if log file location needs to be changed
4) CELERYD_PID_FILE :
5) CELERYD_GROUP :
6) CELERYD_GROUP :


To run celery as a deamon, celerydconfi file should have root permissions.
$ sudo chown root '/Users/paroksh.saxena/personal/python/playingWithPython/celeryProject/celerydconfig'

Command to run :
sudo sh celeryd start

Running Scheduler : celerybeat
celerybeat & celerybeatconfig has all configurations

in celeryconfig file, you need to define celerybeat scheduler timings.