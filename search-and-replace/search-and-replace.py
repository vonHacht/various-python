import logging
import re

from logs import init_output_formatters


class MyRegex:
    _regex = r"\"(.*)\":((\".*\",)|(.*,)|(.*))"
    # _regex = r"(\")([A-Z])(.*:.*)"

    @staticmethod
    def substitute(content):
        return re.sub(MyRegex._regex, MyRegex._convert_json, content)

    @staticmethod
    def _convert_case(match_obj):
        return match_obj.group(1) + match_obj.group(2).lower() + match_obj.group(3)

    @staticmethod
    def _convert_json(match_obj):
        first = match_obj.group(1).lower()
        second = match_obj.group(2)

        for c in ["-", "(", ")", " ", "_"]:
            first = first.replace(c, "")

        for c in [",", "\""]:
            second = second.replace(c, "")

        second = f"\'{second}\'"

        return first + ":" + second + ","


if __name__ == '__main__':
    init_output_formatters('debug')

    logging.info("Search and replace")

    i = "C:\\Software\\git\\MetricApp\\app\\src\\components\\templatereport2_original.js"
    o = "C:\\Software\\git\\MetricApp\\app\\src\\components\\templatereport2_output.js"

    with open(i, "r") as io:
        content = io.read()

    content = MyRegex.substitute(content)

    content = content.replace("templatereport2_original", "templatereport2_output")

    logging.info(content.lower())

    if o:
        with open(o, "w") as io:
            io.write(content)
