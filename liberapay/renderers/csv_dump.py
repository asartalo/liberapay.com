import csv
from io import StringIO

from aspen.simplates import renderers


class Renderer(renderers.Renderer):

    def render_content(self, context):
        rows = eval(self.compiled, globals(), context)
        if not rows:
            return ''
        f = StringIO()
        w = csv.writer(f)
        if hasattr(rows[0], '_fields'):
            w.writerow(rows[0]._fields)
        w.writerows(rows)
        f.seek(0)
        return f.read()


class Factory(renderers.Factory):
    Renderer = Renderer
