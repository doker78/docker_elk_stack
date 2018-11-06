Here's a little walkthrough of how Yannick and I are using feature branches and pull requests to develop new features and adding them to the project. Below are the steps I take when working on a new feature. Hopefully this, along with watching the process on Github, will serve as a starting point to having everyone use a similar workflow. 

Questions, comments, and suggestions for improvements welcome!

## Start with the latest on master

When starting a new feature, I make sure to start with the latest and greatest codebase:

```
git checkout master
git pull origin master
```

This reduces complications of dealing with out of date code, and reduces the chances of merge issues.

## Create feature branch

Now I develop a local branch to house the changes required for the new feature. 

Here we are using the term 'feature' loosely. Its a logical grouping of code and configuration changes to enable a new portion of the code, fix an issue, or improve existing code. The idea is to use your best judgement and try to keep the scope of the changes limited to a single logical issue.

```
git checkout -b add_linting
```

This will create a new branch called `add_linting` and check it out for me. 

We could argue about branch naming practices, but so far I haven't found naming to be that big of an issue.

```
git status
```

Will show we are on the new branch and ready to work

## Modify code

Now we implement the new feature / bug fix. Work as you would normally, making small incremental changes and checking them into the local feature branch.

Use descriptive comments when adding new changes so that the history of changes is easy to follow. They can still be short and succinct - but clear.

## Push Feature Branch to Remote

Ok, you are done with the implementation. You've checked and double checked the changes, and are ready to have them integrated into the main code base. 

The first step of the review process is to push your feature branch to `origin`.

```
git push origin add_linting
```

This will push your current branch to a new branch on origin with the same name. 

Of course you can do this multiple times during the development process - if you want the peace of mind of having your changes distributed, or you want another set of eyes on it even before the pull request.

## Create Pull Request

With your feature branch on github, navigate to the project on github. On the main page, you should see a new little toolbar that shows your feature branch listed and asks if you want to create a pull request from it. So let's do it!

