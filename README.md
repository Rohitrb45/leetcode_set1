Solutions for some of the leetocde problems
Steps to push the changes:
1. Create remote repositry on github
2. cd to_your_local_folder
3. git init
4. git remote add origin your_repository_url.git
5. git add .
6. git commit -m "Initial commit"
7. Generate Personal acces token on github
8. git remote set-url origin https://your_username:your_token@github.com/your_username/your_repository.git
9. git push -u origin master

If there are any conflicts:
git fetch origin
git merge origin/master
git add .
git merge --continue
git push origin master

To push the second directory in the same folder:
1. Repeat steps 5-8
2. git fetch origin
3. git merge origin/master  # or the branch you're working on
4. git push origin master  # or the branch you're working on



