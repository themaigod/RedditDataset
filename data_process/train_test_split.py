"""
split data into train, val, test
"""

from typing import List
import random


class SplitData:
    def __init__(self, ratio: List[float] = (0.7, 0.15, 0.15)):
        """
        ratio: list of floats, sum(ratio) == 1
        """

        if not sum(ratio) == 1:
            ratio = [i / sum(ratio) for i in ratio]

        if len(ratio) > 3:
            print("Warning: more than 3 splits. Please check if this is intended.")
        elif len(ratio) == 2:
            print(
                "Warning: only 2 splits. Please check if this is intended. If so, the second split will be used as test set.")
        elif len(ratio) != 3:
            raise ValueError("Invalid number of splits. Please specify 2 or 3 splits.")

        self.ratio = ratio

    def split(self, time_tuples):
        """
        time_tuples: list of tuples of (time, data)
        """
        time_tuples = sorted(time_tuples, key=lambda x: x[0])
        n = len(time_tuples)
        for i in range(len(self.ratio)):
            if i == len(self.ratio) - 1:
                # yield time_tuples[-(n - n * sum(self.ratio[:i])):]
                yield [time_tuples[i] for i in range(int(n * sum(self.ratio[:i])), n)]

            else:
                # yield time_tuples[n * sum(self.ratio[:i]):n * sum(self.ratio[:i + 1])]
                yield [time_tuples[i] for i in range(int(n * sum(self.ratio[:i])), int(n * sum(self.ratio[:i + 1])))]

    @staticmethod
    def split_data(time_tuples, ratio=(0.7, 0.15, 0.15)):
        """
        time_tuples: list of tuples of (time, data)
        ratio: list of floats, sum(ratio) == 1
        """
        time_tuples = sorted(time_tuples, key=lambda x: x[0])
        n = len(time_tuples)
        for i in range(len(ratio)):
            if i == len(ratio) - 1:
                # yield time_tuples[-(n - n * sum(ratio[:i])):]
                # yield [time_tuples[i] for i in range(n - n * sum(ratio[:i]), n)]
                yield [time_tuples[i] for i in range(int(n * sum(ratio[:i])), n)]

            else:
                # yield time_tuples[n * sum(ratio[:i]):n * sum(ratio[:i + 1])]
                # yield [time_tuples[i] for i in range(n * sum(ratio[:i]), n * sum(ratio[:i + 1]))]
                yield [time_tuples[i] for i in range(int(n * sum(ratio[:i])), int(n * sum(ratio[:i + 1])))]

    def split_data_time_careless(self, time_tuples):
        """
        time_tuples: list of tuples of (time, data)
        ratio: list of floats, sum(ratio) == 1
        """
        ratio = self.ratio
        time_tuples = sorted(time_tuples, key=lambda x: x[0])
        random.shuffle(time_tuples)
        n = len(time_tuples)
        for i in range(len(ratio)):
            if i == len(ratio) - 1:
                # yield time_tuples[-(n - n * sum(ratio[:i])):]
                yield [time_tuples[i] for i in range(int(n * sum(ratio[:i])), n)]

            else:
                # yield time_tuples[n * sum(ratio[:i]):n * sum(ratio[:i + 1])]
                yield [time_tuples[i] for i in range(int(n * sum(ratio[:i])), int(n * sum(ratio[:i + 1])))]


class SplitNodes:
    def __init__(self, ratio: List[float] = (0.7, 0.15, 0.15)):
        """
        ratio: list of floats, sum(ratio) == 1
        """

        if not sum(ratio) == 1:
            ratio = [i / sum(ratio) for i in ratio]

        if len(ratio) > 3:
            print("Warning: more than 3 splits. Please check if this is intended.")
        elif len(ratio) == 2:
            print(
                "Warning: only 2 splits. Please check if this is intended. If so, the second split will be used as test set.")
        elif len(ratio) != 3:
            raise ValueError("Invalid number of splits. Please specify 2 or 3 splits.")

        self.ratio = ratio

    def split(self, time_tuples, nodes: List[List[int]]):
        """
        time_tuples: list of tuples of (time start, time end)
        """
        time_tuples = sorted(time_tuples, key=lambda x: x[0])
        n = len(time_tuples)
        return_result = []
        for i in range(len(self.ratio)):
            return_result.append([])

        for i in range(len(time_tuples)):
            length = len(nodes[i])
            temp_nodes = nodes[i]
            # print(temp_nodes)
            # raise ValueError
            for j in range(len(self.ratio)):
                if len(temp_nodes) < 10:
                    return_result[j].append([])
                random.shuffle(temp_nodes)
                if j == len(self.ratio) - 1:
                    # return_result[j].append(
                    #     temp_nodes[-(length - length * sum(self.ratio[:j])):])
                    return_result[j].append(
                        temp_nodes[int(length * sum(self.ratio[:j])):])
                else:
                    # return_result[j].append(temp_nodes[
                    #                         length * sum(self.ratio[:j]):length * sum(
                    #                             self.ratio[:j + 1])])
                    return_result[j].append(temp_nodes[
                                             int(length * sum(self.ratio[:j])):int(length * sum(
                                                 self.ratio[:j + 1]))])
        return return_result
