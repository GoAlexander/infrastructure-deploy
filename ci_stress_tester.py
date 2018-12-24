# ci_stress_tester.py --repo-path my/path --commits-number 20
# Scripts generate inputted number of commits of goven git-repository.
# It creates folder `_tmp` and files `1.txt`, `2.txt` and so on.

# Choose the branch carefully it will create commits!

import argparse
import pathlib
import subprocess


def create_commits(repo_path, number):
    tmp_folder = repo_path / "_tmp"
    tmp_folder.mkdir(parents=True) #TODO: add deleting of folder?

    text = "Stress-test commit."

    for i in range(number):
        print("Create commit number {}".format(i))
        file_path = tmp_folder / "{}.txt".format(i)
        with file_path.open("w", encoding ="utf-8") as f:
            f.write(text)
        commit_message = "Stress-commit number {}".format(i)
        #TODO: use subprocess "adapter"
        subprocess.run('git add --all', cwd=str(repo_path), shell=True, 
                                                            check=True,
                                                            stdout=subprocess.PIPE,
                                                            stderr=subprocess.STDOUT)
        subprocess.run('git commit -m "{}"'.format(commit_message), cwd=str(repo_path), shell=True, 
                                                                     check=True,
                                                                     stdout=subprocess.PIPE,
                                                                     stderr=subprocess.STDOUT)

def main():
    parser = argparse.ArgumentParser(prog="ci_stress_tester.py",
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--version", action="version", version="%(prog)s 1.0")
    parser.add_argument('-p', "--repo-path", metavar="PATH", required=True,
                        help="Path to the git repository for stress testing")
    parser.add_argument('-n', "--commits-number", metavar="int", required=True,
                        help="Number of commit which needs to create")

    parsed_args, unknown_args = parser.parse_known_args()

    print("Will be created {} commits".format(parsed_args.commits_number))
    print("For repo: {}".format(parsed_args.repo_path))

    create_commits(pathlib.Path(parsed_args.repo_path), int(parsed_args.commits_number))



if __name__ == '__main__':
    main()
