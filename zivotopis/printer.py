# -*- coding: utf-8 -*-
from cStringIO import StringIO
from django.conf import settings
from django.template.defaultfilters import linebreaksbr
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Table, TableStyle, Paragraph, SimpleDocTemplate
from reportlab.pdfgen import canvas
from zivotopis.forms import CVForm
import os
import time

FONT_PATH = os.path.join(settings.STATIC_ROOT, 'elektrijada/fonts/OpenSans-Regular.ttf')
pdfmetrics.registerFont(TTFont('OpenSans', FONT_PATH))
FONT_PATH = os.path.join(settings.STATIC_ROOT, 'elektrijada/fonts/OpenSans-Bold.ttf')
pdfmetrics.registerFont(TTFont('OpenSans-Bold', FONT_PATH))


class NumberedCanvas(canvas.Canvas):
    page_title = ''

    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.setFont('OpenSans', 9)
        self.drawRightString(A4[0] - 2.5*cm, 2*cm, '%d/%d' % (self._pageNumber, page_count))
        self.drawString(2.5*cm, 2*cm, 'Datum ispisa: %s' % time.strftime('%d.%m.%Y.'))


def cv_pdf(cv):
    output = StringIO()
    # A4 29.7 x 21 cm
    doc = SimpleDocTemplate(output, showBoundary=0)
    elements = []
    NumberedCanvas(output)

    table_title = Table([(cv.full_name, u'Elektrijada - Životopis'), ('', '')],  repeatRows=0,
                        style=TableStyle([
                            ('LINEBELOW', (0, 1), (-1, -1), 1, colors.lightgrey),
                            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                            ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
                            ('FONT', (0, 0), (-1, -1), 'OpenSans'),
                            ('FONTSIZE', (0, 0), (-1, -1), 16),
                            ('FONTSIZE', (1, 0), (-1, -1), 13),
                        ]),
                        colWidths=[11.0*cm, 5.0*cm],
                        rowHeights=[0.5*cm, 0.5*cm])
    elements.append(table_title)

    attrs = []
    for field in CVForm(instance=cv):
        attrs.append((field.label, unicode(linebreaksbr(field.value()))))
    # Wrap into paragraphs
    style = ParagraphStyle(
        name='Table',
        fontName='OpenSans',
        fontSize=11,
    )
    para_data = []
    for row in attrs:
        para_data.append([Paragraph(col, style) for col in row])

    table = Table(para_data,  repeatRows=0,
                  style=TableStyle([
                      ('LINEBELOW', (0, 0), (-1, -1), 1, colors.lightgrey),
                      ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                      ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                  ]),
                  colWidths=[5.00*cm, 11*cm])
    elements.append(table)

    doc.build(elements, canvasmaker=NumberedCanvas)
    return output.getvalue()
