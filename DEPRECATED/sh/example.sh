source ./savesys.sh

save_exists # Generate file
save_refresh # Create/update array (aptly named arr)

echo Original var: ${arr[1]}

save_writer 1 7; echo "Replacing line 1 with '7'"
save_refresh

echo New var: ${arr[1]}
