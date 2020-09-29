class FileNameExtractor:
    def extract_file_name(dirty_file_name):
        for i, j in enumerate(dirty_file_name):
            if not j.isdigit():
                return ".".join(dirty_file_name[i+1:].split(".")[:2])
