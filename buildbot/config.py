import sys

import project_secrets

BUILD = "build"
BUILD_MASTER = "build-master-branch"
TEST = "test"

WORKERS = {
    BUILD: {"example-worker": {},
            "b-2": {}},
    TEST: {"t-1": {},
           "t-2": {}}
}

PORT = "8010"
WORKER_PORT = "9000"
BUILDBOT_NET_USAGE_DATA = None # "None" disables the sending of usage analysis info to buildbot.net
BUILDBOT_TREE_STABLE_TIMER = None # Value "None" means that a separate build will be started immediately for each Change.
BUILDBOT_TITLE = "Hello, World!"
POLL_INTERVAL = 10 # Poll Github for new changes (in seconds)

WORKER_PASS = project_secrets.WORKER_PASS #default "pass"
GITHUB_TOKEN = project_secrets.GITHUB_TOKEN
GITHUB_OWNER = "GoAlexander"
GITHUB_OWNERS_REPO = "infrastructure-test"
BUILDBOT_URL = "http://goalexander.asuscomm.com/"

GITHUB_REPOSITORY = f"{GITHUB_OWNER}/{GITHUB_OWNERS_REPO}"
REPO_URL = f"https://github.com/{GITHUB_REPOSITORY}"
REPO_INFO = f"{GITHUB_OWNERS_REPO}:%(prop:branch)s:%(prop:revision)s"
