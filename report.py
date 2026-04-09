from datetime import datetime
import data_layer.models as models
import service_layer.service as services

def generate_reports():
    print("Generating reports...")

    # Markdown Report
    with open("report.md", "w", encoding="utf-8") as f:
        f.write("# College Course Registration Report\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        f.write("## Professors\n")
        for p in models.list_professors():
            f.write(f"-  {p[1]} {p[2]}  ({p[3]}) — {p[4]}\n")

        f.write("\n## Students\n")
        for s in models.list_students():
            f.write(f"-  {s[1]} {s[2]}  — {s[4]} (Year {s[5]}) — {s[3]}\n")

        f.write("\n## Classes\n")
        for c in models.list_classes():
            f.write(f"-  {c[1]}  taught by {c[2]} ({c[3]})\n")

        f.write("\n## Enrollments\n")
        for e in models.list_enrollments():
            f.write(f"- {e[1]} enrolled in  {e[2]}  ({e[3]})\n")

    # Html report
    with open("report.html", "w", encoding="utf-8") as f:
        f.write("<html><head><title>Registration Report</title></head><body>")
        f.write(f"<h1>College Course Registration Report</h1>")
        f.write(f"<p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>")

        # Professors Table
        f.write("<h2>Professors</h2>")
        f.write("<table border='1' cellpadding='8' cellspacing='0'>")
        f.write("<tr><th>ID</th><th>First Name</th><th>Last Name</th><th>Department</th><th>Email</th></tr>")
        for p in services.list_professors():
            f.write(f"<tr><td>{p[0]}</td><td>{p[1]}</td><td>{p[2]}</td><td>{p[3]}</td><td>{p[4]}</td></tr>")
        f.write("</table><br>")

        # Students Table
        f.write("<h2>Students</h2>")
        f.write("<table border='1' cellpadding='8' cellspacing='0'>")
        f.write("<tr><th>ID</th><th>First Name</th><th>Last Name</th><th>Email</th><th>Major</th><th>Year</th></tr>")
        for s in services.list_students():
            f.write(f"<tr><td>{s[0]}</td><td>{s[1]}</td><td>{s[2]}</td><td>{s[3]}</td><td>{s[4]}</td><td>{s[5]}</td></tr>")
        f.write("</table><br>")

        # Classes Table
        f.write("<h2>Classes</h2>")
        f.write("<table border='1' cellpadding='8' cellspacing='0'>")
        f.write("<tr><th>ID</th><th>Class Name</th><th>Professor</th><th>Semester</th><th>Max Students</th></tr>")
        for c in services.list_classes():
            f.write(f"<tr><td>{c[0]}</td><td>{c[1]}</td><td>{c[2]}</td><td>{c[3]}</td><td>{c[4]}</td></tr>")
        f.write("</table><br>")

        # Enrollments Table
        f.write("<h2>Enrollments</h2>")
        f.write("<table border='1' cellpadding='8' cellspacing='0'>")
        f.write("<tr><th>ID</th><th>Student</th><th>Class</th><th>Semester</th></tr>")
        for e in services.list_enrollments():
            f.write(f"<tr><td>{e[0]}</td><td>{e[1]}</td><td>{e[2]}</td><td>{e[3]}</td></tr>")
        f.write("</table>")

        f.write("</body></html>")

    print("Reports generated!")
    print("report.md")
    print("report.html")
