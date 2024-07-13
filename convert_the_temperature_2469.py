from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [float(celsius+273.15), float((celsius*1.80)+32.00)]
