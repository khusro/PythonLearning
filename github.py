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
#       6. After approval from team members/Lead your code is promoted to develop branch
#       7. Automatically the new develop branch code shall be deployed to Development environment
#       8. The developer(s) will test the application for integrity and correctness
#       9. If everyone is satisfied the code is promoted to Test Environemt
#       10. Testers will test the application in the test environment (Integration Testing/ End to End Testing)
#       11. If bugs/defects are created then developer shall create a new branch under "bugfix" prefix (1-10 would repeat)
#       12. A release (branch) is created and deployed to staging
#       13. Fine tuning and performance testing happens
#       14. If any issue is found (1-13 would repeat)
#       15. Release (branch) is promoted to production then merged to main (branch)