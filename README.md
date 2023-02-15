# Github Gist Monitor

This script uses the Github API to query a user’s publicly available gists and list any new gists since the last run. On the first run, it will display a listing of all the user’s publicly available gists. On subsequent runs, it will list any gists that have been published since the last run. 

## Prequisites
To use the Github API to query a user's publicly available gists and list any new gists since the last run, we can use **Python** and the **requests library** to send HTTP requests to the Github API.

## Usage
1. Clone this repository to your local machine.
2. Replace **<GITHUB_USERNAME>** and **<GITHUB_TOKEN>** in the `github_gist_monitor.py` file with your Github username and personal access token, respectively. You can generate a personal access token by following the instructions [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).
3. Make sure that the `last_run_timestamp.txt` file is in the same directory as the `github_gist_monitor.py` script. This file stores the timestamp of the last run and is used to determine which gists are new.
4. Open a terminal and navigate to the directory where you cloned this repository.
5. Run the script by entering `python github_gist_monitor.py` in the terminal.
6. On the first run, the script will display a listing of all your publicly available gists. On subsequent runs, the script will display any new gists that have been published since the last run.
## Additional Functionality
You can add additional functionality to the script by using command line flags to specify different Github users or authentication tokens. For example:

- To monitor the gists of a different Github user, use the `--user` flag followed by the username. For example: `python github_gist_monitor.py --user octocat`.
- To use a different Github personal access token, use the `--token` flag followed by the token. For example: `python github_gist_monitor.py --token 0123456789abcdef0123456789abcdef01234567`.
- To display a list of all the user's gists regardless of whether they are new or not, use the `--all` flag. For example: `python github_gist_monitor.py --all`.