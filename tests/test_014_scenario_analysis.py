import unittest

from merchant_risk_router.models import Record
from merchant_risk_router.scoring import score_record


class DepthCheck14(unittest.TestCase):
    def test_014_scenario_analysis(self):
        record = Record(id="merchant-014", exposure=10917, signal=0.671, urgency=8)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
