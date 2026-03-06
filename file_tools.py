import os
import shutil


class RenameSingleFile:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "file_path": ("STRING", {"default": ""}),
                "new_name": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("new_file_path",)
    FUNCTION = "rename_file"
    CATEGORY = "Mikhail/File Tools"

    def rename_file(self, file_path, new_name):
        if not file_path:
            raise ValueError("file_path is empty")

        if not new_name:
            raise ValueError("new_name is empty")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File does not exist: {file_path}")

        folder = os.path.dirname(file_path)
        new_file_path = os.path.join(folder, new_name)

        if os.path.abspath(file_path) == os.path.abspath(new_file_path):
            return (new_file_path,)

        os.rename(file_path, new_file_path)
        return (new_file_path,)


class MoveSingleFile:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "file_path": ("STRING", {"default": ""}),
                "destination_path": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("new_file_path",)
    FUNCTION = "move_file"
    CATEGORY = "Mikhail/File Tools"

    def move_file(self, file_path, destination_path):
        if not file_path:
            raise ValueError("file_path is empty")

        if not destination_path:
            raise ValueError("destination_path is empty")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File does not exist: {file_path}")

        dest_folder = os.path.dirname(destination_path)
        if dest_folder:
            os.makedirs(dest_folder, exist_ok=True)

        shutil.move(file_path, destination_path)
        return (destination_path,)


NODE_CLASS_MAPPINGS = {
    "RenameSingleFile": RenameSingleFile,
    "MoveSingleFile": MoveSingleFile,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RenameSingleFile": "Rename Single File",
    "MoveSingleFile": "Move Single File",
}
