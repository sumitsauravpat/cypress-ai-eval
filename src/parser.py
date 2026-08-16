import json

with open('sample_data/cypress_results_sample.json') as f:

     results = json.load(f)

def calculate_pass_rate(results: dict) -> float:
  total_tests = results['stats']['tests']
  passes = results['stats']['passes']
  failures = results['stats']['failures']
  return  passes / total_tests *100



print(f"Pass rate: {calculate_pass_rate(results)}%")


def get_failed_tests(results: dict) -> list:
  failed_tests = []
  for item in results['results']:
    for suite in item['suites']:
       for test in suite['tests']:
         if test['state'] == 'failed':
           failed_tests.append(test)
  return failed_tests

result = get_failed_tests(results)

print(f"Failed tests: {result}")
print(f"Total failed tests: {len(result)}")
