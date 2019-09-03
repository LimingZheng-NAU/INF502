1.Draw a diagram of the commits and branches in repository.

--Use git branch to list the branches in this repository.

--Use git checkout to explore each branch.

--Use git log --decorate to explore the structure of commits.

commit 18931d12a8be7cac049b73c6bc8136e9482f3371 (HEAD -> master)
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:15:28 2019 -0700

    Making a small change here

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
* commit 18931d12a8be7cac049b73c6bc8136e9482f3371 (HEAD -> master)
| Author: Igor Steinmacher <igorsteinmacher@gmail.com>
| Date:   Wed Aug 14 23:15:28 2019 -0700
| 
|     Making a small change here
|   
| * commit e3c629dd524712aedea96d7dbaad1c50d12b5b5e (math)
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
