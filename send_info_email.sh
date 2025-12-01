#!/bin/bash

# Takes in a filter file with an email at the top. Makes the relevant weekly update, then sends that email the weekly update
local_dir="/home/sean/arxiv_weekly_summary/data_local_copy"
message_file="$local_dir/info_message.txt"

send_single_email() {
    # Usage:
    #   send_single_email recipient@example.com message_file.txt
    #
    # message_file.txt format:
    #   line 1 = subject
    #   line 2+ = body

    if [[ $# -ne 2 ]]; then
        echo "Usage: send_single_email recipient_email message_file"
        return 1
    fi

    local recipient="$1"
    local file="$2"

    if [[ ! -f $file || ! -s $file ]]; then
        echo "Message file does not exist or is empty."
        return 1
    fi

    # Normalize line endings
    dos2unix "$file" 2>/dev/null
    sed -i 's/\r/\n/g' "$file"

    # Extract subject & body
    local subject
    subject=$(sed -n '1p' "$file")

    local body
    body=$(tail -n +2 "$file")

    # Send via mutt (plain text)
    printf "%s\n" "$body" | mutt -s "$subject" -- "$recipient"
}

send_emails_for_each_filter_file() {
  for local_filter_file in "$local_dir/filters/"*
  do
    read -r send_address < "$local_filter_file"
    echo "Sending info email to: $send_address"
    send_single_email "$send_address" "$message_file"
  done
}

send_emails_for_each_filter_file
