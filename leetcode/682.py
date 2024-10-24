class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # python version >= 3.10
        stack_of_records = []
        for op in operations:
            print(stack_of_records, op)
            match op:
                case '+':
                    b = stack_of_records.pop()
                    a = stack_of_records.pop()
                    stack_of_records.append(int(a))
                    stack_of_records.append(int(b))
                    stack_of_records.append(int(a + b))
                case 'D':
                    stack_of_records.append(stack_of_records[-1]*2)
                case 'C':
                    stack_of_records.pop()
                case _:
                    stack_of_records.append(int(op))
        return sum(stack_of_records)

