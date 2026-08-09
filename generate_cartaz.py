from reportlab.lib.pagesizes import mm
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from pathlib import Path

root = Path(__file__).resolve().parent
output = root / 'cartaz_pao_por_deus.pdf'
qr_path = root / 'site_qrcode.png'

if not qr_path.exists():
    raise FileNotFoundError(qr_path)

size = 210 * mm
c = canvas.Canvas(str(output), pagesize=(size, size))
width, height = size, size

c.setFillColor(colors.white)
c.rect(0, 0, width, height, fill=1, stroke=0)

c.setFillColor(colors.HexColor('#2f2b26'))
c.setFont('Helvetica-Bold', 32)
c.drawCentredString(width / 2, height - 35 * mm, 'PÃO-POR-DEUS')

c.setFont('Helvetica-Bold', 16)
c.drawCentredString(width / 2, height - 52 * mm, 'Espaço ideal para realização de eventos sociais e corporativos.')

qr_size = 100 * mm
qr_x = (width - qr_size) / 2
qr_y = (height - qr_size) / 2 - 5 * mm
c.setFillColor(colors.white)
c.roundRect(qr_x - 8 * mm, qr_y - 8 * mm, qr_size + 16 * mm, qr_size + 16 * mm, 10 * mm, fill=1, stroke=0)
c.drawImage(ImageReader(str(qr_path)), qr_x, qr_y, qr_size, qr_size, preserveAspectRatio=True, anchor='nw')

c.setFont('Helvetica', 12)
c.setFillColor(colors.HexColor('#6f675c'))
c.drawCentredString(width / 2, qr_y - 14 * mm, 'Todas as informações no site')

c.save()
print(f'Created {output}')
