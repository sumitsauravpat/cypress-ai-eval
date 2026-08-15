import json

with open('sample_data/cypress_results_sample.json') as f:

     results = json.load(f)

def calculate_pass_rate(results: dict) -> float:
  total_tests = results['stats']['tests']
  passes = results['stats']['passes']
  failures = results['stats']['failures']
  return  passes / total_tests *100



print(f"Pass rate: {calculate_pass_rate(results)}%")
