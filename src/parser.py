import json

def calculate_pass_rate(results: dict) -> float:
  total_tests = results['stats']['tests']
  passes = results['stats']['passes']
  failures = results['stats']['failures']
  return  passes / total_tests *100

def get_failed_tests(results: dict) -> list:
  failed_tests = []
  for item in results['results']:
    for suite in item['suites']:
       for test in suite['tests']:
         if test['state'] == 'failed':
           failed_tests.append(test)
  return failed_tests

class TestSuite:
  def __init__(self, results: dict):
    self.results = results


  def get_failures(self) -> list:
    return get_failed_tests(self.results)

  def get_pass_rate(self) -> float:
    return calculate_pass_rate(self.results)

  def get_duration_seconds(self) -> float:
    return self.results['stats']['duration'] / 1000

  def __repr__(self) -> str:
    return f"TestSuite(pass_rate={self.get_pass_rate()}, Total Failures ={len(self.get_failures())})"


if __name__ == "__main__":
  with open('sample_data/cypress_results_sample.json') as f:
       results = json.load(f)
       print(f"Pass rate: {calculate_pass_rate(results)}%")
       result = get_failed_tests(results)
       print(f"Failed tests: {result}")
       print(f"Total failed tests: {len(result)}")
       suite = TestSuite(results)
       print(suite)
       print(f"Duration: {suite.get_duration_seconds()} seconds")
