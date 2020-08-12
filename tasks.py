
from invoke import task

@task(default=True)
def build(c, version='1.0.0'):
    """ Build source code distribution
    """
    c.run("python3 ./setup.py sdist", pty=True, echo=True)


@task
def publish(c, version='1.0.0'):
    """ Publish package version
    """
    c.run("twine upload pybringcloud-0.0.0.tar.gz", pty=True, echo=True)
