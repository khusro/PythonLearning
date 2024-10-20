# Environments:
#   1. Local Environment (your own setup + your own data to test)
#   2. Development Environment (your team's setup + data created on the basis of requirements provided)
#   3. Test Environment (Optional sometimes) (scaled down setup of Prod + some data from prod but masked)
#   4. Staging Environment (Optional) (replica of production + prod data)
#   5. Production Environment

# Github:
#   main (branch) ==> Production Environment
#   develop (branch) ==> Most recent merged code (If no active development is going on then main === develop)
#       1. New Branch (xyz-branch) from <develop branch>
#       2. download the branch locally
#       3. Code the new feature and test locally
#       4. Commit and Push your code to your remote branch
#       5. Creat a Pull Request in order for your changes to be merged back into develop branch