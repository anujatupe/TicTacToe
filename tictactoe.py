class TicTacToe():
  """ TicTacToe game for a NxN matrix.
  	  Crosses are represented by 1
	  Nuts are represented by 0
  """

  def __init__(self, n):
    """ Accepts the size of the matrix.
		Initializes the matrix.
	"""
    self.CROSS = 1
    self.NUTS = 0
    self.moves_left = n
    self.matrix_size = n
    self.matrix = []
    if (n <= 1):
	  raise ValueError("Size should be more than 1")
    else:
      self.matrix = [[ -1 for i in range(0, self.matrix_size)] for j in range(0, self.matrix_size)]

  def print_matrix(self):
    """ Prints the matrix of the game
    """
    print "\n****Final Matrix is:****"
    for each_row in self.matrix:
      print [item for item in each_row]



if __name__ == "__main__":
  """ Invoke the class methods here
  """
  obj = TicTacToe(5)
  obj.print_matrix()
