class SplitByEmptyLine:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
            }
        }

    # 返回一个列表类型（LIST）
    RETURN_TYPES = ("LIST",)
    RETURN_NAMES = ("list",)
    FUNCTION = "do_split"
    CATEGORY = "TextUtils"

    def do_split(self, text):
        # 按空行切割，并去掉空白段落
        parts = [p.strip() for p in text.split("\n\n") if p.strip()]

        # 返回 Python list（ComfyUI 会自动作为 LIST 处理）
        return (parts,)


NODE_CLASS_MAPPINGS = {
    "SplitByEmptyLine": SplitByEmptyLine,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SplitByEmptyLine": "Split Text by Empty Line (List)",
}
