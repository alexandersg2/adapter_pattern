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


class WebReport:

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


class PDFReportAdapter(WebReport):
    # Write an adapter class to adapt the PDFReport class
    # You'll need to "convert" the data - use a print statement: print("Converted json to xml")
    # Also, notice that some of the method names in WebReport and PDFReport are different
    ...


class ReportClient:

    def build_report(report, content, template) -> WebReport:
        report.set_content(content)
        report.set_template(template)

        return report

    
    def render_report(report: WebReport):
        return report.render()


def main():
    print("Data has arrived, generating reports!!")

    report_client = ReportClient

    print("\nGenerating a Web report")
    web_report = report_client.build_report(
        WebReport(),
        "<Some awesome JSON content>",
        "<A really beautiful Django Template>",
    )
    report_client.render_report(web_report)

    print("\nGenerating a PDF report")
    xml_content = "<Some interesting XML content>"
    jinja_template = "<A rather pretty Jinja template>"
    # Generate a PDF report here, using your new adapter class


if __name__ == "__main__":
    main()
