import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