![screen shot 2015-05-27 at 10 28 45 am](https://cloud.githubusercontent.com/assets/9369/7843160/ae17dcf2-045c-11e5-9f12-db8f4b197137.png)


When creating a pull request, you want to summarize the changes being made for this new feature and give it a descriptive title. 

You can reference existing issues or other PR's by typing # - and then the issue number. A little pop-up should help with picking the right issue number. 

Feel free to add screenshots or other images if there are visual changes associated with your PR. 

Once you have written out the description for the new PR - submit it and sit back for a bit while a teammate reviews. 

Next up, we will look at the PR review process and how it can be done efficiently on github.


## Reviewing PR's Locally

In many cases, a visual check of the changes via the PR page on github is enough to give a +1 to changes. But sometimes, you want to try things out locally to really get a feel for what is going on. 

Here is a few tips for doing just that.

### Dealing with Local Changes

Optimally, you will be at a good stopping point in your own work, so that you are mentally prepared to review someone else's changes. 

Obviously, sometimes this isn't the case. There's a PR that's urgent and needs to get looked at Now! There is a lull in your creative process, and you want to perform some other tasks before trying to tackle your problem again. Someone just asks you to take a look - and you want to get back to them before they go to bed. Plenty of reasons why you might have unfinished business in your local repo.

**Option 1: Use Your Feature Branch**
A suggested option would be to simply check in your current changes into your local _feature branch_ before pulling down someone else's. This is another great benefit to feature branches. They are for your changes only, and are meant to be used for small commits as you work on a particular feature/problem. 

A `git status` will tell you if you might have forgotten to create a feature branch before you started working on a problem. If you did, referring to above, you can just `git checkout -b feature_name` (assuming you are already on `master`), and then just check in your changes there. 

**Option 2: Use git stash**

If you really don't want to check in your changes for some reason, git also provides a handy nook to hide things in with `git stash`. [Git Stash](https://git-scm.com/book/en/v1/Git-Tools-Stashing) is provided - as the headline says - for when _"things are in a messy state and you want to switch branches for a bit to work on something else."_

Using git stash in its basic form is pretty simple:

```
git stash
```

This will _stash_ your local, uncommitted changes making your repo again clean and free of changes, thus allowing you to move on to the PR viewing.

## Pull Down PR

Getting the PR down from github and into your local repository can be done in many ways. As [github's documentation](https://help.github.com/articles/checking-out-pull-requests-locally/) suggests, you can use the GUI github client to pull down remote branches visually. 

Else, you can pull down the PR using something like this:

```
git fetch origin pull/ID/head:BRANCHNAME
```

Where `ID` is the numerical ID assigned to the PR (which you can see in its url or at the top of the PR page), and `BRANCHNAME` is the local branch name you want to give it. 

For example, on the [mvlvm](https://github.com/bocoup/mvlvm) project, there is a PR with an ID of 21.

![screen shot 2015-06-11 at 8 52 18 am](https://cloud.githubusercontent.com/assets/9369/8111526/32a85eea-1017-11e5-87ba-cb0e8a8eaaef.png)

I'll grab this PR using the following command:

```
git fetch origin pull/21/head:bool_vis
```

Which gives me a new _read only_ reference to the PR. 

![screen shot 2015-06-11 at 8 53 29 am](https://cloud.githubusercontent.com/assets/9369/8111559/6fd9c33a-1017-11e5-946e-803565e90db2.png)

Now I switch to this branch in my local repo

```
git checkout bool_vis
```

A quick third alternative is to pull down the remote branch that the PR is based on. You would do that with something like:


```
git checkout -b BRANCHNAME origin/BRANCHNAME
```

So, for the branch for this PR, I would do:

```
git checkout -b module_experiment origin/module_experiment
```

In all cases, the PR get into your local repo for experimentation. 

## Retrieving Local Changes

Once done with the review, it's time to get back to work.

If you used a feature branch approach, and checked in your changes, you can just switch back to your feature branch and go.

If you used stash, you'll want to _pop_ those stashed changes off the stash (which actually works like a stack - allowing you to stash many things). Back in your feature branch, you can run:

```
git stash pop
```

And all stashed changes will be back locally, and uncommitted, just the way you left them.

Now that a Pull Request is live, someone has to review it. Let's walk through some of the steps involved in making this process go quickly. 

## Finding Pull Requests

First we need to get to the PR. From a project's main page, we can see that Pull Requests are a menu option.

![screen_shot_2015-05-27_at_8_57_48_am](https://cloud.githubusercontent.com/assets/9369/7841032/f1f4e220-044e-11e5-9f6e-c6aa19430457.png)

Click that to see a list of all the open PR's. 

For this example, I'm going to focus on my [Generated Docs PR](https://github.com/bocoup/moebio_framework/pull/13) .

## Reviewing a PR

As a reviewer, its my job to check out the PR for any major issues, as well as comment on smaller issues I find in the code. I think a goal here is to be through but balance your time and the developer's time. 

On a PR's main page, I can see the PR's description and any existing comments about the code. 

![screen shot 2015-05-27 at 9 04 40 am](https://cloud.githubusercontent.com/assets/9369/7841198/cc9ee812-044f-11e5-9839-fef02ceacedf.png)

Start here to understand the scope of the request.

Then, skip to the __File Changes__ tab to start reviewing. 

(So far, I haven't found the _Commits_ tab all that useful for reviewing the code - it gets too fragmented when there are multiple changes).

![screen_shot_2015-05-27_at_9_08_45_am](https://cloud.githubusercontent.com/assets/9369/7841268/54ac9b8c-0450-11e5-8eaf-810288805d0c.png)

## Commenting on Issues

So the PR isn't perfect. No biggie - that is expected. The review process makes it easy for a reviewer to spot issues and for the coder to implement changes. 

As a reviewer, you can add comments inline to the change preview on github. Simply click on the little + next to the line or lines you have issue with.

![screen shot 2015-05-27 at 8 04 44 am](https://cloud.githubusercontent.com/assets/9369/7841281/753f01b4-0450-11e5-9222-0f7767119ff4.png)


As the PR requester, you can comment on those comments to justify or suggest future actions. 

Here is an example where Yannick catches a spot where I left in some old code.

![screen shot 2015-05-27 at 8 43 58 am](https://cloud.githubusercontent.com/assets/9369/7841287/7c867eca-0450-11e5-9eff-cce402e0fa9e.png)

I follow up, indicating that it will be dealt with on this branch

![screen shot 2015-05-27 at 8 44 14 am](https://cloud.githubusercontent.com/assets/9369/7841294/820817e6-0450-11e5-9b31-fce0d11b1f89.png)

## Dealing with Issues

Now that there is a problem with the PR, we need to fix it. The PR process makes this pretty easy too. 

Locally, on my feature branch, I simply implement the changes to fix the problem and commit the changes. 

Then I push those changes up to the remote branch again. In this case, the branch was called `docs`. So:

```
git push origin docs
```

The PR is automatically updated with the latest changes. As Yannicks comments are on code affected by this new commit, they are hidden by default.

![screen shot 2015-05-27 at 8 51 39 am](https://cloud.githubusercontent.com/assets/9369/7841308/998310c4-0450-11e5-9e03-9cae537e5bde.png)

## Merging PR

After a few messages, we should arrive at a desired `+1` - which means its time to get this merged.

![screen shot 2015-05-27 at 9 17 03 am](https://cloud.githubusercontent.com/assets/9369/7841457/9d74226c-0451-11e5-9b18-cdf72aaf7464.png)

Additional suggestions can be dealt with in a separate PR - or added as another commit to the existing one - if you feel the scope is small enough. I typically like smaller PRs to bigger ones, so if I can justify splitting out additional suggestions into separate issues, I go that route. 

If you are lucky, the PR can be automerged - and you can do it right inside github!

But sometimes (and not often honestly), the magic doesn't quite work, and you need to return to the command line one final time for the merge.

![screen shot 2015-05-27 at 9 21 48 am](https://cloud.githubusercontent.com/assets/9369/7841505/fb5e21b6-0451-11e5-89e1-eef542cd0a21.png)

Luckily, the instructions for getting started are right there, just a click away.

![screen shot 2015-05-27 at 9 23 53 am](https://cloud.githubusercontent.com/assets/9369/7841544/3bb7698e-0452-11e5-932b-177e55b0e880.png)

First make sure you have the latest master in your local repo.

```
git checkout master
git pull origin master
```

Then switch back to the feature branch and merge in master

```
git checkout docs
git merge master
```

This should fail, and it should tell you which files you need to look at to resolve the conflict.

![screen shot 2015-05-27 at 9 29 30 am](https://cloud.githubusercontent.com/assets/9369/7841647/eb838d34-0452-11e5-9d32-5c4e1588b8dc.png)

Here, I just have one file that needs attention `gruntfile.js`

Opening it up in my text editor, i look for the <<<< indicating a merge conflict.

![screen shot 2015-05-27 at 9 28 46 am](https://cloud.githubusercontent.com/assets/9369/7841661/180d0574-0453-11e5-85c8-2c766d17b2b7.png)

I modify the code until all the conflicts are dealt with. Then add the file to staging.

```
git add gruntfile.js
```

The rest of the merge is already in staging - so now I can commit the merge 

```
git commit -m 'merged master'
```

And switch back to master to push up this change

```
git checkout master
git merge --no-ff docs
git push origin master
```

A lot more work then the auto-merge -but hopefully its unusual that auto-merge isn't an option

## Delete remote branch

Either way, once the PR is merged into master, we can remove the remote branch - which keeps our github project cleaned up. 

![screen shot 2015-05-27 at 9 45 03 am](https://cloud.githubusercontent.com/assets/9369/7841987/339751e4-0455-11e5-8e5f-d2f0f3c4f3f9.png)
