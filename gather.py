import sys
import os
import json
import yaml
import re
from subprocess import Popen, PIPE, STDOUT


def gather():
    print("Version of python:")
    v1 = str(sys.version_info[0])
    v2 = str(sys.version_info[1])
    v3 = str(sys.version_info[2])
    print(v1 + "." + v2 + "." + v3)
    print("\n")
    print("virtualenvs:")
    os.system("pyenv virtualenvs")
    print("\n")
    print("Python execution location:")
    print(sys.executable)
    print("\n")
    print("installed packages:")
    os.system("pip list")
    print("\n")
    print("PYTHONPATH: ")
    print(str((os.environ['PATH'].split(os.pathsep))[0]))
    print("\n")
    print("Pip location:")
    os.system("which pip")
    print("\n")
    i = 0
    while i < len(sys.path):
        if 'site-packages' in sys.path[i]:
            print("Path to site-packages location")
            print(sys.path[i])
        i += 1


def general_function():
    d = {}
    d["Python execution location"] = str(sys.executable)
    i = 0
    path_site = ""
    while i < len(sys.path):
        if 'site-packages' in sys.path[i]:
            path_site = str(sys.path[i])
        i += 1
    d["Path to site-packages location"] = path_site

    p = Popen(
       'pyenv virtualenvs',
       shell=True, stdin=PIPE,
       stdout=PIPE, stderr=STDOUT, close_fds=True
    )
    output = p.stdout.read().decode('utf-8')
    strings = re.findall(r'(?<=\s\s).+', output)
    d["virtualenv"] = strings[0]

    p = Popen(
        'which pip', shell=True,
        stdin=PIPE, stdout=PIPE,
        stderr=STDOUT, close_fds=True
    )
    output = p.stdout.read().decode('utf-8')
    pip_string = re.findall(r'[^\s]', output)
    pip_location = ''.join(pip_string)
    d["Pip location"] = pip_location

    d["PYTHONPATH"] = str((os.environ['PATH'].split(os.pathsep))[0])

    vs1 = str(sys.version_info[0])
    vs2 = str(sys.version_info[1])
    vs3 = str(sys.version_info[2])
    d["version"] = vs1 + "." + vs2 + "." + vs3
    p = Popen(
      'pip list', shell=True,
      stdin=PIPE, stdout=PIPE,
      stderr=STDOUT, close_fds=True
    )
    output = p.stdout.read().decode('utf-8')

    strings = re.findall(r'(?<=\s).+', output)
    u = 1
    d2 = {}
    while u < len(strings):
        d2[u] = strings[u]
        u += 1
    d["Packeges"] = d2
    return d


def json_file():
    d = general_function()
    with open('json_pyenv.json', 'w') as outfile:
        json.dump(d, outfile, sort_keys=True, indent=4, ensure_ascii=False)
        outfile.write("\n")


def yaml_file():
    d = general_function()
    with open('yaml_pyenv.yaml', 'w') as outfile:
        yaml.dump(d, outfile, default_flow_style=False, allow_unicode=True)
        outfile.write("\n")


if __name__ == "__main__":
    gather()
    json_file()
    yaml_file()
