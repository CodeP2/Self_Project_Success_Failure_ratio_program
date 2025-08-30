from success_failure_ratio import SuccessRatio
import matplotlib as plt


class VisualizeRatio:
    """"""

    def __init__(self):
        """"""

    def _get_ratio_and_amount_numbers(self):
        """"""
        self.get_success, self.get_failure = input("What is the success/failure ratio (ex. 1/2)\n> ").split("/")
        self.get_amount = input("What is the number of attempts?\n> ")
        self._change_str_to_int(self.get_success, self.get_failure, self.get_amount)
        print(type(self.get_success))
    
    def _change_str_to_int(self, *args):
        """"""
        for each in args:
            int(each)
            print(each)
            print(type(each))


check = VisualizeRatio()
check._get_ratio_and_amount_numbers()
