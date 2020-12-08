def gnomeSort(array):
  pos = 0
  while pos < len(array):
    if (pos == 0 or array[pos] >= array[pos - 1]):
      pos += 1
    else:
      #Begin swap
      aux = array[pos]
      array[pos] = array[pos - 1]
      array[pos - 1] = aux
      #End swap
      pos -= 1
  return array
