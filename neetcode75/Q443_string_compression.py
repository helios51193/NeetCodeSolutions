class Solution:
    def compress(self, chars: list[str]) -> int:
        
        # use 2 pointers , read and write
        write = 0
        read = 0
        while read < len(chars):
            ch = chars[read]
            count = 1

            while read + 1 < len(chars) and ch == chars[read + 1]:
                count += 1
                read += 1
            
            read +=1

            # Write character
            chars[write] = ch
            write += 1

            if count > 1:
                count_str = str(count)
                for c in count_str:
                    chars[write] = c
                    write += 1
        
        return write

"""
    Last Looked
    30-12-25

"""  