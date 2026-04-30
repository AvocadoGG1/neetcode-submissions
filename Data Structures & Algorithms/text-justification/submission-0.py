class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = [] # Array
        line, length = [], 0 # curr line, curr line length
        i = 0 # pointer

        while i < len(words): # loop through words
            if length + len(line) + len(words[i]) > maxWidth: # words + each space for word and length of curr line, check if exceed maxWidth
                # Line complete
                extra_space = maxWidth - length # distribute extra space evenly, not including spaces
                spaces = extra_space // max(1, len(line) - 1) # spaces between each word
                remainder = extra_space % max(1, len(line) - 1) # get reminder spaces distribute left to right in greedy way

                # add spaces to curr line 
                for j in range(max(1, len(line) - 1)): # get around the edge case of one word with max()
                    line[j] += " " * spaces # take string and mutliply by integer (only python)
                    if remainder: # if remainder non zero
                        line[j] += " " # take one extra space and add space to end
                        remainder -= 1 
                res.append("".join(line)) # take all the words and join them together, delimiter -> ""
                line, length = [], 0 # Reset line and length
                
            line.append(words[i])  # Add curr word to curr line
            length += len(words[i]) # update length of curr line, not including spaces
            i += 1 # get to next word
        # Handling last line
        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line) # add space to end
        res.append(last_line + " " * trail_space)
        return res