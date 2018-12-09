#include <stdio.h>

int main() {
    int elfs[411] = {0};
    int marbles = 71170;
    static int circle[71170] =  { 0 };

    int c, e, val2;
    int m = 1;
    int curr = 0;
    int added = 1;
    while (m < marbles){
      if (m % 23 == 0){
        e = (m-1) % 411;
        val2 = (curr - 7 + added) % added;
        elfs[e] += m + circle[val2];

        // Delete att index e
        for (c = val2 ; c < added -1; c++)
          circle[c] = circle[c+1];
        added--;
        curr = val2;
      } else {
        int i = ((curr + 1) % added) + 1;
        // Insert at index i
        for (c = added - 1; c >= i - 1; c--)
          circle[c+1] = circle[c];
        circle[i] = m;
        curr = i;
        added++;
      }
      m++;
    }

    int max = 0;
    int i;
    for(i = 0; i < 411; i++){
      if(elfs[i] > max){
        max = elfs[i];
      }
    }
    printf("Answer: %d \n", max);
}
