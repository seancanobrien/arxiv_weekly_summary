#!/bin/bash

# Takes in a filter file with an email at the top. Makes the relevant weekly update, then sends that email the weekly update

local_dir="/home/sean/arxiv_weekly_summary/data_local_copy"

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
      mkdir -p "$specific_email_store_dir"
      echo "made directory $specific_email_store_dir"
  fi

  update_html=$(~/arxiv_weekly_summary/venv/bin/python3 ~/arxiv_weekly_summary/src/main.py t t $1 $specific_email_store_dir)

  if [[ -n $update_html && -f $update_html && -s $update_html ]]
  then
    echo "generated file $update_html"
    mutt -e 'set content_type=text/html' -s 'Weekly Arxiv Update' $send_email < $update_html
    echo "sent email containing $update_html to $send_email"
  else
    echo "some error with generated file: $update_html"
  fi
}

clean_and_process_file() {
  local filter_file=$1
  if [[ -f $filter_file && -s $filter_file ]]
  then
	  if file $filter_file | grep -q "text"
	  then
	    echo "-------------------------------------"
	    echo "collected filter file $filter_file"
	    # fix potential dos carriage returns
	    dos2unix $filter_file
	    sed -i 's/\r/\n/g' $filter_file
	    construct_summary_and_send_email $filter_file
	  else
	    echo "$filter_file is not a plain text file, skipping"
	  fi
  else
    echo "$filter_file is not a file or is empty, skipping"
  fi
}

process_all_files() {
  echo "-------------------------------------"
  echo "cleaning and processing filter file"

  for local_filter_file in "$local_dir/filters/"*
  do
    clean_and_process_file "$local_filter_file"
  done
}

process_single_file() {
  local file=$1
  local local_copy_file="$local_dir/filters/$(basename $file)"
  clean_and_process_file "$local_copy_file"
}

if [[ $# -eq 0 ]]; then
  process_all_files
else
  process_single_file "$1"
fi
