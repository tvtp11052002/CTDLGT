bubble_sort <- function(x)
{
  n <- length(x)
  
  for (i in 1 : (n - 1)) {
    
    for (j in 1 : (n - i)) {
      if (x[j] > x[j + 1]) {
        temp <- x[j]
        x[j] <- x[j + 1]
        x[j + 1] <- temp
      }
    }
  }
  x
}


arr <- c(4, 6, 7, 8, 9)
sorted_array <- bubble_sort(arr)
sorted_array