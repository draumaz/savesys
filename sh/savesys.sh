# Savesys, an easily-implementable save manager
# draumaz, 2022 | MIT

FILE_NAME="test.txt"

save_reader() {
        while IFS= read -r line || [ -n "$line" ]; do arr+=("$line")
        done < $FILE_NAME
}

save_refresh() { # update array
        arr=()
        save_reader
}

save_writer() {
        save_refresh;
        > $FILE_NAME
        for i in {0..4}; do # ADJUST TO DESIRED LENGTH
                if [ "$1" == "$i" ]; then # match loop
                        echo "$2" >> $FILE_NAME
                fi
                echo ${arr[$i]} >> $FILE_NAME
        done
}

save_generation() {
        touch $FILE_NAME && > $FILE_NAME
        for i in {0..4}; do echo 0 >> $FILE_NAME; done # ADJUST TO DESIRED LENGTH
}

save_exists() {
        if [ ! -e $FILE_NAME ]; then save_generation; fi
}
