import json

from django.http import QueryDict
from rest_framework import parsers


class MultipartJsonParser(parsers.MultiPartParser):

    def parse(self, stream, media_type=None, parser_context=None):
        result = super().parse(
            stream, media_type=media_type, parser_context=parser_context
        )
        data = json.loads(result.data["data"])
        data["documents"] = []
        for key in result.files:
            data["documents"].append({"path": result.files[key]})
        return parsers.DataAndFiles(data, [])
