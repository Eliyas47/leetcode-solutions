class Solution:
    def interpret(self, command):
        result = command.replace("()", "o")
        result = result.replace("(al)", "al")
        return result
