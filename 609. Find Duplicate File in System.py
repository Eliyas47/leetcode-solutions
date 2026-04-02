class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = {}
        
        for path in paths:
            parts = path.split(" ")
            directory = parts[0]
            for file in parts[1:]:
                name, content = file.split("(")
                content = content[:-1]  # remove trailing ')'
                full_path = directory + "/" + name
                if content not in content_map:
                    content_map[content] = []
                content_map[content].append(full_path)
        
        return [group for group in content_map.values() if len(group) > 1]
