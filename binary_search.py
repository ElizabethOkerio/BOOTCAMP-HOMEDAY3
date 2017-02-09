class BinarySearch(list):
  
  def __init__(self, a, b):
    self.a = a
    self.b = b    
    for y in range(1,a+1):
      self.append(y*b)

    self.length = len(self)

  def search(self, num_to_search):
    self.sort() 
    
    first = 0
    last = self.length - 1
    
    count = 0
    while 1:

      middle = ((first + last) // 2) 
      if first > last or middle > last:
        return {'count':count, 'index':-1}
      
      if self[middle] == num_to_search:
        return {'count':count, 'index':middle}
      elif self[last] == num_to_search:
        return {'count':count, 'index':last}
      elif self[first] == num_to_search:
        return {'count':count, 'index':first}
      elif middle==first or middle==last:
        return {'count':count, 'index':-1}      
      elif self[middle] < num_to_search:
        first = middle + 1
      elif self[middle] > num_to_search:

        last = middle - 1

    count+=1