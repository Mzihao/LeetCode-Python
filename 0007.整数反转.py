class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        if x_str[0] != '-' and x_str[-1] != '0':
            x_str = ''.join(list(reversed(x_str)))
            return self.returnX(int(x_str))
        elif x_str[0] == '-' and x_str[-1] != '0':
            x_str = x_str[1:]
            x_str = '-' + ''.join(list(reversed(x_str)))
            return self.returnX(int(x_str))
        elif x_str[0] == '-' and x_str[-1] == '0':
            x_str = x_str[1:]
            while x_str[-1] == '0':
                x_str = self.remove0(x_str)
            return self.returnX(int('-' + ''.join(list(reversed(x_str)))))
        elif x_str[0] != '-' and x_str[-1] == '0':
            while x_str[-1] == '0':
                x_str = self.remove0(x_str)
                if len(x_str) == 0:
                    return 0
            return self.returnX(int(''.join(list(reversed(x_str)))))

    def remove0(self, x: str) -> str:
        return x[:-1]

    def returnX(self, x: int) -> int:
        if -2 ** 31 <= x <= 2 ** 31:
            return x
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    x = s.reverse(123)
    print(x)
