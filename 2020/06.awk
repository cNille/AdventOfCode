BEGIN {
  FS=""       # Field separator. Sets each character a own field
}
{
  if (NF == 0){ # NF - Number of fields. 0 means empty line
    total = total + length(group)

    # Part 2
    for(letters in group) {
      if (group[letters] >= person_count) {
        total2 += 1
      }
    }
    delete group
    person_count = 0
  } else {
    person_count += 1
    for(i=1; i <= NF; i++){
      group[$i]++ 
    }
  }
}
END {
  printf "Solution part 1: " total "\n"
  printf "Solution part 2: " total2 "\n"
}
