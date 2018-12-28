git checkout --orphan new-master
git add .
git commit -m "Clean commits"
git branch -m master old-master
git branch -m new-master master
git push --force --set-upstream origin master
git branch -D old-master
git pushgit checkout --orphan new-master
git add .
git commit -m "Clean commits"
git branch -m master old-master
git branch -m new-master master
git push --force --set-upstream origin master
git branch -D old-master
git push
