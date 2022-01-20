# Project 0 - Git Guide

## Command line git

- status
  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub)
    - list of files in local folder than are NOT being tracked by git
    - list of files in local folder that have changes that need to be committed
  - `git status`
- clone
  - Copies repository folder from remote server (such as GitHub) onto the local machine so that it can be modified on that local machine.
  - When using GitHub and SSH authentication, the clone command is usually formatted like this: `git clone git@github.com:account-name/repository-name.git`.
- add
  - Adds a file or directory for tracking by git
  - `git add file-or-directory-name`
- rm
  - Can be used to remove a file from tracking by git
  - If `git rm filename` is run, that will remove the file from tracking, and it will delete the file off of the disk.
  - To just remove the file from tracking but keep it on the disk, the command `git rm --cached filename` should be used.
  - Any previous version history on the remote repository of the file will still be visible when this is used, so git will only stop tracking a file going forward.
- commit
  - Creates a "stopping point," wraps up and puts a "post-it note"/message on the changes made since the last commit.
  - When writing code, this is good for keeping track of what changes were made over time throughout the time spent making the program.
  - Also, if something goes wrong with the code, and it was not working properly anymore, version control can be used to restore the file(s) to the last committed version and bring it/them back to when the code was last working properly.
  - `git commit -m "Enter commit message here"`
  - Can also type `git commit`, which will open a text editor in which to type a commit message.
- push
  - Syncs remote repository with changes made in local repository
  - `git push`
- fetch
  - Downloads contents of a remote repository onto a local system. This helps show the changes other users have made to a repository.
  - This can be used to download and view the contents of a remote repository, but it does not update the local repository, so all the work on that is left alone.
  - `git fetch repository-name`
- merge
  - Merges a new branch into main branch. The branch to be merged into should be the one that is actively being worked in, so `git checkout receiving-branch-name` should be run before merging.
  - Then, run `git merge branch-to-be-combined-with-receiving-branch`
- pull
  - Syncs remote repo with local
  - Updates files on local repo, unlike `git fetch`, which just downloads the files but does not update anything.
- branch
  - Creates a new branch
  - `git branch new-branch-name`
- checkout
  - Changes working branch
  - `git checkout new-branch-to-move-to`
- ~~init~~
  - Initializes an empty git repo, reinitializes old one, or turns a folder into a repo.
  - `git init name_of_repository`
  - Running `git init --bare repository_name.git` creates a bare repository with just a .git folder inside.
- ~~remote~~

## git files & folders

- .git folder
  - Contains the inner workings of the git program that make version control possible.
  - Also, this can be used to make scripts to limit what contents can be pushed and committed to repo.
  - An example of this would be a test to see what kind of contents are in the commit before allowing it to go through when a worker at a company wants to commit to the repo.
- .gitignore file
  - Contains a list of files usually typed in by the user that git can ignore for version control tracking.
  - This makes it so git does not display warning messages when running commands such as `git status` and `git commit`.
- ~~.git/hooks~~

## GitHub

- Pull requests
  - A pull request just syncs the local repository with the remote repository's changes.
- SSH authentication to repositories
  - This is a new form of authentication that replaced HTTPS authentication that required a username and password.
  - SSH uses public and private keys to authenticate without a password.
  - When first cloning a repo, a key pair must be made using ssh-keygen.
  - The public key needs to then be uploaded to GitHub/remote repo.
  - After this, changes can be pushed without a password having to be typed in each time.
  - Also, this is more secure than HTTPS.
- ~~Actions~~

## Resources

- [Git fetch webpage](https://www.atlassian.com/git/tutorials/syncing/git-fetch#:~:text=The%20git%20fetch%20command%20downloads,else%20has%20been%20working%20on.&text=This%20makes%20fetching%20a%20safe,them%20with%20your%20local%20repository.)
- [Git merge webpage](https://www.atlassian.com/git/tutorials/using-branches/git-merge)
- In-class lectures 