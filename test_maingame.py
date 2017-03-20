import unittest
from unittest.mock import Mock, patch
from maingame import printEmptyLine
 
 
class PrintHelloTestCase(unittest.TestCase):
    @patch("builtins.print",autospec=True)
    def test_somethingelse(self, mock_print):
        printEmptyLine()
        mock_print.assert_called_with("")
 
if __name__ == '__main__':
    printEmptyLine()
