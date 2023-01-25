import shelve, os, sys

class FileManager:
    def __init__(self, dir : str) -> None:
        self.parent_dir = dir
        self.save_dir = self.get_save_dir()
    def get_save_dir(self) -> str:
        '''
        returns where assets SHOULD be looked for if the program is frozen vs running in ide
        '''
        save_folder_path = ''
        if getattr(sys, 'frozen', False):
            # frozen program
            save_folder_path = os.path.dirname(sys.executable)
        else:
            # not frozen
            save_folder_path = os.path.dirname(self.parent_dir)
        return os.path.join(save_folder_path, 'save')