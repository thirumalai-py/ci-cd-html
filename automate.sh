#!/bin/bash

folder_path="/var/www/ci-cd-html"
commit_file="latest_commit.txt"
# cat $commit_file

# echo "Checking for the latest commit in the repository: $git_path"
# last_commit=$(git log -1 --pretty=format:"%H")
# saved_commit=$(cat $commit_file | head -n 1)
# echo $last_commit
# echo $saved_commit

# if [[ "$last_commit" == "$saved_commit" ]]; then
#     echo "No new commit found"
# else
#     echo "New commit found"
#     git pull
#     new_commit_id=$(git log -1 --pretty=format:"%H")
#     cat $commit_file | head -n 1 > $new_commit_id
# fi

last_commit=$(git log -1 --pretty=format:"%H")
saved_commit=$(cat "$commit_file" | head -n 1)
echo "Last Commit id: $last_commit"
echo "Saved Commit id:  $saved_commit"

if [[ "$last_commit" == "$saved_commit" ]]; then
    echo "No new commit found"
else
    echo "New commit found"
    git pull
    new_commit_id=$(git log -1 --pretty=format:"%H")
    # Update the commit file with the new commit id
    echo "$new_commit_id" > "$commit_file" # Need to echo only then > will save the file 
fi


# if [ $last_commit ]
# cat latest_commit.txt | head -n 1 > text.txt

# last_commit= $(cat $commit_file) || echo "No previous commit found"
# echo "Last commit: $last_commit"


# git log -1 --pretty=format:"%h - %an, %ar : %s" > $commit_file
# echo "Latest commit details saved in $commit_file"

# if [ -d "$folder_path" ]; then
#     cd $folder_path
#     # git pull
#     git log -1 --pretty=format:"%h - %an, %ar : %s" > $commit_file
#     echo "Latest commit details saved in $commit_file"
# else
#     echo "Folder $folder_path does not exist"
# fi


