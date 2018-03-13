import requests
import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
      "--pswd",
      help="that optional takes your github account",
      required=True
)
parser.add_argument(
            "--login",
            help="that optional takes your github login",
            required=True
)
argument = "that optional argument has:"
argument += "\n \"rep_name\" and \"id_rep\" and \"public_repos\""
parser.add_argument(
            "--repos",
            nargs="?",
            help=argument
)

argument = "that optional argument has:"
argument += "\n \"pull_title\" and \"pull_id\" and \"pull_updated\""
argument += " and \"state\" and \"locked\" and \"number\""
argument += "and \"merge_commit_sha\""
parser.add_argument(
                "--pulls", nargs="?",
                help=argument
)
args = parser.parse_args()

PASSWORD = args.pswd
LOGIN = args.login

repo_info = requests.get(
               'https://api.github.com/user',
               auth=(LOGIN, PASSWORD)
)

Pulls_info = requests.get(
           'https://api.github.com/repos/alenaPy/devops_lab/pulls',
           auth=(LOGIN, PASSWORD)
)

json_dict = repo_info.json()

json_pulls = Pulls_info.json()

# print(json_dict.items())
max_count = len(json_pulls)


def cool_function(parameter):
    print("%-30s%-5s" % ("Owner:", "Your parameter:"))
    i = 0
    while i < max_count:
        # global max_count
        vj = json_pulls[i]["user"].get("login")
        jd = json.dumps(vj, sort_keys=True, indent=4, ensure_ascii=False)
        info1 = str(jd)
        vj2 = json_pulls[i][parameter]
        jd2 = json.dumps(vj2, sort_keys=True, indent=4, ensure_ascii=False)
        info2 = str(jd2)
        print("%-30s%-5s" % (info1, info2))
        i += 1


if args.repos == "rep_name":
    print("Rep_name = " + str(json_dict.get("login")))

if args.repos == "rep_id":
    print("ID = " + str(json_dict.get("id")))

if args.repos == "public_repos":
    print("Public_Repo = " + str(json_dict.get("public_repos")))
# public_repos

if args.pulls == "pull_title":
    cool_function("title")

if args.pulls == "pull_id":
    cool_function("id")

if args.pulls == "pull_updated":
    cool_function("update_at")

if args.pulls == "state":
    cool_function("state")

if args.pulls == "locked":
    cool_function("locked")

if args.pulls == "number":
    cool_function("number")

if args.pulls == "merge_commit_sha":
    cool_function("merge_commit_sha")
