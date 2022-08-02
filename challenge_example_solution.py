class PDFReport:
    
    def set_xml_content(self, xml_content):
        self.xml_content = xml_content
    
    def set_jinja_template(self, jinja_template):
        self.jinja_template = jinja_template
    
    def render_pdf(self):
        print(
            f"""
            Rendering [{self.xml_content}] XML data using the [{self.jinja_template}] Jinja template.
            <a beautiful PDF>
            """
        )


class BaseReport:
    def set_content(self, content):
        ...
    
    def set_template(self, template):
        ...
    
    def render(self):
        ...


class WebReport(BaseReport):

    def set_content(self, json_content):
        self.json_content = json_content
    
    def set_template(self, django_template):
        self.django_template = django_template
    
    def render(self):
        print(
            f"""
            Rendering [{self.json_content}] JSON data using the [{self.django_template}] Django template.
            <a beautiful webpage>
            """
        )


class PDFReportAdapter(BaseReport):
    # Write an adapter class to adapt the PDFReport class
    # You'll need to "convert" the data (change "JSON" to "XML" and "Django" to "Jinja" in the strings)
    # Also, notice that some of the method names in WebReport and PDFReport are different

    def __init__(self, pdf_report: PDFReport):
      self.pdf_report = pdf_report
    
    def set_content(self, json_content):
      xml_content = json_content.replace("JSON", "XML")
      self.pdf_report.set_xml_content(xml_content)
    
    def set_template(self, django_template):
        jinja_template = django_template.replace("Django", "Jinja")
        self.pdf_report.set_jinja_template(jinja_template)
    
    def render(self):
        self.pdf_report.render_pdf()


class ReportClient:

    def build_report(report, content, template) -> BaseReport:
        report.set_content(content)
        report.set_template(template)

        return report

    
    def render_report(report: BaseReport):
        return report.render()


def main():
    print("Data has arrived, generating reports!!")

    json_content = "<Some awesome JSON content>"
    django_template = "<A really beautiful Django Template>"

    print("\nGenerating a Web report")
    web_report = ReportClient.build_report(
        WebReport(),
        json_content,
        django_template,
    )
    ReportClient.render_report(web_report)

    print("\nGenerating a PDF report")
    # Generate a PDF report here, using your new adapter class
    adapted_pdf_report = PDFReportAdapter(PDFReport())
    pdf_report = ReportClient.build_report(
        adapted_pdf_report,
        json_content,
        django_template,
    )
    ReportClient.render_report(pdf_report)


if __name__ == "__main__":
    main()
