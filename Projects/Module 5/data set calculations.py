import statistics
from typing import List, Union

def get_data() -> List[Union[int, float]]:
    """Get data set from user input."""
    data = input("Enter numbers separated by spaces: ").split()
    return [float(x) for x in data]

def find_minimum(data: List[Union[int, float]]) -> Union[int, float]:
    """Find minimum value in data set."""
    return min(data)

def find_maximum(data: List[Union[int, float]]) -> Union[int, float]:
    """Find maximum value in data set."""
    return max(data)

def find_mode(data: List[Union[int, float]]) -> Union[int, float]:
    """Find mode (most frequent value) in data set."""
    return statistics.mode(data)

def find_median(data: List[Union[int, float]]) -> Union[int, float]:
    """Find median value in data set."""
    return statistics.median(data)

def find_mean(data: List[Union[int, float]]) -> float:
    """Find mean (average) of data set."""
    return statistics.mean(data)

def find_range(data: List[Union[int, float]]) -> Union[int, float]:
    """Find range of data set."""
    return max(data) - min(data)

def find_standard_deviation(data: List[Union[int, float]]) -> float:
    """Find standard deviation of data set."""
    return statistics.stdev(data)

def main():
    """Main function to display all statistics."""
    data = get_data()
    
    print(f"\nMinimum: {find_minimum(data)}")
    print(f"Maximum: {find_maximum(data)}")
    print(f"Mode: {find_mode(data)}")
    print(f"Median: {find_median(data)}")
    print(f"Mean: {find_mean(data)}")
    print(f"Range: {find_range(data)}")
    print(f"Standard Deviation: {find_standard_deviation(data)}")

if __name__ == "__main__":
    main()