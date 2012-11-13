import sys, os

sys.path.extend(['lib'])

def pypath():
    """ Setup the environment and python path for django and for dev_appserver.
    """

    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

    # Set up the python path using dev_appserver
    for path in os.environ.get('PATH').split(os.pathsep):
        if 'dev_appserver.py' in os.listdir(path):
            test_path = os.path.join(path, 'dev_appserver.py')
            sdk_path = os.path.dirname(os.readlink(test_path) 
                if os.path.islink(test_path) 
                else test_path)
            sys.path.insert(0, sdk_path)

            from dev_appserver import fix_sys_path
            from google.appengine import tools, dist 

            # Load config from app.yaml
            appinfo, _, _ = tools.dev_appserver.LoadAppConfig(
                os.path.normpath(os.path.abspath('.')), default_partition='dev')

            fix_sys_path()

            # Add Django (and any libraries) defined in app.yaml
            if appinfo.libraries:
                for library in appinfo.libraries:
                    dist.use_library(library.name, library.version)

