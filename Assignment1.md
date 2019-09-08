1.Draw a diagram of the commits and branches in repository.

(base) LimingdeMacBook-Pro:handson limingzheng$ git branch
* master
  math
(base) LimingdeMacBook-Pro:handson limingzheng$ git checkout master
Already on 'master'
(base) LimingdeMacBook-Pro:handson limingzheng$ git checkout math
Switched to branch 'math'
(base) LimingdeMacBook-Pro:handson limingzheng$ git log --decorate
commit e3c629dd524712aedea96d7dbaad1c50d12b5b5e (HEAD -> math)
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:13:48 2019 -0700

    Adding some more knowledge to the function

commit 654b490a181dedf82dd6deda5f9848d6cca05918
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:12:14 2019 -0700

    Added a draft of A.py

commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:08:47 2019 -0700

     Creating all files (all empty)
     

2.Try git log --graph --all to see the commit tree. What do you see?

(base) LimingdeMacBook-Pro:handson limingzheng$ git log --graph --all 
* commit 18931d12a8be7cac049b73c6bc8136e9482f3371 (master)
| Author: Igor Steinmacher <igorsteinmacher@gmail.com>
| Date:   Wed Aug 14 23:15:28 2019 -0700
| 
|     Making a small change here
|   
| * commit e3c629dd524712aedea96d7dbaad1c50d12b5b5e (HEAD -> math)
|/  Author: Igor Steinmacher <igorsteinmacher@gmail.com>
|   Date:   Wed Aug 14 23:13:48 2019 -0700
|   
|       Adding some more knowledge to the function
| 
* commit 654b490a181dedf82dd6deda5f9848d6cca05918
| Author: Igor Steinmacher <igorsteinmacher@gmail.com>
| Date:   Wed Aug 14 23:12:14 2019 -0700
| 
|     Added a draft of A.py
| 
* commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
  Author: Igor Steinmacher <igorsteinmacher@gmail.com>
  Date:   Wed Aug 14 23:08:47 2019 -0700
  
       Creating all files (all empty)
:

3.Use git diff BRANCH_NAME to view the differences from a branch and the current branch. Summarize the difference from master to the other branch.

In the master branch and math branch, there are both two files. But in the master branch, there is only one line code. 
When we use git diff to view the other branch, it will show the different line code from the master branch, such as the calculate operator code. 

4.Write a command sequence to merge the non-master branch into master

git merge math

5.Write a command (or sequence) to (i) create a new branch called math (from the master) and (ii) change to this branch

git checkout -b math

git checkout math

6.Edit B.py adding the following source code below the content you have there

print 'I know math, look:'
print 2+2

7.Write a command (or sequence) to commit your changes

git add .

git commit

8.Change back to the master branch and change B.py adding the following source code (commit your change to master):

print 'hello world!'

9.Write a command sequence to merge the math branch into master and describe what happened

git merge math
Auto-merging B.py
CONFLICT (content): Merge conflict in B.py
Automatic merge failed; fix conflicts and then commit the result.

10.Write a set of commands to abort the merge

git merge --abort

11.Now repeat item 9, but proceed with the manual merge (Editing B.py). All implemented methods are needed. Explain your procedure

I use git mergetool to get in kdiff3 interface to change the code location to avoid conflict.

12.Write a command (or set of commands) to proceed with the merge and make master branch up-to-date

git mergetool

