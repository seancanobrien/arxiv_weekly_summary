#!/bin/bash

# Takes in a filter file with an email at the top. Makes the relevant weekly update, then sends that email the weekly update

# There are remote and local copies of the filter files
# and the stored summaries. This is because using rclone directly
# on a remote seems unreliable
remote_dir="google_drive:arxiv_summaries_per_email"
local_dir="/home/sean/.local/arxiv_weekly_summary/data_local_copy"

local_summary_store="$local_dir/summaries"

construct_summary_and_send_email() {
  # Read the first line of the supplied file
  # This is the relavant email address
  read -r send_email < "$1"

  echo "sending update email to $send_email"

  specific_email_store_dir="$local_summary_store/$send_email"
  echo "storing update html in $specific_email_store_dir"

  if [[ ! -d $specific_email_store_dir ]]
  then
      mkdir "$specific_email_store_dir"
      echo "made directory $specific_email_store_dir"
  fi

  update_html=$(/home/sean/.local/arxiv_weekly_summary/env/bin/python3 /home/sean/.local/arxiv_weekly_summary/src/main.py t t $1 $specific_email_store_dir)

  if [[ -n $update_html && -f $update_html && -s $update_html ]]
  then
    echo "generated file $update_html"
    # mutt -e 'set content_type=text/html' -s 'Weekly Arxiv Update' $send_email < $update_html
    echo "sent email containing $update_html to $send_email"
  else
    echo "some error with generated file: $update_html"
  fi
}

echo "-------------------------------------"
echo "syncing filters from remote"
# now upload the local update files to remote
# Copy over the filter files, enuring they are synchronised with remote filter files
rclone sync "$remote_dir/filters" "$local_dir/filters"

for local_filter_file in "$local_dir/filters/"*
do
  if [[ -f $local_filter_file && -s $local_filter_file ]]
  then
    echo "-------------------------------------"
    echo "collected filter file $local_filter_file"
    # fix potential dos carriage returns
    dos2unix $local_filter_file
    sed -i 's/\r/\n/g' $local_filter_file
    construct_summary_and_send_email $local_filter_file
  else
    echo "$local_filter_file is not a file or is empty, skipping"
  fi
done

echo "-------------------------------------"
echo "copying summaries to remote"
# now upload the local update files to remote
rclone copy $local_summary_store "$remote_dir/summaries/"
echo "-------------------------------------"
