from invoke import run


def get_current_version():
    return run('python setup.py --version', hide=True).stdout.strip()


def evaluate_version_bump(force):
    pass


def get_new_version(current_version, level_bump):
    return current_version


def set_new_version(current_version):
    return True
