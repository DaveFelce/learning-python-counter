class Read:
    """Read stuff"""

    def read_lines(self, filename):
        """Read lines from file into list
        
        Params: filename
        Returns: list of lines from file
        """

        all_lines = []
        with open(filename) as fh:
            for line in fh:
                all_lines.append([int(char) for char in line.strip().split(',')])

        return all_lines
