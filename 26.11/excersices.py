from dataclasses import dataclass, field


@dataclass
class Test:
    first_int: int
    multiplier: int
    list_of_ints: list[int]
    calculated_val: float = field(init=False)
    second_int: int = 0

    def __post_init__(self):
        self.calculated_val = (self.first_int * self.multiplier * sum(self.list_of_ints)) - self.second_int

    def __eq__(self, other):
        if self.calculated_val == other.calculated_val:
            return True
        else:
            return False

    def __call__(self, *args, **kwargs):
        return self.calculated_val

    def __str__(self):
        return f"{self.calculated_val}"

    def __repr__(self):
        return f"repr {self.calculated_val}"


if __name__ == "__main__":
    test_result = Test(2, 2, [2, 1], 9)
    print(test_result)
    print(test_result())
