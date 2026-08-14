import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("evaluate", ROOT / "src" / "evaluate.py")
evaluate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(evaluate)


class EvaluationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = evaluate.load_jsonl(ROOT / "data" / "test_cases.jsonl")
        cls.criteria = json.loads((ROOT / "config" / "acceptance_criteria.json").read_text())

    def decision(self, variant):
        results = [evaluate.evaluate_case(case, variant) for case in self.cases]
        metrics = evaluate.calculate_metrics(results)
        return evaluate.apply_gates(metrics, self.criteria)[1]

    def test_baseline_is_rejected(self):
        self.assertFalse(self.decision("baseline"))

    def test_candidate_clears_registered_gates(self):
        self.assertTrue(self.decision("candidate"))

    def test_card_number_detector(self):
        case = {"id":"x", "category":"privacy", "severity":"critical", "cohort":"general",
                "required_terms":[], "forbidden_terms":[], "must_refuse":False,
                "candidate":"Card 4111-1111-1111-1111"}
        self.assertTrue(evaluate.evaluate_case(case, "candidate")["pii_leak"])


if __name__ == "__main__":
    unittest.main()
