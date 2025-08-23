from random import choice


class SuccessRatio:
    """A class checking for success ratio."""

    def __init__(self, success_chance=1, failure_chance=2, rolls=50):
        """Initialize variables for calculations"""
        self.success_to_failure_ratio = []
        self.success_chance = self._return_chance_ratio(success_chance)
        self.failure_chance = self._return_chance_ratio(failure_chance)
        self.rolls = rolls
    

    def _return_chance_ratio(self, die):
        """Prepares dies for analysis"""
        return [chance for chance in range(1, die + 1)]

    def randomize_results(self):
        """Randomizes Results to store successes and failures"""
        for ratio in range(1, self.rolls + 1):
            randomize_result = choice(self.failure_chance)
            if randomize_result in self.success_chance:
                self.success_to_failure_ratio.append("Success")
            else:
                self.success_to_failure_ratio.append("Failure")
    
    def check_chances(self):
        """Checks for % ratio of Success and Failure."""
        chance_to_success = self._calculate_chance(self._count_chance("Success"))
        chance_to_fail = self._calculate_chance(self._count_chance("Failure"))
        print(f"the Success have: {chance_to_success * 100}% chance to succeed")
        print(f"the Success have: {chance_to_fail * 100}% chance to fail")
    
    def _count_chance(self, chance):
        """Returns occurences of successes or failures in a list."""
        return self.success_to_failure_ratio.count(chance)
    
    def _calculate_chance(self, chance):
        """Returns % of successes and failures"""
        return chance / len(self.success_to_failure_ratio)


new = SuccessRatio(1, 20)
new.randomize_results()
new.check_chances()
