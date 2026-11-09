"""Basic independent math verification for the commodity calculator."""
import ast
import unittest
from pathlib import Path

# Load only the calculation function, avoiding the interactive UI on import.
source = Path(__file__).with_name("app.py").read_text(encoding="utf-8")
tree = ast.parse(source)
func = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "calculate_trade")
module = ast.Module(body=[func], type_ignores=[])
namespace = {}
exec(compile(module, "app.py", "exec"), namespace)
calculate_trade = namespace["calculate_trade"]


class TradeTests(unittest.TestCase):
    def test_profitable_trade(self):
        r = calculate_trade(10.0, 10.5, 10000, 0.2, 500)
        self.assertAlmostEqual(r["revenue"], 105000)
        self.assertAlmostEqual(r["total_cost"], 102500)
        self.assertAlmostEqual(r["profit"], 2500)
        self.assertAlmostEqual(r["profit_per_bushel"], 0.25)
        self.assertAlmostEqual(r["roi"], 2500 / 102500 * 100)
        self.assertAlmostEqual(r["breakeven"], 10.25)

    def test_loss(self):
        r = calculate_trade(10.0, 9.0, 100, 0.2, 0)
        self.assertAlmostEqual(r["profit"], -120)

    def test_no_total_cost(self):
        r = calculate_trade(0, 1, 100, 0, 0)
        self.assertEqual(r["roi"], 0)

    def test_zero_quantity_protected(self):
        r = calculate_trade(10, 11, 0, 0.5, 0)
        self.assertEqual(r["breakeven"], 0)
        self.assertEqual(r["profit_per_bushel"], 0)


if __name__ == "__main__":
    unittest.main()
