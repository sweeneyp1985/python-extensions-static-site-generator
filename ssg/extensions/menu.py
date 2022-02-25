from ssg import hooks
from ssg import parsers

files = {}

def collect_files(source,site_parsers):
hooks.register("collect_files")
valid = lambda(p)
