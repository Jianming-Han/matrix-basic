class Matrix:
    """

    """

    def __init__(self):
        self.arr = []


    def add(self, arr1, arr2):
        """

        """
        try:
            return [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]
        except:
            print('matrices are not in same size!')
            return None


    def subtract(self, arr1, arr2):
        """

        """
        try:
            return [[arr1[i][j] - arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]
        except:
            print('matrices are not in same size!')
            return None


    def multiply(self, arr1, arr2):
        """

        """
        try:
            return [[sum(a*b for a, b in zip(arr1_row, arr2_col)) for arr2_col in zip(*arr2)] for arr1_row in arr1]
        except:
            print('matrices unable to multiply')
            return None


    def transpose(self, arr1):
        """

        """
        return [[arr1[i][j] for i in range(len(arr1))] for j in range(len(arr1[0]))]
