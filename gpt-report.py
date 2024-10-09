from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm

# Create a reusable PDF generation function
def generate_financial_report(filename, client_name, month, total_assets, portfolio_return, return_period):
    # Set up the document
    doc = SimpleDocTemplate(filename, pagesize=A4,
                            rightMargin=36, leftMargin=36,
                            topMargin=36, bottomMargin=36)
    styles = getSampleStyleSheet()
    story = []

    # Title and Header
    header_style = ParagraphStyle(
        name="HeaderStyle",
        fontSize=28,
        leading=34,
        alignment=1,
        fontName='Helvetica-Bold'
    )
    header = Paragraph("ekho", header_style)
    story.append(header)
    story.append(Spacer(1, 12))

    title_style = ParagraphStyle(
        name="TitleStyle",
        fontSize=16,
        leading=20,
        alignment=1,
        fontName='Helvetica-Bold'
    )
    title = Paragraph(f"RELATÓRIO DE CONSOLIDAÇÃO / RESUMO - {month.upper()} 2024", title_style)
    story.append(title)
    story.append(Spacer(1, 24))

    # Insights Section
    insights_title_style = ParagraphStyle(
        name="InsightsTitleStyle",
        fontSize=14,
        leading=18,
        fontName='Helvetica-Bold'
    )
    insights_text_style = ParagraphStyle(
        name="InsightsTextStyle",
        fontSize=12,
        leading=14,
        fontName='Helvetica'
    )
    insights_title = Paragraph("INSIGHTS", insights_title_style)
    story.append(insights_title)
    story.append(Spacer(1, 12))

    insights_text = (
        f"Olá {client_name}, seu patrimônio global em {month} é de <b>R$ {total_assets:,}</b>.<br/>        Sua carteira rendeu <b>R$ {portfolio_return:,}</b> em {month}, descontando inflação.<br/>        O rendimento no período foi de <b>R$ {return_period:,}</b>."
    )
    insights_paragraph = Paragraph(insights_text, insights_text_style)
    story.append(insights_paragraph)
    story.append(Spacer(1, 24))

    # Breakdown Patrimônio Global
    breakdown_title = Paragraph("BREAKDOWN PATRIMÔNIO GLOBAL", insights_title_style)
    story.append(breakdown_title)
    story.append(Spacer(1, 12))

    # Placeholder for Breakdown Chart
    chart_placeholder = Paragraph("[Gráfico de Breakdown Patrimônio Global]", insights_text_style)
    story.append(chart_placeholder)
    story.append(Spacer(1, 24))

    # Detalhamento por Ativo Section
    detalhamento_title = Paragraph("DETALHAMENTO POR ATIVO", insights_title_style)
    story.append(detalhamento_title)
    story.append(Spacer(1, 12))

    # Performance Charts Placeholder
    performance_chart_placeholder = Paragraph("[Gráficos de Performance - Private Equity, Real Estate, etc.]", insights_text_style)
    story.append(performance_chart_placeholder)
    story.append(Spacer(1, 24))

    # Histórico / Performance Mensal e Custódia Global
    performance_title = Paragraph("HISTÓRICO / PERFORMANCE MENSAL E CUSTÓDIA GLOBAL", insights_title_style)
    story.append(performance_title)
    story.append(Spacer(1, 12))

    # Table for Historical Performance
    performance_data = [["Ano", "Rentabilidade", "Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Acumulado"],
                        ["2024", "CARTEIRA", "0,8%", "0,8%", "1,2%", "-0,8%", "0,5%", "1%", "1,3%", "14,1%"],
                        ["2023", "CARTEIRA", "0,2%", "1,5%", "1,8%", "0,9%", "0,5%", "0,7%", "1,5%", "8,8%"],
                        ["2022", "%CDI", "88,5%", "129,4%", "164,6%", "84,2%", "41,0%", "70,3%", "160,2%", "100,2%"]]

    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    performance_table = Table(performance_data, colWidths=[2 * cm] * 9)
    performance_table.setStyle(table_style)
    story.append(performance_table)
    story.append(Spacer(1, 24))

    # Disclaimer Section
    disclaimer_style = ParagraphStyle(
        name="DisclaimerStyle",
        fontSize=8,
        leading=10,
        textColor=colors.grey,
        spaceBefore=20
    )
    disclaimer_text = (
        "Este material é informativo, não sendo uma oferta de venda ou recomendação de investimento dos ativos mencionados. "
        "Ao aplicar seus recursos, aconselha-se aos investidores a leitura cuidadosa dos regulamentos dos fundos e informações complementares, "
        "bem como do Contrato de Gestão firmado com a Gestora."
    )
    disclaimer_paragraph = Paragraph(disclaimer_text, disclaimer_style)
    story.append(disclaimer_paragraph)

    # Build the PDF
    doc.build(story)

# Example usage
generate_financial_report(
    filename="financial_report.pdf",
    client_name="João Silva",
    month="Julho",
    total_assets=61515530,
    portfolio_return=21780000,
    return_period=753700
)